
from interprete.expresiones._return import Return
from interprete.instrucciones.asignacion_var import AsignacionVar
from interprete.instrucciones.procedure import Procedure
from interprete.instrucciones.function import Function
from interprete.extra.retorno import Retorno
from interprete.instrucciones.argumento import Argumento
from interprete.instrucciones.instruccion import Instruccion
from interprete.extra.enviroment import Enviroment
from interprete.extra.errores import *
from interprete.extra.tipos import TipoSimbolo
from interprete.extra.symbol import Symbol
from interprete.extra.tipos import TipoDato

# Esta clase buscará el procedimiento en el XML
class Exec(Instruccion):
    def __init__(self, text_val, nombre_proc, argumentos:Argumento, linea, columna):
        super().__init__(text_val, linea, columna)
        self.nombre_proc = nombre_proc
        if argumentos[0] == None: self.argumentos = []
        else:                     self.argumentos = argumentos

    def ejecutar(self, env:Enviroment):
        from analizador.parser import parser
        
        text = ''
        with open('backend/ejemplo.txt', 'r', encoding='utf-8') as file:
            text = file.read()
        
        instruccion:Procedure|Function = parser.parse(text.lower())[0]

        # Guardando la funcion/procedimiento en la tabla de simbolos
        instruccion.guardarEnTablaSimbolos(env)

        # instruccion = parser.parse('cadena')
        simbolo = None

        if isinstance(instruccion, Procedure):
            if not env.existe_simbolo(self.nombre_proc, TipoSimbolo.PROCEDURE):
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'No existe un procedimiento llamado "{self.nombre_proc}"')
                TablaErrores.addError(err)
                return Retorno(tipo=TipoDato.ERROR, valor=None)
            simbolo = env.getSimbolo(self.nombre_proc, TipoSimbolo.PROCEDURE)
            
            # Creando un nuevo entorno 
            new_env = Enviroment(ent_anterior=env, ambito="PROCEDURE")

        elif isinstance(instruccion, Function):
            if not env.existe_simbolo(self.nombre_proc, TipoSimbolo.FUNCTION):
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'No existe una función llamada "{self.nombre_proc}"')
                TablaErrores.addError(err)
                return Retorno(tipo=TipoDato.ERROR, valor=None)
            simbolo = env.getSimbolo(self.nombre_proc, TipoSimbolo.FUNCTION)

            # Creando un nuevo entorno 
            new_env = Enviroment(ent_anterior=env, ambito="FUNCTION")
            new_env.setDentroFuncion(True)

        # Validar que la llamada tenga la misma cantidad de parametros que recibe el procedimiento
        if len(self.argumentos) != len(simbolo.parametros):
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'La llamada al procedimiento debe tener la misma cantidad de argumentos que el procedimiento "{self.nombre_proc}"')
            TablaErrores.addError(err)
            return Retorno(tipo=TipoDato.ERROR, valor=None)

        parametros = simbolo.parametros
        for parametro in parametros:
            parametro.ejecutar(new_env)
        
        asignaciones:AsignacionVar = []

        # Validar si los argumentos se envian de la forma EXEC @precio = 1.50 (asignacion explicita) o solo 1.50 (asignacion no explicita)
        asignacion_explicita = False
        if len(self.argumentos) != 0:
            if self.argumentos[0].id != None:
                asignacion_explicita = True

        if asignacion_explicita:
            for parametro in parametros:
                for argumento in self.argumentos:
                    if argumento.id == None:
                        err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Los argumentos deben tener la misma estructura en la llamada al procedure "{self.nombre_proc}"')
                        TablaErrores.addError(err)
                        return Retorno(tipo=TipoDato.ERROR, valor=None)

                    if parametro.id == argumento.id:
                        asignaciones.append(AsignacionVar('', parametro.id, argumento.expresion, self.linea, self.columna))

        else:
            i = 0
            for parametro in parametros:
                if self.argumentos[i].id != None:
                    err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Los argumentos deben tener la misma estructura en la llamada al procedure "{self.nombre_proc}"')
                    TablaErrores.addError(err)
                    return Retorno(tipo=TipoDato.ERROR, valor=None)

                asignaciones.append(AsignacionVar('', parametro.id, self.argumentos[i].expresion, self.linea, self.columna))
                i += 1

        # Declarar los parametros de la funcion (Declaraciones) en un nuevo entorno
        for asignacion in asignaciones:
            asignacion.ejecutar(new_env)
        
        ret = simbolo.instrucciones.ejecutar(new_env)

        if isinstance(ret, Return):
            if new_env.getDentroFunction():
                exp:Retorno = ret.exp_ret.ejecutar(new_env)
                
                # Validar que el retorno sea del mismo tipo
                if instruccion.getTipoRetorno() != exp.tipo:
                    err = Error(tipo='Semántico', linea=ret.linea, columna=ret.columna, descripcion=f'La sentencia RETURN debe retornar el mismo tipo especificado en la función y no un tipo {exp.tipo.name}')
                    TablaErrores.addError(err)
                    return Retorno(tipo=TipoDato.ERROR, valor=None)
                return exp

            else:
                err = Error(tipo='Semántico', linea=ret.linea, columna=ret.columna, descripcion=f'Solo se puede utilizar la sentencia RETURN dento de una función')
                TablaErrores.addError(err)
                return Retorno(tipo=TipoDato.ERROR, valor=None)

        return Retorno(tipo=TipoDato.ERROR, valor=None)

        