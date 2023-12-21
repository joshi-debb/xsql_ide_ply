from interprete.expresiones.tipoChars import TipoChars
from interprete.extra.ast import *
from interprete.extra.tipos import *

class Atributo:
    def __init__(self, text_val:str, id, tipo:TipoDato, parametros:TipoOpciones, linea:int, columna:int):
        self.text_val = text_val
        self.id = id
        self.tipo = tipo
        self.parametros = parametros
        self.linea = linea
        self.columna = columna
    
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='ATRIBUTO', hijos=[])
        raiz.addHijo(hijo)
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor=self.id, hijos=[]))
        id = AST.generarId()
        if isinstance(self.tipo, TipoChars):
            hijo.addHijo(Nodo(id=id, valor=self.tipo.charTipo.name, hijos=[]))
        else:
            hijo.addHijo(Nodo(id=id, valor=self.tipo.name, hijos=[]))

        tipo = ''
        for parametro in self.parametros:
            id = AST.generarId()
            hijo.addHijo(Nodo(id=id, valor=parametro.name, hijos=[]))
