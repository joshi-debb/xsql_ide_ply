from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato
from interprete.extra.retorno import Retorno
from interprete.extra.enviroment import Enviroment

class Substraer(Expresion):
    
    def __init__(self, text_val:str, op1:Expresion, inicio:Expresion, longitud:Expresion, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.op1 = op1
        self.inicio = inicio
        self.longitud = longitud
    
    def ejecutar(self, env:Enviroment):
        print('SUBSTRAER: text_val: ', self.text_val)
        print('------------------ SUBSTRAER --------------------------')
        op1:Retorno = self.op1.ejecutar(env)
        inicio:Retorno = self.inicio.ejecutar(env)
        longitud:Retorno = self.longitud.ejecutar(env)
        resultado = Retorno(tipo=TipoDato.ERROR, valor=None)

        if op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR:
            resultado.tipo = TipoDato.NVARCHAR
            resultado.valor = op1.valor[inicio.valor:longitud.valor+inicio.valor]
            print("La substraccion es: ", resultado.valor)
        print('-----------------------------------------------------')

        return resultado