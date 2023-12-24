from interprete.extra.ast import *
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
from xml.dom import minidom
from interprete.extra.generador import Generador


# Esta clase buscará la funcion en el XML
class LlamadaFnc(Instruccion):
    def __init__(self, text_val, nombre_fnc, argumentos:Argumento, linea, columna):
        super().__init__(text_val, linea, columna)
        self.nombre_fnc = nombre_fnc
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
                functions = elem.getElementsByTagName('function')
                for function in functions:
                    if function.getAttribute('name') == self.nombre_fnc:
                        self.text = str(function.firstChild.data)
                        break
        
        if self.text == '':
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'La función "{self.nombre_fnc}" no existe.')
            TablaErrores.addError(err)
            return Retorno(tipo=TipoDato.ERROR, valor=None)
        
        # Obteniendo la Funcion
        instruccion:Function = parser.parse(self.text.lower())[0]
        
        if not env.existe_simbolo_ent_actual(self.nombre_fnc, TipoSimbolo.FUNCTION):
            # Guardando la funcion en la tabla de simbolos
            instruccion.guardarEnTablaSimbolos(env)
        
        # Obteniendo la funcion de la tabla de simbolos
        simbolo = env.getSimbolo(self.nombre_fnc, TipoSimbolo.FUNCTION)

        # Creando un nuevo entorno
        new_env = Enviroment(ent_anterior=env, ambito="FUNCTION")
        new_env.setDentroFuncion(True)

        # Validar que la llamada tenga la misma cantidad de parametros que recibe la función
        if len(self.argumentos) != len(simbolo.parametros):
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'La llamada al procedimiento debe tener la misma cantidad de argumentos que el procedimiento "{self.nombre_fnc}"')
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
                        err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Los argumentos deben tener la misma estructura en la llamada al function "{self.nombre_fnc}"')
                        TablaErrores.addError(err)
                        return Retorno(tipo=TipoDato.ERROR, valor=None)

                    if parametro.id == argumento.id:
                        asignaciones.append(AsignacionVar('', parametro.id, argumento.expresion, self.linea, self.columna))
        else:
            i = 0
            for parametro in parametros:
                if self.argumentos[i].id != None:
                    err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Los argumentos deben tener la misma estructura en la llamada al function "{self.nombre_fnc}"')
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

    # self.nombre_fnc = nombre_fnc
    # if argumentos[0] == None: self.argumentos = []
    # else:                     self.argumentos = argumentos
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='LLAMADA FUNCION', hijos=[])
        raiz.addHijo(hijo)
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor=self.nombre_fnc, hijos=[]))
        
        # Argumentos
        if len(self.argumentos) != 0:
            id = AST.generarId()
            hijo2 = Nodo(id=id, valor='ARGUMENTOS', hijos=[])
            hijo.addHijo(hijo2)
            for argumento in self.argumentos:
                argumento.recorrerArbol(hijo2)
    
    def ejecutar3d(self, env: Enviroment, generador: Generador):
        pass