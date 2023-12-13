from interprete.instrucciones.instruccion import Instruccion
from interprete.extra.enviroment import Enviroment

class Bloque(Instruccion):

    def __init__(self, instrucciones:Instruccion, linea:int, columna:int):
        super().__init__(linea, columna)
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self, env: Enviroment):
        # Creando nuevo entorno
        new_env = Enviroment(ent_anterior=env, ambito="Local")
        
        # Ejecutando las instrucciones
        try:
            for instruccion in self.instrucciones:
                instruccion.ejecutar(new_env)
        except Exception as e:
            print(f'ERROR: en la linea: {self.linea} y columna: {self.columna}')

        return self