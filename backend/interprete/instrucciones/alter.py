
from interprete.instrucciones.instruccion import Instruccion
from interprete.extra.tipos import TipoDato


from xml.dom import minidom


class AlterADD(Instruccion):
    def __init__(self, name_table, campo, tipo:TipoDato , linea:int, columna:int):
        self.name_table = name_table
        self.campo = campo
        self.tipo = tipo
        
    def ejecutar(self):
        print("AlterADD")
        print(self.name_table)
        print(self.campo)
        print(self.tipo)
        
    

class AlterDROP(Instruccion):
    def __init__(self, name_table, campo, line, column):
        self.name_table = name_table
        self.campo = campo
        self.line = line
        self.columna = column
    
    def ejecutar(self):
        print("AlterDROP")
        print(self.name_table)
        print(self.campo)