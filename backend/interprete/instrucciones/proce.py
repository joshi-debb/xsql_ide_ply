from interprete.extra.tipos import TipoDato
from .instruccion import Instruccion
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.declaracion_var import Declaracion
from interprete.instrucciones.bloque import Bloque

class Proce(Instruccion):
    def __init__(self, text_val:str, id:str, parametros:Declaracion, instrucciones:Bloque, linea, columna):
        super().__init__(text_val, linea, columna)
        self.id = id
        self.parametros = parametros
        self.instrucciones = instrucciones
    
    def ejecutar(self, env: Enviroment):
        print('PROCEDIMIENTO: ', self.text_val)
        return super().ejecutar(env)