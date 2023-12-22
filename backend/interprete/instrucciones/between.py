from interprete.extra.ast import *
from interprete.expresiones.Expresion import Expresion
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion

class Between(Instruccion):
    
    def __init__(self, text_val:str, campo:str, op1:Expresion, op2:Expresion, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.campo = campo
        self.op1 = op1
        self.op2 = op2
        self.operador = ''
    
    def ejecutar(self, env: Enviroment):
        if 'OR' in self.text_val:
            self.operador = 'OR'
        elif 'AND' in self.text_val:
            self.operador = 'AND'
    
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='BETWEEN', hijos=[])
        raiz.addHijo(hijo)                                    
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor=self.campo, hijos=[]))     
        self.op1.recorrerArbol(hijo)
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor='&&', hijos=[]))     
        self.op2.recorrerArbol(hijo) 