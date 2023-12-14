from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato, TipoLogico
from interprete.extra.retorno import Retorno
from interprete.extra.enviroment import Enviroment
from interprete.extra.errores import Error, TablaErrores

class Logica(Expresion):
    def __init__(self, text_val:str, op1:Expresion, operador:TipoLogico, op2:Expresion, linea, columna):
        super().__init__(text_val, linea, columna)
        self.op1 = op1
        self.op2 = op2
        self.operador = operador
    
    def ejecutar(self, env:Enviroment):
        op1:Retorno = self.op1.ejecutar(env)
        op2:Retorno = self.op2.ejecutar(env)
        resultado = Retorno(tipo=TipoDato.ERROR, valor=None)

        # Que no haya error en los operandos
        if op1.tipo == TipoDato.ERROR or op2.tipo == TipoDato.ERROR:
            # Agregando a la tabla de errores
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error al realizar la operacion logica.')
            TablaErrores.addError(err)
            return resultado
        
        if op1.tipo != TipoDato.BOOL or op2.tipo != TipoDato.BOOL:
            # Agregando a la tabla de errores
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Ambas expresiones deben ser de tipo logicas (true o false).')
            TablaErrores.addError(err)
            return resultado
        
        if self.operador == TipoLogico.AND:
            resultado.tipo = TipoDato.BOOL
            resultado.valor = op1.valor and op2.valor

        elif self.operador == TipoLogico.OR:
            resultado.tipo = TipoDato.BOOL
            resultado.valor = op1.valor or op2.valor

        elif self.operador == TipoLogico.NOT:
            resultado.tipo = TipoDato.BOOL
            resultado.valor = not op1.valor
        
        return resultado