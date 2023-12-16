from interprete.extra.enviroment import Enviroment
from interprete.expresiones.Expresion import Expresion
from interprete.instrucciones.instruccion import Instruccion
from interprete.extra.tipos import TipoDato
from interprete.expresiones.tipoChars import TipoChars

class Argumento(Instruccion):

    def __init__(self, text_val:str, id:str, expresion:Expresion, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.id = id
        self.expresion = expresion
    
    def ejecutar(self, env: Enviroment):
        return super().ejecutar(env)