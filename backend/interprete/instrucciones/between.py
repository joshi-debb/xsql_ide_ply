from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion

class Between(Instruccion):
    
    def __init__(self, text_val:str, op1:str, op2:str, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.op1 = op1
        self.op2 = op2
        self.operador = ''
    
    def ejecutar(self, env: Enviroment):
        if 'OR' in self.text_val:
            self.operador = 'OR'
        elif 'AND' in self.text_val:
            self.operador = 'AND'