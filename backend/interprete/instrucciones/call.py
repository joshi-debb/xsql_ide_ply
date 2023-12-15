
from interprete.instrucciones.instruccion import Instruccion
from interprete.extra.enviroment import Enviroment

class Call(Instruccion):
    def __init__(self, text_val, nombre_proc, line, column):
        Instruccion.__init__(self,None,line,column)
        self.nombre_proc = nombre_proc

    def ejecutar(self, env:Enviroment):
        ##leer xml y ejecutar el procedure
        ##texto = procedimiento_almacenado
        
        ##proc = parser.parse(texto)
        ##proc.ejecutar_proc()
        pass