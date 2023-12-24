from interprete.extra.ast import *
from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato
from interprete.extra.retorno import Retorno
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion
from interprete.extra.errores import *
from interprete.extra.generador import Generador

class OpTernario(Expresion):

    def __init__(self, text_val:str, condicion:Expresion, instruccionTrue:Instruccion, instruccionFalse:Instruccion, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.condicion = condicion
        self.instruccionTrue = instruccionTrue
        self.instruccionFalse = instruccionFalse
    
    def ejecutar(self, env: Enviroment):
        val_condicion:Retorno = self.condicion.ejecutar(env)

        # Si hay un error en la expresion...
        if val_condicion.tipo == TipoDato.ERROR:
            # Agregando a la tabla de errores
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error en la condición del operador ternario.')
            TablaErrores.addError(err)
            return Retorno(tipo=TipoDato.ERROR, valor=None)
        
        # La condicion debe de retornar un tipo booleano
        if val_condicion.tipo != TipoDato.BOOL:
            # Agregando a la tabla de errores
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Se esperaba una expresion booleana pero se obtuvo una de tipo {val_condicion.tipo.name}')
            TablaErrores.addError(err)
            return Retorno(tipo=TipoDato.ERROR, valor=None)
        
        if val_condicion.valor == True:
            return self.instruccionTrue.ejecutar(env)
        else:
            return self.instruccionFalse.ejecutar(env)

    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='IF', hijos=[])
        raiz.addHijo(hijo)
        self.condicion.recorrerArbol(hijo)
        self.instruccionTrue.recorrerArbol(hijo)
        self.instruccionFalse.recorrerArbol(hijo)
    
    def ejecutar3d(self, env:Enviroment, generador:Generador):
        pass