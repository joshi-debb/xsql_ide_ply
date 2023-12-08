from .instruccion import Instruccion

class CrearBD(Instruccion):
    
    def __init__(self, id, linea:int, columna:int):
        super().__init__(linea, columna)
        self.id = id
    
    def ejecutar(self):
        print(self.id)