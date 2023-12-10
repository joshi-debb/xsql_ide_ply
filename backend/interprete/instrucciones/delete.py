from interprete.instrucciones.instruccion import Instruccion
from interprete.instrucciones.asignacion_campo import Campo
from interprete.instrucciones.condicion_where import CondicionWhere

class Delete(Instruccion):
    def __init__(self, table_name:str, condicion:CondicionWhere, linea:int, columna:int):
        super().__init__(linea, columna)
        self.table_name = table_name
        self.condicion = condicion
    
    def ejecutar(self):
        print('------------------ DELETE --------------------------')
        print("> Nombre de tabla: ", self.table_name)

        # Solo acepta condiciones del tipo: WHERE campo = expresion
        print("> Valor de la condicion: ")
        print("     Campo: ", self.condicion.id)
        expresion = self.condicion.expresion.ejecutar()
        print("     Expresion: ", expresion.valor)
        print('-----------------------------------------------------')
