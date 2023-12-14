from msilib.schema import Error
from operator import truediv
from interprete.extra.retorno import Retorno
from interprete.extra.tipos import TipoDato, TipoSimbolo
from interprete.instrucciones.instruccion import Instruccion
from interprete.expresiones.Expresion import Expresion
from interprete.extra.enviroment import Enviroment
from interprete.extra.errores import Error, TablaErrores

class AsignacionVar(Instruccion):
    def __init__(self, text_val:str, id:str, expresion:Expresion, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.id = id
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self, env:Enviroment):
        
        # Validar que la variable exista en la tabla de simbolos
        if not env.existe_simbolo(self.id, TipoSimbolo.VARIABLE):
            # Agregando a la tabla de erorres
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error de asignacion de variable. No existe una variable con el nombre {self.id}')
            TablaErrores.addError(err)
            return self

        simbolo = env.getSimbolo(self.id, TipoSimbolo.VARIABLE)
        exp = self.expresion.ejecutar(env)

        if exp.tipo == TipoDato.ERROR:
            # Agregando error a la tabla de erorres
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion='Error en la asignacion de variable')
            TablaErrores.addError(err)
            return self

        # El tipo de la variable debe coincidir con el tipo de de dato asignandose
        if exp.tipo != simbolo.tipo and (simbolo.tipo != TipoDato.BIT):
            # Agregando a la tabla de erorres
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion='La expresion debe ser del mismo tipo que la variable')
            TablaErrores.addError(err)
            return self
        
        if simbolo.tipo == TipoDato.BIT:
            if exp.tipo != TipoDato.INT:
                # Agregando a la tabla de erorres
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion='Error Semantico. El valor a asignar debe ser tipo bit (1 o 0)')
                TablaErrores.addError(err)
                return self
            if exp.valor == 1:
                simbolo.valor = True
            elif exp.valor == 0:
                simbolo.valor = False
            else:
                # Agregando a la tabla de erorres
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion='Error Semantico. El valor a asignar debe ser tipo bit (1 o 0)')
                TablaErrores.addError(err)
                return self
            return self
        else:
            # Modificando el valor de la variable
            simbolo.valor = exp.valor

        return self