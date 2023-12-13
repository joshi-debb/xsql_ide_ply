from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion

class Between(Instruccion):
    
    def __init__(self, op1:str, op2:str, linea:int, columna:int):
        super().__init__(linea, columna)
        self.op1 = op1
        self.op2 = op2
    
    def ejecutar(self, env: Enviroment):
        pass