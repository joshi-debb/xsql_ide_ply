from interprete.extra.ast import *
from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato
from interprete.extra.retorno import Retorno
from datetime import datetime
from interprete.extra.enviroment import Enviroment
from interprete.extra.generador import Generador

class Hoy(Expresion):
    
    def __init__(self, text_val:str, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
    
    def ejecutar(self, env:Enviroment):
        # Obtener la fecha y hora actual
        now = datetime.now()
        
        # Formatear la fecha y hora sin segundos
        formato = "%Y-%m-%d %H:%M"
        fecha_hora_formateada = now.strftime(formato)
        resultado = Retorno(tipo=TipoDato.DATETIME, valor=fecha_hora_formateada)

        return resultado
    
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='HOY()', hijos=[])
        raiz.addHijo(hijo)
    
    def ejecutar3d(self, env:Enviroment, generador:Generador):
        pass