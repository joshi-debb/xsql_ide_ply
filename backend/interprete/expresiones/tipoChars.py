from .Expresion import Expresion
from interprete.expresiones.Literal import Literal
from interprete.extra.tipos import *

class TipoChars(Expresion):
    def __init__(self, charTipo:TipoDato, valor:Literal):
        self.charTipo = charTipo
        self.valor = valor
        
    def ejecutar(self):
        return self.valor.ejecutar()