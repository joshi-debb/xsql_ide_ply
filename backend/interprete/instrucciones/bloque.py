from interprete.extra.retorno import Retorno
from interprete.expresiones.Expresion import Expresion
from interprete.instrucciones.instruccion import Instruccion
from interprete.extra.enviroment import Enviroment
from interprete.expresiones._return import Return

class Bloque(Instruccion):

    def __init__(self, text_val:str, instrucciones:Instruccion, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self, env: Enviroment):
        # Creando nuevo entorno
        # new_env = Enviroment(ent_anterior=env, ambito="Local")
        # Ejecutando las instrucciones
        # try:
        for instruccion in self.instrucciones:
            ret = instruccion.ejecutar(env)
            if isinstance(ret, Return) or isinstance(ret, Retorno):
                return ret
        # except Exception as e:
            # print(f'ERROR: en la linea: {self.linea} y columna: {self.columna}')

        return self