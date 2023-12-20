from interprete.extra.enviroment import Enviroment
from interprete.expresiones.Expresion import Expresion
from interprete.instrucciones.instruccion import Instruccion
from interprete.extra.tipos import TipoDato

class AccesoTabla(Instruccion):

    # Sintaxis: nom_tabla.nom_campo
    def __init__(self, text_val:str, nom_tabla:str, nom_campo:str, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.nom_tabla = nom_tabla
        self.nom_campo = nom_campo
    
    def ejecutar(self, env: Enviroment):
        pass