from interprete.extra.enviroment import Enviroment

class Expresion:
    def __init__(self, linea, columna) -> None:
        self.linea:int = linea
        self.columna:int = columna
    
    def ejecutar(self, env:Enviroment):
        pass