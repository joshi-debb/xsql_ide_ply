from interprete.instrucciones.instruccion import Instruccion
from interprete.expresiones.Expresion import Expresion
from interprete.extra.enviroment import Enviroment

class CondicionWhere(Instruccion):
    def __init__(self, text_val:str, id:str, expresion:Expresion, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.id = id
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