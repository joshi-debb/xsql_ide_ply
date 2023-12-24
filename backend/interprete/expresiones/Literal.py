from interprete.extra.ast import *
from interprete.extra.tipos import TipoDato
from .Expresion import Expresion
from interprete.extra.retorno import Retorno, Retorno3d
from interprete.extra.enviroment import Enviroment
from interprete.extra.generador import Generador
from interprete.instrucciones.instruccion import Instruccion

class Literal(Expresion):
    def __init__(self, text_val:str, tipo, valor, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.valor = valor
        self.tipo = tipo
    
    def ejecutar(self, env:Enviroment):
        if self.tipo == TipoDato.NCHAR or self.tipo == TipoDato.NVARCHAR or self.tipo == TipoDato.DATE or self.tipo == TipoDato.DATETIME:
            self.valor = self.valor.replace("\\n", "\n").replace("\\\\", "\\").replace("\\r", "\r").replace("\\t", "\t").replace("\\\"", "\"").replace("\\\'", "\'").replace("\"", "").replace("\'", "")
            
        return Retorno(tipo=self.tipo, valor=self.valor)
    
    def ejecutar3d(self, env:Enviroment, generador:Generador):
        codigo = ''
        temp = ''
        
        if self.tipo == TipoDato.DECIMAL or self.tipo == TipoDato.INT:
            temp = generador.obtenerTemporal()
            codigo += f'{temp} = {self.valor};\n'
        
        elif self.tipo == TipoDato.NVARCHAR or self.tipo == TipoDato.NCHAR:
            temp = generador.obtenerTemporal()
            codigo += f'{temp} = HP;\n'
            for c in self.valor:
                codigo += f'heap[HP] = {ord(c)};\n'
                codigo += f'HP = HP + 1;\n'
            codigo += f'heap[HP] = 0;\n'
            codigo += f'HP = HP + 1;\n'
            
        generador.agregarInstruccion(codigo)
        
        retorno_c3d = Retorno3d()
        
        retorno_c3d.iniciarRetorno(codigo, '', temp, self.tipo)
            
        return retorno_c3d
    
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor=self.valor, hijos=[])
        raiz.addHijo(hijo)
    
    def ejecutar3d(self, env:Enviroment, generador:Generador):
        pass