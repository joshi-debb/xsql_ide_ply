
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion
from xml.dom import minidom
from interprete.expresiones.concatenar import Concatenar


class Select(Instruccion):
    def __init__(self, opciones, linea, columna):
        self.opciones = opciones
        self.linea = linea
        self.columna = columna

<<<<<<< HEAD
    def ejecutar(self):
        if (isinstance(self.opciones, Concatenar)):
            self.opciones = self.opciones.concatenar()
=======
    def ejecutar(self, env:Enviroment):
        print("ejecutar select")
        print(self.opciones)

>>>>>>> 7ad632a52e930145e6092ddb425fe4f079697849
