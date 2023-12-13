from xmlrpc.client import Boolean
from interprete.extra.tipos import TipoDato
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion
from interprete.expresiones.Expresion import Expresion
from interprete.extra.retorno import Retorno
from interprete.extra.errores import *

class IfElse(Instruccion):

    def __init__(self, condicion:Expresion, bloque:Instruccion, bandera_else:Boolean, bloque_else:Instruccion, linea:int, columna:int):
        self.condicion = condicion
        self.bloque = bloque
        self.bandera_else = bandera_else
        self.bloque_else = bloque_else
        self.linea = linea
        self.columna = columna
        
    def ejecutar(self, env: Enviroment):

        print("ENTRO AL IF")
        
        val_condicion:Retorno = self.condicion.ejecutar(env)

        if val_condicion.tipo == TipoDato.ERROR:
            # Agregando a la tabla de errores
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error al evaluar la condicion IF.')
            TablaErrores.addError(err)
            return Retorno(tipo=TipoDato.ERROR, valor=None)
        
        if val_condicion.tipo != TipoDato.BOOL:
            # Agregando a la tabla de errores
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Se esperaba una expresión expresión de tipo booleano en la condición IF.')
            TablaErrores.addError(err)
            return Retorno(tipo=TipoDato.ERROR, valor=None)
        
        # Ejecutando bloque de instrucciones dentro de if
        if val_condicion.valor == True:
            return self.bloque.ejecutar(env)
        
        # Si hay un bloque else...
        if self.bandera_else == True:
            return self.bloque_else.ejecutar(env)

        return super().ejecutar(env)