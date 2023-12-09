from .Expresion import Expresion

class Literal(Expresion):
    def __init__(self, tipo, valor, linea:int, columna:int):
        super().__init__(linea, columna)
        self.valor = valor
        self.tipo = tipo
    
    def ejecutar(self):
        return self.valor