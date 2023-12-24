from interprete.extra.ast import *
from interprete.extra.tipos import TipoDato
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion
from interprete.expresiones.Expresion import Expresion
from interprete.extra.retorno import Retorno
from interprete.extra.errores import *
from interprete.instrucciones.bloque import Bloque
from interprete.extra.generador import Generador

class When(Instruccion):

    def __init__(self, text_val:str, condicion:Expresion, bloque:Bloque, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.condicion = condicion
        self.bloque = bloque
    
    def ejecutar(self, env: Enviroment):
        return self.bloque.ejecutar(env)
    
    def evaluarCondicion(self, env:Enviroment):
        val_condicion:Retorno = self.condicion.ejecutar(env)

        if val_condicion.tipo == TipoDato.ERROR:
            # Agregando a la tabla de errores
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error al evaluar la condicion WHEN.')
            TablaErrores.addError(err)
            return Retorno(tipo=TipoDato.ERROR, valor=None)
        
        if val_condicion.tipo != TipoDato.BOOL:
            # Agregando a la tabla de errores
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Se esperaba una expresión expresión de tipo booleano en la condición WHEN.')
            TablaErrores.addError(err)
            return Retorno(tipo=TipoDato.ERROR, valor=None)
        
        if val_condicion.valor == True:
            return True
        return False
    
    
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='WHEN', hijos=[])
        raiz.addHijo(hijo)
        self.condicion.recorrerArbol(hijo)
        self.bloque.recorrerArbol(hijo)
    
    def ejecutar3d(self, env:Enviroment, generador:Generador):
        pass
    