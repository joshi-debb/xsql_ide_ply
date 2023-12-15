from interprete.expresiones.acceso import Acceso
from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato
from interprete.extra.retorno import Retorno
from interprete.instrucciones.condicion_where import CondicionWhere
from interprete.extra.enviroment import Enviroment

class Suma(Expresion):
    
    def __init__(self, text_val:str, column:Expresion, table_name:str, condicion:CondicionWhere, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.column = column
        self.table_name = table_name
        self.condicion = condicion
    
    def ejecutar(self, env:Enviroment):
        print('SUMA: text_val: ', self.text_val)
        print('------------------ SUMA --------------------------')
        
        # Se acepta el nombre o numero de columna
        if isinstance(self.column, Acceso):
            print("> Nombre/Numero de columna: ", self.column.id)
        else:
            column:Retorno = self.column.ejecutar(env)
            print("> Nombre/Numero de columna: ", column.valor)

        resultado = Retorno(tipo=TipoDato.ERROR, valor=None)
        

        print("> Nombre de tabla: ", self.table_name)

        # Solo acepta condiciones del tipo: WHERE campo = expresion
        print("> Valor de la condicion: ")
        print("     Campo: ", self.condicion.id)
        expresion = self.condicion.expresion.ejecutar(env)
        print("     Expresion: ", expresion.valor)

        
        print('-----------------------------------------------------')

        return resultado