from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato
from interprete.extra.retorno import Retorno
from interprete.instrucciones.condicion_where import CondicionWhere
from interprete.extra.enviroment import Enviroment

class Contar(Expresion):
    
    def __init__(self, text_val:str, campos: str, tablas:str, condicion_where:CondicionWhere, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.campos = campos
        self.tablas = tablas
        self.condicion_where = condicion_where
    
    def ejecutar(self, env:Enviroment):
        print('CONTAR: text_val: ', self.text_val)
        print('------------------ CONTAR --------------------------')

        resultado = Retorno(tipo=TipoDato.ERROR, valor=None)
        

        print("> Nombre de tabla: ", self.tablas)

        # Solo acepta condiciones del tipo: WHERE campo = expresion
        print("> Valor de la condicion_where: ")
        print("     Campo: ", self.condicion_where.id)
        expresion = self.condicion_where.expresion.ejecutar(env)
        print("     Expresion: ", expresion.valor)

        print('-----------------------------------------------------')

        return resultado