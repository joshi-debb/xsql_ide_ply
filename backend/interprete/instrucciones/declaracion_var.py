from interprete.extra.ast import *
from interprete.expresiones.tipoChars import TipoChars
from interprete.extra.enviroment import Enviroment
from interprete.extra.tipos import TipoSimbolo
from interprete.instrucciones.instruccion import Instruccion
from interprete.expresiones.Expresion import Expresion
from interprete.extra.tipos import TipoDato
from interprete.extra.retorno import Retorno
from interprete.extra.symbol import Symbol
from interprete.extra.errores import Error, TablaErrores
from interprete.extra.generador import Generador


class Declaracion(Instruccion):
    def __init__(self, text_val:str, id:str, tipo:TipoDato, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.id = id
        self.valor = None
        if isinstance(tipo, TipoChars): self.tipo = tipo.charTipo
        else:                           self.tipo = tipo
        
    def ejecutar(self, env:Enviroment):

        # Validar si la variable existe en la tabla de simbolos
        if env.existe_simbolo_ent_actual(self.id, TipoSimbolo.VARIABLE):
            # Agregando a la tabla de errores
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Ya existe una variable con el nombre {self.id}.')
            TablaErrores.addError(err)
            return self
        
        # Simbolo a insertar en tabla de simbolos
        print('A TB simbolos: ', self.id)
        simbolo = Symbol(TipoSimbolo.VARIABLE, self.tipo, self.id, self.valor, env.ambito, None)

        # Guardando con un valor por defecto
        if self.valor == None:
            if self.tipo == TipoDato.INT:
                simbolo.valor = 0
            elif self.tipo == TipoDato.DECIMAL:
                simbolo.valor = 0.0
            elif self.tipo == TipoDato.DATE:
                simbolo.valor = ' '
            elif self.tipo == TipoDato.DATETIME:
                simbolo.valor = ' '
            elif self.tipo == TipoDato.NCHAR or self.tipo == TipoDato.NVARCHAR:
                simbolo.valor = ' '
            elif self.tipo == TipoDato.BIT:
                simbolo.valor = False
        
        env.insertar_simbolo(self.id, simbolo)

        return self

    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='DECLARE', hijos=[])
        raiz.addHijo(hijo)
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor=self.id, hijos=[]))
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor=self.tipo.name, hijos=[]))
        
    def ejecutar3d(self, env:Enviroment, generador:Generador):

        # Validar si la variable existe en la tabla de simbolos
        if env.existe_simbolo_ent_actual(self.id, TipoSimbolo.VARIABLE):
            # Agregando a la tabla de errores
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Ya existe una variable con el nombre {self.id}.')
            TablaErrores.addError(err)
            return self

        tam_env = env.getTamanio()              # Tamaño del entorno
        tmp2 = generador.obtenerTemporal()
        tmp = generador.obtenerTemporal()       # Donde se indexar al stack

        valor = ''
        # Guardando con un valor por defecto
        if self.valor == None:
            if self.tipo == TipoDato.INT:
                valortmp = 0
            elif self.tipo == TipoDato.DECIMAL:
                valor = 0.0
            elif self.tipo == TipoDato.DATE:
                valor = '\"\"'
            elif self.tipo == TipoDato.DATETIME:
                valor = '\"\"'
            elif self.tipo == TipoDato.NCHAR or self.tipo == TipoDato.NVARCHAR:
                valor = '\"\"'
            elif self.tipo == TipoDato.BIT:
                valor = 0

        generador.agregarInstruccion('/* DECLARACION DE VARIABLE */')
        generador.agregarInstruccion(f'{tmp} = SP + {tam_env};')
        generador.agregarInstruccion(f'stack [(int) {tmp}] = {valor};')
        env.incrementarTamanio()

        simbolo = Symbol(TipoSimbolo.VARIABLE, self.tipo, self.id, self.valor, env.ambito, None, direccion=tam_env)
        env.insertar_simbolo(id=self.id, simbolo=simbolo)
        
        return self
