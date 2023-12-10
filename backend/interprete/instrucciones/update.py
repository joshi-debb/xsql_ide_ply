from interprete.instrucciones.instruccion import Instruccion
from interprete.instrucciones.asignacion_campo import Campo
from interprete.instrucciones.condicion_where import CondicionWhere

class Update(Instruccion):
    def __init__(self, table_name:str, tupla:Campo, condicion:CondicionWhere, linea:int, columna:int):
        super().__init__(linea, columna)
        self.table_name = table_name
        self.tupla = tupla                 
        self.condicion = condicion
    
    def ejecutar(self):
        print('------------------ UPDATE --------------------------')
        print("> Nombre de tabla: ", self.table_name)

        print("> Tupla: (valores a asignar) ")
        for tup in self.tupla:
            print("     Campo: ", tup.id)
            expresion = tup.expresion.ejecutar()
            print("     Expresion: ", expresion.valor)

        # Solo acepta condiciones del tipo: WHERE campo = expresion
        print("> Valor de la condicion: ")
        print("     Campo: ", self.condicion.id)
        expresion = self.condicion.expresion.ejecutar()
        print("     Expresion: ", expresion.valor)
        print('-----------------------------------------------------')
