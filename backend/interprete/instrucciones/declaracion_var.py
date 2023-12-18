from interprete.expresiones.tipoChars import TipoChars
from interprete.extra.enviroment import Enviroment
from interprete.extra.tipos import TipoSimbolo
from interprete.instrucciones.instruccion import Instruccion
from interprete.expresiones.Expresion import Expresion
from interprete.extra.tipos import TipoDato
from interprete.extra.retorno import Retorno
from interprete.extra.symbol import Symbol
from interprete.extra.errores import Error, TablaErrores

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
            elif isinstance(self.tipo, TipoChars):
                simbolo.valor = ' '
            elif self.tipo == TipoDato.BIT:
                simbolo.valor = False
        
        env.insertar_simbolo(self.id, simbolo)

        return self
