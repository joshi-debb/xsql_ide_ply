from interprete.instrucciones.bloque import Bloque
from interprete.extra.tipos import TipoDato
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion
from interprete.expresiones.Expresion import Expresion
from interprete.extra.retorno import Retorno
from interprete.extra.errores import *
from interprete.instrucciones.when import When

class Case(Instruccion):

    def __init__(self, text_val:str, lista_when:When, _else:bool, bloque_else:Bloque, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.lista_when = lista_when
        self._else = _else
        self.bloque_else = bloque_else
    
    def ejecutar(self, env: Enviroment):
        print('CASE: ')
        print(self.text_val)
        return super().ejecutar(env)