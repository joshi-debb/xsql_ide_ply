from interprete.extra.retorno import Retorno3d
from interprete.extra.ast import *
from interprete.extra.symbol import Symbol
from interprete.extra.enviroment import Enviroment
from interprete.extra.tipos import TipoDato
from .Expresion import Expresion
from interprete.extra.retorno import Retorno
from interprete.extra.tipos import TipoSimbolo
from interprete.extra.errores import Error, TablaErrores
from interprete.extra.generador import Generador

class Acceso(Expresion):
    def __init__(self, text_val:str, id:str, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.id = id
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self, env:Enviroment):
        resultado = Retorno(tipo=TipoDato.ERROR, valor=None)

        # Si no existe la variable en alguna tabla de simbolos
        if not env.existe_simbolo(self.id, TipoSimbolo.VARIABLE):
            # Agregando a la tabla de erorres
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'No existe una variable con el nombre {self.id}')
            TablaErrores.addError(err)
            return resultado
                
        simbolo:Symbol = env.getSimbolo(self.id, TipoSimbolo.VARIABLE)

        resultado = Retorno(tipo=simbolo.tipo, valor=simbolo.valor)
        
        return resultado
    
    def ejecutar3d(self,env: Enviroment, generador: Generador):
        codigo = ''

        if not env.existe_simbolo(self.id, TipoSimbolo.VARIABLE):
            # Agregando a la tabla de erorres
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'No existe una variable con el nombre {self.id}')
            TablaErrores.addError(err)
            return Retorno3d()
        
        simbolo:Symbol = env.getSimbolo(self.id, TipoSimbolo.VARIABLE)
        tmp1 = generador.obtenerTemporal()
        tmp2 = generador.obtenerTemporal()

        codigo = f'/* ACCESO A VARIABLE */\n'
        codigo += f'{tmp1} = SP + {simbolo.direccion};\n'
        codigo += f'{tmp2} = stack [(int) {tmp1}];\n'
        generador.agregarInstruccion(codigo)

        return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp2, tipo=simbolo.tipo, valor=simbolo.valor) 

        
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor=self.id, hijos=[])
        raiz.addHijo(hijo)
        
        
        