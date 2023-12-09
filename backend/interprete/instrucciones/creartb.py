from .instruccion import Instruccion
from .atributo import Atributo

from xml.dom import minidom

class CrearTB(Instruccion):
    def __init__(self, id, atributo:Atributo , linea:int, columna:int):
        super().__init__(linea, columna)
        self.id = id
        self.atributos = atributo
    
    def ejecutar(self):
        print(self.id)
        for atributo in self.atributos:
            print(atributo.id)
            print(atributo.tipo)
            for parametro in atributo.parametros:
                print(parametro)