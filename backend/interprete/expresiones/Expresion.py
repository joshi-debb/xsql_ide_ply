from interprete.extra.enviroment import Enviroment

class Expresion:
    def __init__(self,  text_val:str='', linea=0, columna=0) -> None:
        self.text_val = text_val
        self.linea:int = linea
        self.columna:int = columna
    
    def ejecutar(self, env:Enviroment):
        pass