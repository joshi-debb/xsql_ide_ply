from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato
from interprete.extra.retorno import Retorno
from interprete.extra.enviroment import Enviroment

class Concatenar(Expresion):
    
    def __init__(self, text_val:str, op1:Expresion, op2:Expresion, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.op1 = op1
        self.op2 = op2
    
    def ejecutar(self, env:Enviroment):
        op1:Retorno = self.op1.ejecutar(env)
        op2:Retorno = self.op2.ejecutar(env)
        resultado = Retorno(tipo=TipoDato.ERROR, valor=None)

        if (op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR) or (op2.tipo == TipoDato.NCHAR or op2.tipo == TipoDato.NVARCHAR):
            resultado.tipo = TipoDato.NVARCHAR
            resultado.valor = op1.valor + op2.valor

        return resultado