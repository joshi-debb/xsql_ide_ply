from interprete.extra.tipos import *

class Atributo:
    def __init__(self, id, tipo:TipoDato, parametros:TipoOpciones, linea:int, columna:int):
        self.id = id
        self.tipo = tipo
        self.parametros = parametros
        self.linea = linea
        self.columna = columna