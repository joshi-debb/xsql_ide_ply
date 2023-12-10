from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato, TipoLogico
from interprete.extra.retorno import Retorno

class Logica(Expresion):
    def __init__(self, op1:Expresion, operador:TipoLogico, op2:Expresion, linea, columna):
        super().__init__(linea, columna)
        self.op1 = op1
        self.op2 = op2
        self.operador = operador
    
    def ejecutar(self):
        op1:Retorno = self.op1.ejecutar()
        op2:Retorno = self.op2.ejecutar()
        resultado = Retorno(tipo=TipoDato.ERROR, valor=None)

        # if op1.tipo == TipoLogico.UNDEFINED or op2.tipo == TipoLogico.UNDEFINED:
        #     ctr.agregarError("Semántico", "Un operando no tiene un tipo de dato definido", ent.ambito, self.linea, self.columna)
        #     return resultado
        
        if op1.tipo == TipoDato.ERROR or op2.tipo == TipoDato.ERROR:
            print("Semántico", "Error al operar la expresion lógica.", self.linea, self.columna)
            return resultado
        
        if op1.tipo != TipoDato.BOOL or op2.tipo != TipoDato.BOOL:
            print("Semántico", "Ambas expresiones deben ser de tipo bool.", self.linea, self.columna)
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