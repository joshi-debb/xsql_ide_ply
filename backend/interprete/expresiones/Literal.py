from interprete.extra.tipos import TipoDato
from .Expresion import Expresion
from interprete.extra.retorno import Retorno

class Literal(Expresion):
    def __init__(self, tipo, valor, linea:int, columna:int):
        super().__init__(linea, columna)
        self.valor = valor
        self.tipo = tipo
    
    def ejecutar(self):
        if self.tipo == TipoDato.NCHAR or self.tipo == TipoDato.NVARCHAR:
            self.valor = self.valor.replace("\\n", "\n").replace("\\\\", "\\").replace("\\r", "\r").replace("\\t", "\t").replace("\\\"", "\"").replace("\\\'", "\'").replace("\"", "").replace("\'", "")
        return Retorno(tipo=self.tipo, valor=self.valor)