from interprete.extra.ast import *
from interprete.extra.retorno import Retorno
from interprete.expresiones.Expresion import Expresion
from interprete.instrucciones.instruccion import Instruccion
from interprete.extra.enviroment import Enviroment
from interprete.expresiones._return import Return

class Bloque(Instruccion):

    def __init__(self, text_val:str, instrucciones:Instruccion, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self, env: Enviroment):
        try:
            for instruccion in self.instrucciones:
                ret = instruccion.ejecutar(env)
                if isinstance(ret, Return) or isinstance(ret, Retorno):
                    return ret
        except Exception as e:
            print(f"Error inesperado: {e}")
        return self
    
    def recorrerArbol(self, raiz:Nodo):
        for instruccion in self.instrucciones:
            instruccion.recorrerArbol(raiz)
            