from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato
from interprete.extra.retorno import Retorno
from datetime import datetime


class Hoy(Expresion):
    
    def __init__(self, linea:int, columna:int):
        super().__init__(linea, columna)
    
    def ejecutar(self):
        print('------------------ HOY --------------------------')
        # Obtener la fecha y hora actual
        now = datetime.now()
        # Formatear la fecha y hora sin segundos
        formato = "%Y-%m-%d %H:%M"
        fecha_hora_formateada = now.strftime(formato)
        resultado = Retorno(tipo=TipoDato.DATETIME, valor=fecha_hora_formateada)
        print("DATETIME: ", fecha_hora_formateada)
        print('-----------------------------------------------------')

        return resultado