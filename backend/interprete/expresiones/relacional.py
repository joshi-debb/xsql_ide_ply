from .Expresion import Expresion
from interprete.extra.tipos import TipoDato, TipoRelacional
from interprete.extra.retorno import Retorno
from interprete.extra.enviroment import Enviroment
from interprete.extra.errores import Error, TablaErrores

class Relacional(Expresion):
    def __init__(self, text_val:str, op1:Expresion, operador:TipoRelacional, op2:Expresion, linea, columna):
        super().__init__(text_val, linea, columna)
        self.op1 = op1
        self.op2 = op2
        self.operador = operador
    
    def ejecutar(self, env:Enviroment):
        op1:Retorno = self.op1.ejecutar(env)
        op2:Retorno = self.op2.ejecutar(env)
        resultado = Retorno(tipo=TipoDato.ERROR, valor=None)

        # print('type: ', type(op1))
        # print('op1: ', op1.valor)
        # print(op1.tipo)
        # print('type: ', type(op2))
        # print('op2: ', op2.valor)
        # print(op2.tipo)

        # Que no haya error en los operandos
        if op1.tipo == TipoDato.ERROR or op2.tipo == TipoDato.ERROR:
            print("Error al realizar la operacion Relacional. En la linea " + str(self.linea))
            # Agregando a la tabla de errores
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error al realizar operacion relacional.')
            TablaErrores.addError(err)
            return resultado
        
        if self.operador == TipoRelacional.MAYOR:
            if (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL) and (op2.tipo == TipoDato.INT or op2.tipo == TipoDato.DECIMAL):
                resultado.tipo = TipoDato.BOOL
                resultado.valor = (op1.valor > op2.valor)
        
        elif self.operador == TipoRelacional.MENOR:
            if (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL) and (op2.tipo == TipoDato.INT or op2.tipo == TipoDato.DECIMAL):
                resultado.tipo = TipoDato.BOOL
                resultado.valor = (op1.valor < op2.valor)
        
        elif self.operador == TipoRelacional.MAYOR_IGUAL:
            if (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL) and (op2.tipo == TipoDato.INT or op2.tipo == TipoDato.DECIMAL):
                resultado.tipo = TipoDato.BOOL
                resultado.valor = (op1.valor >= op2.valor)
        
        elif self.operador == TipoRelacional.MENOR_IGUAL:
            if (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL) and (op2.tipo == TipoDato.INT or op2.tipo == TipoDato.DECIMAL):
                resultado.tipo = TipoDato.BOOL
                resultado.valor = (op1.valor <= op2.valor)
        
        elif self.operador == TipoRelacional.IGUALDAD or self.operador == TipoRelacional.IGUAL:
            if (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL) and (op2.tipo == TipoDato.INT or op2.tipo == TipoDato.DECIMAL):
                resultado.tipo = TipoDato.BOOL
                resultado.valor = (op1.valor == op2.valor)
                
        elif self.operador == TipoRelacional.DESIGUALDAD:
            if (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL) and (op2.tipo == TipoDato.INT or op2.tipo == TipoDato.DECIMAL):
                resultado.tipo = TipoDato.BOOL
                resultado.valor = (op1.valor != op2.valor)

        return resultado