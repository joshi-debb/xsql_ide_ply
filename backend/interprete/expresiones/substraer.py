from interprete.extra.ast import *
from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato
from interprete.extra.retorno import Retorno
from interprete.extra.enviroment import Enviroment
from interprete.extra.generador import Generador

class Substraer(Expresion):
    
    def __init__(self, text_val:str, op1:Expresion, inicio:Expresion, longitud:Expresion, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.op1 = op1
        self.inicio = inicio
        self.longitud = longitud
    
    def ejecutar(self, env:Enviroment):
        op1:Retorno = self.op1.ejecutar(env)
        inicio:Retorno = self.inicio.ejecutar(env)
        longitud:Retorno = self.longitud.ejecutar(env)
        resultado = Retorno(tipo=TipoDato.ERROR, valor=None)

        if op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR:
            resultado.tipo = TipoDato.NVARCHAR
            resultado.valor = op1.valor[inicio.valor:longitud.valor+inicio.valor]

        return resultado
    
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='SUBSTRAER()', hijos=[])
        raiz.addHijo(hijo)
        id = AST.generarId()
        self.op1.recorrerArbol(hijo)
        self.inicio.recorrerArbol(hijo)
        self.longitud.recorrerArbol(hijo)
    
    def ejecutar3d(self, env:Enviroment, generador:Generador):
        pass