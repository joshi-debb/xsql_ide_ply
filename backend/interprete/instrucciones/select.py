
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion
from xml.dom import minidom

class Select(Instruccion):
    def __init__(self, opciones, linea, columna):
        self.opciones = opciones
        self.linea = linea
        self.columna = columna

    def ejecutar(self, env:Enviroment):
        print("ejecutar select")
        print(self.opciones)

