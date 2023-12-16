
from interprete.instrucciones.instruccion import Instruccion
from interprete.extra.enviroment import Enviroment

# Esta clase buscará el procedimiento en el XML
class Exec(Instruccion):
    def __init__(self, text_val, nombre_proc, linea, columna):
        super().__init__(text_val, linea, columna)
        self.nombre_proc = nombre_proc

    def ejecutar(self, env:Enviroment):
        print('EXEC: ')
        print(self.text_val)
        # Buscar el nombre de la funcion 'self.nombre_proc' en el XML 
        # Ejecutar el procedure
        # texto = procedimiento_almacenado
        
        ##proc = parser.parse(texto)
        ##proc.ejecutar_proc()
        pass