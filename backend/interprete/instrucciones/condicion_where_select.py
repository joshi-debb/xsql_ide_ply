from interprete.instrucciones.instruccion import Instruccion
from interprete.expresiones.Expresion import Expresion
from interprete.extra.enviroment import Enviroment

class CondicionWhereSelect(Instruccion):
    def __init__(self, expresion:str, linea:int, columna:int):
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
    
    # No hace nada
    def ejecutar(self, env:Enviroment):
        pass
    
    # Retorna el nombre del campo
    def getId(self):
        return self.id
    
    # Retorna el valor de una condicion
    def getExpresion(self):
        return self.expresion.ejecutar()