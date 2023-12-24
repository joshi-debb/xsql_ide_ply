from interprete.extra.ast import *
from interprete.expresiones.tipoChars import TipoChars
from .Expresion import Expresion
from interprete.extra.tipos import *
from interprete.extra.retorno import Retorno
from interprete.extra.enviroment import Enviroment
from interprete.extra.errores import *
from interprete.extra.symbol import Symbol
from interprete.extra.generador import Generador


class Cas(Expresion):
    
    def __init__(self, text_val:str, id_var:Expresion, tipo:TipoDato, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.id_var = id_var
        if isinstance(tipo, TipoChars): self.tipo = tipo.charTipo
        else:                           self.tipo = tipo
    
    def ejecutar(self, env: Enviroment):
        # Si no existe la variable en alguna tabla de simbolos
        if not env.existe_simbolo(self.id_var, TipoSimbolo.VARIABLE):
            # Agregando a la tabla de erorres
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error en el casteo. No existe una variable con el nombre {self.id_var}')
            TablaErrores.addError(err)
            return Retorno(tipo=TipoDato.ERROR, valor=None)
        
        # Trayendo la variable
        simbolo:Symbol = env.getSimbolo(self.id_var, TipoSimbolo.VARIABLE)
        if simbolo.tipo == TipoDato.BIT:
            if self.tipo == TipoDato.INT:
                simbolo.tipo = TipoDato.INT
                if simbolo.valor == None:
                    simbolo.valor = 0    
                else:
                    simbolo.valor = int(simbolo.valor)
            elif self.tipo == TipoDato.NCHAR or self.tipo == TipoDato.NVARCHAR:
                simbolo.tipo = self.tipo   
                if simbolo.valor == True:    simbolo.valor = '1'
                elif simbolo.valor == False: simbolo.valor = '0'
                elif simbolo.valor == None:  simbolo.valor = '0'
            else:
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error en el casteo. No se puede realizar un casteo de un {simbolo.tipo.name} a un {self.tipo.name}')
                TablaErrores.addError(err)
                return Retorno(tipo=TipoDato.ERROR, valor=None)

        elif simbolo.tipo == TipoDato.NCHAR or simbolo.tipo == TipoDato.NVARCHAR:
            if self.tipo == TipoDato.INT:
                suma_ascii = 0
                for char in simbolo.valor:
                    suma_ascii += ord(char)
                simbolo.tipo = TipoDato.INT
                simbolo.valor = suma_ascii
            else:
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error en el casteo. No se puede realizar un casteo de un {simbolo.tipo.name} a un {self.tipo.name}')
                TablaErrores.addError(err)
                return Retorno(tipo=TipoDato.ERROR, valor=None)
        
        elif simbolo.tipo == TipoDato.INT:
            if self.tipo == TipoDato.NVARCHAR or self.tipo == TipoDato.NCHAR:
                simbolo.tipo = self.tipo
                if simbolo.valor > 255 or simbolo.valor < 0: simbolo.valor = chr(0) # Convertir el valor null a cadena
                else:                   simbolo.valor = chr(simbolo.valor)
            elif self.tipo == TipoDato.DECIMAL:
                simbolo.tipo = TipoDato.DECIMAL
                simbolo.valor = float(simbolo.valor)
            else:
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error en el casteo. No se puede realizar un casteo de un {simbolo.tipo.name} a un {self.tipo.name}')
                TablaErrores.addError(err)
                return Retorno(tipo=TipoDato.ERROR, valor=None)
        elif simbolo.tipo == TipoDato.DECIMAL:
            if self.tipo == TipoDato.INT:
                simbolo.tipo = TipoDato.INT
                simbolo.valor = int(simbolo.valor)
        else:
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error en el casteo. No se puede realizar un casteo de un {simbolo.tipo.name} a un {self.tipo.name}')
            TablaErrores.addError(err)
            return Retorno(tipo=TipoDato.ERROR, valor=None)

        return Retorno(tipo=simbolo.tipo, valor=simbolo.valor)
    
    
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='CAS', hijos=[])
        raiz.addHijo(hijo)
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor=self.id_var, hijos=[]))
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor=self.tipo.name, hijos=[]))
        
    def generar3d(self,env: Enviroment, generador: Generador):
        pass