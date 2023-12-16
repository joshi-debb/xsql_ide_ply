from .instruccion import Instruccion
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.declaracion_var import Declaracion
from interprete.instrucciones.bloque import Bloque
from interprete.extra.tipos import TipoDato

class Function(Instruccion):

    def __init__(self, text_val:str, tipo_ret:TipoDato, id:str, parametros:Instruccion, instrucciones:Bloque, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.tipo_ret = tipo_ret
        self.id = id
        self.parametros = parametros
        self.instrucciones = instrucciones
    
    def ejecutar(self, env: Enviroment):
        print('FUNCION: ')
        print(self.text_val)
        # Guardar en XML
        return super().ejecutar(env)