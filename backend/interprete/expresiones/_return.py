from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato
from interprete.extra.retorno import Retorno
from interprete.extra.enviroment import Enviroment

class Return(Expresion):

    def __init__(self, text_val:str, exp_ret:Expresion, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.exp_ret = exp_ret
    
    def ejecutar(self, env: Enviroment):
        return self     # Retornando la clase en sí