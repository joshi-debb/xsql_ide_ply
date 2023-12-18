from interprete.extra.tipos import TipoDato
from .Expresion import Expresion
from interprete.extra.retorno import Retorno
from interprete.extra.enviroment import Enviroment

class Literal(Expresion):
    def __init__(self, text_val:str, tipo, valor, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.valor = valor
        self.tipo = tipo
    
    def ejecutar(self, env:Enviroment):
        if self.tipo == TipoDato.NCHAR or self.tipo == TipoDato.NVARCHAR:
            self.valor = self.valor.replace("\\n", "\n").replace("\\\\", "\\").replace("\\r", "\r").replace("\\t", "\t").replace("\\\"", "\"").replace("\\\'", "\'").replace("\"", "").replace("\'", "")

        return Retorno(tipo=self.tipo, valor=self.valor)