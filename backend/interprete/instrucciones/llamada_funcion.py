
from interprete.instrucciones.instruccion import Instruccion
from interprete.extra.enviroment import Enviroment

# Esta clase buscará la funcion en el XML
class LlamadaFnc(Instruccion):
    def __init__(self, text_val, nombre_fnc, linea, columna):
        super().__init__(text_val, linea, columna)
        self.nombre_fnc = nombre_fnc

    def ejecutar(self, env:Enviroment):
        print('Llamada funcion: ')
        print(self.text_val)
        # Buscar el nombre de la funcion 'self.nombre_proc' en el XML 
        ##leer xml y ejecutar el procedure
        ##texto = procedimiento_almacenado
        
        ##proc = parser.parse(texto)
        ##proc.ejecutar_proc()
        pass