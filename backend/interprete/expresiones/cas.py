from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato
from interprete.extra.retorno import Retorno
from interprete.extra.enviroment import Enviroment

class Cas(Expresion):
    
    def __init__(self, text_val:str, op:Expresion, tipo:TipoDato, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.op1 = op
        self.tipo = tipo
    
    def ejecutar(self, env: Enviroment):
        print('CAS -> text_val: ', self.text_val)
        return super().ejecutar(env)