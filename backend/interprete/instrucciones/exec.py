from interprete.extra.ast import *
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
from interprete.extra.generador import Generador


from xml.dom import minidom

# Esta clase buscará el procedimiento en el XML
class Exec(Instruccion):
    def __init__(self, text_val, nombre_proc, argumentos:Argumento, linea, columna):
        super().__init__(text_val, linea, columna)
        self.nombre_proc = nombre_proc
        if argumentos[0] == None: self.argumentos = []
        else:                     self.argumentos = argumentos
        self.text = ''

    def ejecutar(self, env:Enviroment):
        from analizador.parser import parser

        datas = open('backend/structure.xml', 'r+', encoding='utf-8')

        mydoc = minidom.parse(datas)
        current = mydoc.getElementsByTagName('current')[0]  
        bases = mydoc.getElementsByTagName('database')
        
        for elem in bases:
            if elem.getAttribute('name') == current.getAttribute('name'):
                procedures = elem.getElementsByTagName('procedure')
                for procedure in procedures:
                    if procedure.getAttribute('name') == self.nombre_proc:
                        self.text = str(procedure.firstChild.data)
                        break
        
        if self.text == '':
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'El procedimiento "{self.nombre_proc}" no existe.')
            TablaErrores.addError(err)
            return Retorno(tipo=TipoDato.ERROR, valor=None)
        
        # Obteniendo el procedure
        instruccion:Procedure = parser.parse(self.text.lower())[0]

        if not env.existe_simbolo_ent_actual(self.nombre_proc, TipoSimbolo.PROCEDURE):
            # Guardando el procedimiento en la tabla de simbolos
            instruccion.guardarEnTablaSimbolos(env)

        # Obteniendo el procedimiento de la tabla de simbolos    
        simbolo = env.getSimbolo(self.nombre_proc, TipoSimbolo.PROCEDURE)
        
        # Creando un nuevo entorno 
        new_env = Enviroment(ent_anterior=env, ambito="PROCEDURE")            

        # Validar que la llamada tenga la misma cantidad de parametros que recibe el procedimiento
        if len(self.argumentos) != len(simbolo.parametros):
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'La llamada al procedimiento debe tener la misma cantidad de argumentos que el procedimiento "{self.nombre_proc}"')
            TablaErrores.addError(err)
            return Retorno(tipo=TipoDato.ERROR, valor=None)

        # Parametros que recibe el procedimiento en su declaracion
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

        # Asignando los parametros del procedimiento con los valores dados en la llamada
        for asignacion in asignaciones:
            asignacion.ejecutar(new_env)
        
        # Ejecutando las instrucciones dentro del procedimiento
        ret = simbolo.instrucciones.ejecutar(new_env)

        # No puede haber un 'RETURN' dentro de un procedimiento, solo en una función
        if isinstance(ret, Return):
            err = Error(tipo='Semántico', linea=ret.linea, columna=ret.columna, descripcion=f'Solo se puede utilizar la sentencia RETURN dento de una función.')
            TablaErrores.addError(err)

        return Retorno(tipo=TipoDato.ERROR, valor=None) 
    
    # self.nombre_proc = nombre_proc
    # if argumentos[0] == None: self.argumentos = []
    # else:                     self.argumentos = argumentos
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='EXEC', hijos=[])
        raiz.addHijo(hijo)
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor=self.nombre_proc, hijos=[]))
        
        # Argumentos
        if len(self.argumentos) != 0:
            id = AST.generarId()
            hijo2 = Nodo(id=id, valor='ARGUMENTOS', hijos=[])
            hijo.addHijo(hijo2)
            for argumento in self.argumentos:
                argumento.recorrerArbol(hijo2)

    
    def ejecutar3d(self, env: Enviroment, generador: Generador):
        pass