from .Expresion import Expresion
from interprete.extra.tipos import TipoDato, TipoRelacional
from interprete.extra.retorno import Retorno

class Relacional(Expresion):
    def __init__(self, op1:Expresion, operador:TipoRelacional, op2:Expresion, linea, columna):
        super().__init__(linea, columna)
        self.op1 = op1
        self.op2 = op2
        self.operador = operador
    
    def ejecutar(self):
        op1:Retorno = self.op1.ejecutar()
        op2:Retorno = self.op2.ejecutar()
        resultado = Retorno(tipo=TipoDato.ERROR, valor=None)

        # if op1.tipo == TipoDato.UNDEFINED or op2.tipo == TipoDato.UNDEFINED:
        #     ctr.agregarError("Semántico", "Un operando no tiene un tipo de dato definido", ent.ambito, self.linea, self.columna)
        #     return resultado
        
        if op1.tipo == TipoDato.ERROR or op2.tipo == TipoDato.ERROR:
            print("Semántico", "Error al operar la expresion relacional.", self.linea, self.columna)
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
        
        elif self.operador == TipoRelacional.IGUALDAD:
            if (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL) and (op2.tipo == TipoDato.INT or op2.tipo == TipoDato.DECIMAL):
                resultado.tipo = TipoDato.BOOL
                resultado.valor = (op1.valor == op2.valor)
                
        elif self.operador == TipoRelacional.DESIGUALDAD:
            if (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL) and (op2.tipo == TipoDato.INT or op2.tipo == TipoDato.DECIMAL):
                resultado.tipo = TipoDato.BOOL
                resultado.valor = (op1.valor != op2.valor)

        return resultado