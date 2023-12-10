from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato
from interprete.extra.retorno import Retorno


class Substraer(Expresion):
    
    def __init__(self, op1:Expresion, inicio:Expresion, longitud:Expresion, linea:int, columna:int):
        super().__init__(linea, columna)
        self.op1 = op1
        self.inicio = inicio
        self.longitud = longitud
    
    def ejecutar(self):
        print('------------------ SUBSTRAER --------------------------')
        op1:Retorno = self.op1.ejecutar()
        inicio:Retorno = self.inicio.ejecutar()
        longitud:Retorno = self.longitud.ejecutar()
        resultado = Retorno(tipo=TipoDato.ERROR, valor=None)

        if op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR:
            resultado.tipo = TipoDato.NVARCHAR
            resultado.valor = op1.valor[inicio.valor:longitud.valor+inicio.valor]
            print("La substraccion es: ", resultado.valor)
        print('-----------------------------------------------------')

        return resultado