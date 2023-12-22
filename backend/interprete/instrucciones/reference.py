from interprete.extra.ast import *
from interprete.instrucciones.instruccion import Instruccion

class Reference(Instruccion):
    def __init__(self, text_val:str, name_table, atributo_referenciado ,linea: int, columna: int):
        super().__init__(text_val, linea, columna)
        self.name_table = name_table
        self.atributo_referenciado = atributo_referenciado
        self.linea = linea
        self.columna = columna

    def ejecutar(self):
        pass
    
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='REFERENCE', hijos=[])
        raiz.addHijo(hijo)
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor=self.name_table, hijos=[]))
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor=self.atributo_referenciado, hijos=[]))
        