from interprete.extra.symbol import Symbol
from interprete.extra.enviroment import Enviroment
from interprete.extra.tipos import TipoDato
from .Expresion import Expresion
from interprete.extra.retorno import Retorno
from interprete.extra.tipos import TipoSimbolo
from interprete.extra.errores import Error, TablaErrores

class Acceso(Expresion):
    def __init__(self, id:str, linea:int, columna:int):
        self.id = id
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self, env:Enviroment):
        resultado = Retorno(tipo=TipoDato.ERROR, valor=None)

        # Si no existe la variable en alguna tabla de simbolos
        if env.existe_simbolo(self.id, TipoSimbolo.VARIABLE) == False:
            # Agregando a la tabla de erorres
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'No existe una variable con el nombre {self.id}')
            TablaErrores.addError(err)
            return resultado
        
        simbolo:Symbol = env.getSimbolo(self.id, TipoSimbolo.VARIABLE)

        resultado = Retorno(tipo=simbolo.tipo, valor=simbolo.valor)
        
        return resultado
        