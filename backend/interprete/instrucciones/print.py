from interprete.extra.tipos import TipoDato
from .instruccion import Instruccion
from interprete.extra.enviroment import Enviroment

class Print(Instruccion):
    def __init__(self, text_val:str, argumento, linea, columna):
        super().__init__(text_val, linea, columna)
        self.text_val = text_val
        self.argumento = argumento
    
    def ejecutar(self, env:Enviroment):
        print("La expresion es: ", self.text_val)
        exp = self.argumento.ejecutar(env)

        # Validar que no haya un error en la expresion
        if exp.tipo == TipoDato.ERROR:
            print("Semántico", f'Error en la expresión de la funcion print()', self.linea, self.columna)
            return self

        print(str(exp.valor))