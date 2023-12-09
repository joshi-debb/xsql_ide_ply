
from .instruccion import Instruccion

class Use(Instruccion):
    def __init__(self, id, line, column):
        self.id = id
        self.line = line
        self.column = column
        
    def ejecutar(self):
        print ("base actual: ", self.id)