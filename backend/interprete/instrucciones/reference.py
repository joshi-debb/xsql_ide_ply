
from interprete.instrucciones.instruccion import Instruccion

class Reference(Instruccion):
    def __init__(self, name_table, atributo_referenciado ,linea: int, columna: int):
        self.name_table = name_table
        self.atributo_referenciado = atributo_referenciado
        self.linea = linea
        self.columna = columna

    def ejecutar(self):
        pass
        