from interprete.extra.enviroment import Enviroment
from interprete.extra.generador import Generador


class Instruccion:
    def __init__(self, text_val:str='', linea: int = 0, columna: int = 0) -> None:
        self.text_val = text_val
        self.linea: int = linea;
        self.columna: int = columna;

    def ejecutar(self, env:Enviroment):
        pass

    def ejecutar3d(self, env:Enviroment, generador:Generador):
        pass