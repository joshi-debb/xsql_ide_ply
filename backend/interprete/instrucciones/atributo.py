from interprete.extra.tipos import *

class Atributo:
    def __init__(self, text_val:str, id, tipo:TipoDato, parametros:TipoOpciones, linea:int, columna:int):
        self.text_val = text_val
        self.id = id
        self.tipo = tipo
        self.parametros = parametros
        self.linea = linea
        self.columna = columna