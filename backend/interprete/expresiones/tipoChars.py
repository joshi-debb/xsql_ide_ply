from interprete.extra.enviroment import Enviroment
from .Expresion import Expresion
from interprete.expresiones.Literal import Literal
from interprete.extra.tipos import *
from interprete.extra.enviroment import Enviroment

class TipoChars(Expresion):
    def __init__(self, charTipo:TipoDato, valor:Literal):
        self.charTipo = charTipo
        self.valor = valor
        
    def ejecutar(self, env:Enviroment):
        return self.valor.ejecutar(env)