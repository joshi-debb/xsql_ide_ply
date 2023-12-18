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

        resultado = Retorno(tipo=TipoDato.INT, valor=0)
        
        print('CAMPOS: ')
        for campo in self.campos:
            print(campo)
        
        print('TABLAS: ')
        for tabla in self.tablas:
            print(tabla)
        
        print('CONDICION WHERE: ', self.condicion_where.text_val)
        
        # Cuando se obtenga la suma, modificar la variable resultado con el con el total
        # resultado.valor = total
        
        print('-----------------------------------------------------')

        return resultado