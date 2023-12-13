from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion

class AccesoAtributo(Instruccion):
    
    def __init__(self, table_name:str, atribute_name:str, linea:int, columna:int):
        super().__init__(linea, columna)
        self.table_name = table_name
        self.atribute_name = atribute_name
    
    def ejecutar(self, env: Enviroment):
        pass