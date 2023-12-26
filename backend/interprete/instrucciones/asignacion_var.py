from interprete.extra.retorno import Retorno3d
from interprete.extra.ast import *
from operator import truediv
from interprete.extra.retorno import Retorno
from interprete.extra.tipos import TipoDato, TipoSimbolo
from interprete.instrucciones.instruccion import Instruccion
from interprete.expresiones.Expresion import Expresion
from interprete.extra.enviroment import Enviroment
from interprete.extra.errores import Error, TablaErrores
from interprete.expresiones.tipoChars import TipoChars
from interprete.extra.generador import Generador


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
        
        if simbolo.tipo == TipoDato.BIT:
            if exp.tipo != TipoDato.INT and exp.tipo != TipoDato.NULL:
                # Agregando a la tabla de erorres
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion='Error Semantico. El valor a asignar debe ser tipo bit (1 o 0)')
                TablaErrores.addError(err)
                return self
            if exp.valor == 1:
                simbolo.valor = True
            elif exp.valor == 0:
                simbolo.valor = False
            elif exp.valor == 'null':
                simbolo.valor = None
            else:
                # Agregando a la tabla de erorres
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion='Error Semantico. El valor a asignar debe ser tipo bit (1, 0 o null)')
                TablaErrores.addError(err)
                return self
            return self
        elif simbolo.tipo == TipoDato.NCHAR or simbolo.tipo == TipoDato.NVARCHAR:
            if exp.tipo == TipoDato.NCHAR or exp.tipo == TipoDato.NVARCHAR:
                simbolo.tipo = simbolo.tipo
                simbolo.valor = exp.valor
            else:
                # Agregando a la tabla de erorres
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error Semantico. El valor a asignar debe ser tipo {simbolo.tipo.name}')
                TablaErrores.addError(err)
                return self
            return self
        
        elif simbolo.tipo == TipoDato.DATETIME:
            if exp.tipo == TipoDato.NCHAR or exp.tipo == TipoDato.NVARCHAR or exp.tipo == TipoDato.DATETIME:
                simbolo.valor = exp.valor
            else: 
                # Agregando a la tabla de erorres
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error Semantico. El valor a asignar debe ser tipo {simbolo.tipo.name}')
                TablaErrores.addError(err)
            return self

        elif simbolo.tipo == TipoDato.DATE:
            if exp.tipo == TipoDato.NCHAR or exp.tipo == TipoDato.NVARCHAR or exp.tipo == TipoDato.DATE:
                simbolo.valor = exp.valor
            else: 
                # Agregando a la tabla de erorres
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error Semantico. El valor a asignar debe ser tipo {simbolo.tipo.name}')
                TablaErrores.addError(err)
            return self

        # El tipo de la variable debe coincidir con el tipo de de dato asignandose
        if exp.tipo != simbolo.tipo:
            # Agregando a la tabla de erorres
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error Semantico. El valor a asignar debe ser tipo {simbolo.tipo.name}')
            return self

        else:
            # Modificando el valor de la variable
            simbolo.valor = exp.valor

        return self

    def ejecutar3d(self, env: Enviroment, generador: Generador):
        # Validar que la variable exista en la tabla de simbolos
        if not env.existe_simbolo(self.id, TipoSimbolo.VARIABLE):
            # Agregando a la tabla de erorres
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error de asignacion de variable. No existe una variable con el nombre {self.id}')
            TablaErrores.addError(err)
            return self
        
        simbolo = env.getSimbolo(self.id, TipoSimbolo.VARIABLE)
        exp:Retorno3d = self.expresion.ejecutar3d(env, generador)

        generador.agregarInstruccion('/* ASIGNACION DE VARIABLE */')
        if simbolo.tipo == exp.tipo:
            tmp1 = generador.obtenerTemporal()
            generador.agregarInstruccion(f'{tmp1} = SP + {simbolo.direccion};')
            generador.agregarInstruccion(f'stack[(int) {tmp1}] = {exp.temporal};')
            simbolo.valor = exp.valor

        return self


    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='SET', hijos=[])
        raiz.addHijo(hijo)
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor=self.id, hijos=[]))
        self.expresion.recorrerArbol(hijo)
        