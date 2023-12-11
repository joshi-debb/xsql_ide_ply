
from interprete.instrucciones.instruccion import Instruccion
from xml.dom import minidom

class Select(Instruccion):
    def __init__(self, opciones, linea, columna):
        self.opciones = opciones
        self.linea = linea
        self.columna = columna

    def ejecutar(self):
        print("ejecutar select")
        print(self.opciones)

