from interprete.extra.ast import *
from interprete.extra.tipos import TipoDato
from .instruccion import Instruccion
from interprete.extra.enviroment import Enviroment

class Print(Instruccion):
    def __init__(self, text_val:str, argumento, linea, columna):
        super().__init__(text_val, linea, columna)
        self.text_val = text_val
        self.argumento = argumento
    
    def ejecutar(self, env:Enviroment):
        exp = self.argumento.ejecutar(env)

        # Validar que no haya un error en la expresion
        if exp.tipo == TipoDato.ERROR:
            print("Semántico", f'Error en la expresión de la funcion print()', self.linea, self.columna)
            return self

        print(str(exp.valor))
    
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='SELECT', hijos=[])
        raiz.addHijo(hijo)                                    
        self.argumento.recorrerArbol(hijo)