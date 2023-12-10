from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato
from interprete.extra.retorno import Retorno
from interprete.instrucciones.condicion_where import CondicionWhere

class Suma(Expresion):
    
    def __init__(self, column:Expresion, table_name:str, condicion:CondicionWhere, linea:int, columna:int):
        super().__init__(linea, columna)
        self.column = column
        self.table_name = table_name
        self.condicion = condicion
    
    def ejecutar(self):
        print('------------------ SUMA --------------------------')
        
        # Se acepta el nombre o numero de columna
        if isinstance(self.column, str):
            print("> Nombre/Numero de columna: ", self.column)
        else:
            column:Retorno = self.column.ejecutar()
            print("> Nombre/Numero de columna: ", column.valor)

        resultado = Retorno(tipo=TipoDato.ERROR, valor=None)
        

        print("> Nombre de tabla: ", self.table_name)

        # Solo acepta condiciones del tipo: WHERE campo = expresion
        print("> Valor de la condicion: ")
        print("     Campo: ", self.condicion.id)
        expresion = self.condicion.expresion.ejecutar()
        print("     Expresion: ", expresion.valor)

        
        print('-----------------------------------------------------')

        return resultado