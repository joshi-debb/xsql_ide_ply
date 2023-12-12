from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato
from interprete.extra.retorno import Retorno
from interprete.instrucciones.condicion_where import CondicionWhere
from interprete.extra.enviroment import Enviroment

class Contar(Expresion):
    
    def __init__(self, table_name:str, condicion:CondicionWhere, linea:int, columna:int):
        super().__init__(linea, columna)
        self.table_name = table_name
        self.condicion = condicion
    
    def ejecutar(self, env:Enviroment):
        print('------------------ CONTAR --------------------------')

        resultado = Retorno(tipo=TipoDato.ERROR, valor=None)
        

        print("> Nombre de tabla: ", self.table_name)

        # Solo acepta condiciones del tipo: WHERE campo = expresion
        print("> Valor de la condicion: ")
        print("     Campo: ", self.condicion.id)
        expresion = self.condicion.expresion.ejecutar(env)
        print("     Expresion: ", expresion.valor)

        print('-----------------------------------------------------')

        return resultado