from interprete.extra.enviroment import Enviroment
from .Expresion import Expresion
from interprete.expresiones.Literal import Literal
from interprete.extra.tipos import *
from interprete.extra.enviroment import Enviroment
from interprete.extra.generador import Generador

class TipoChars(Expresion):
    def __init__(self, text_val:int,charTipo:TipoDato, valor:Literal):
        self.text_val = text_val
        self.charTipo = charTipo
        self.valor = valor
        
    def ejecutar(self, env:Enviroment):
        return self.valor.ejecutar(env)

    def ejecutar3d(self, env:Enviroment, generador:Generador):
        pass