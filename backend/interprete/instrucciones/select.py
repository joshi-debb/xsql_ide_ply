
from interprete.instrucciones.instruccion import Instruccion
from xml.dom import minidom
from interprete.expresiones.concatenar import Concatenar


class Select(Instruccion):
    def __init__(self, opciones, linea, columna):
        self.opciones = opciones
        self.linea = linea
        self.columna = columna

    def ejecutar(self):
        if (isinstance(self.opciones, Concatenar)):
            self.opciones = self.opciones.concatenar()