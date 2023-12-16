from interprete.extra.tipos import TipoDato
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion
from interprete.expresiones.Expresion import Expresion
from interprete.extra.retorno import Retorno
from interprete.extra.errores import *
from interprete.instrucciones.bloque import Bloque

class When(Instruccion):

    def __init__(self, text_val:str, condicion:Expresion, bloque:Bloque, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.condicion = condicion
        self.bloque = bloque
    
    def ejecutar(self, env: Enviroment):
        return super().ejecutar(env)