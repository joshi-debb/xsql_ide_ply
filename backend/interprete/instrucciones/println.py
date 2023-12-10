from interprete.extra.tipos import TipoDato
from .instruccion import Instruccion
 
class Println(Instruccion):
    def __init__(self, argumento, linea, columna):
        super().__init__(linea, columna)
        self.argumento = argumento
    
    def ejecutar(self):
        exp = self.argumento.ejecutar()

        # Validar que no haya un error en la expresion
        if exp.tipo == TipoDato.ERROR:
            print("Semántico", f'Error en la expresión de la funcion print()', self.linea, self.columna)
            return self

        print(str(exp.valor))