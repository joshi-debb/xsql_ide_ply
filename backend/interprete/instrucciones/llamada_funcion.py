
from interprete.instrucciones.function import Function
from interprete.instrucciones.instruccion import Instruccion
from interprete.extra.enviroment import Enviroment
from interprete.extra.errores import *
from interprete.extra.tipos import TipoSimbolo
from interprete.extra.symbol import Symbol
from interprete.extra.tipos import TipoDato
from interprete.extra.retorno import Retorno
from interprete.instrucciones.asignacion_var import AsignacionVar
from interprete.instrucciones.argumento import Argumento
from interprete.expresiones._return import Return

# Esta clase buscará la funcion en el XML
class LlamadaFnc(Instruccion):
    def __init__(self, text_val, nombre_fnc, argumentos:Argumento, linea, columna):
        super().__init__(text_val, linea, columna)
        self.nombre_fnc = nombre_fnc
        if argumentos[0] == None: self.argumentos = []
        else:                     self.argumentos = argumentos

    def ejecutar(self, env:Enviroment):
        from analizador.parser import parser

        # Validar que exista el procedimiento self.nombre_proc en la base de datos en uso

        # Si existe, leer la funcion y parsearla
        text = ''
        with open('backend/ejemplo.txt', 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Obteniendo la Funcion
        instruccion:Function = parser.parse(text.lower())[0]

        # Guardando la funcion en la tabla de simbolos
        instruccion.guardarEnTablaSimbolos(env)
        
        # Obteniendo la funcion de la tabla de simbolos
        simbolo = env.getSimbolo(self.nombre_fnc, TipoSimbolo.FUNCTION)

        # Creando un nuevo entorno
        new_env = Enviroment(ent_anterior=env, ambito="FUNCTION")
        new_env.setDentroFuncion(True)

        # Validar que la llamada tenga la misma cantidad de parametros que recibe la función
        if len(self.argumentos) != len(simbolo.parametros):
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'La llamada al procedimiento debe tener la misma cantidad de argumentos que el procedimiento "{self.nombre_proc}"')
            TablaErrores.addError(err)
            return Retorno(tipo=TipoDato.ERROR, valor=None)

        # Parametros que recibe la función en su declaracion
        parametros = simbolo.parametros

        # Declarando los parametros
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

        # Asignando los parametros de la funcion con los valores dados en la llamada
        for asignacion in asignaciones:
            asignacion.ejecutar(new_env)
        
        # Ejecutando las instrucciones dentro de la función
        ret = simbolo.instrucciones.ejecutar(new_env)

        # Validando que venga un 'RETURN'
        if isinstance(ret, Return):
            exp:Retorno = ret.exp_ret.ejecutar(new_env)
            # Validar que el retorno sea del mismo tipo
            if instruccion.getTipoRetorno() != exp.tipo:
                err = Error(tipo='Semántico', linea=ret.linea, columna=ret.columna, descripcion=f'La sentencia RETURN debe retornar el mismo tipo especificado en la función y no un tipo {exp.tipo.name}')
                TablaErrores.addError(err)
                return Retorno(tipo=TipoDato.ERROR, valor=None)
            return exp

        else:
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'La función {self.nombre_fnc} debe retornar una expresión.')
            TablaErrores.addError(err)

        return Retorno(tipo=TipoDato.ERROR, valor=None)