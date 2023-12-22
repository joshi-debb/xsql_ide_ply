from interprete.extra.ast import *
from interprete.extra.enviroment import Enviroment
from interprete.expresiones.Expresion import Expresion
from interprete.instrucciones.instruccion import Instruccion
from interprete.extra.tipos import TipoDato
from interprete.expresiones.tipoChars import TipoChars

class Argumento(Instruccion):

    def __init__(self, text_val:str, id:str, expresion:Expresion, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.id = id
        self.expresion = expresion
    
    def ejecutar(self, env: Enviroment):
        return super().ejecutar(env)
    
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='ARGUMENTO', hijos=[])
        raiz.addHijo(hijo)
        if self.id != None:
            id = AST.generarId()
            hijo.addHijo(Nodo(id=id, valor=self.id, hijos=[]))
        self.expresion.recorrerArbol(hijo)