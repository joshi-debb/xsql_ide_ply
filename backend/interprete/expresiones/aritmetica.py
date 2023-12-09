from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato
from interprete.extra.retorno import Retorno

class Aritmetica(Expresion):
    def __init__(self, op1:Expresion, operador:TipoAritmetica, op2:Expresion, linea, columna):
        super().__init__(linea, columna)
        self.op1 = op1
        self.op2 = op2
        self.operador = operador
    
    def ejecutar(self):
        op1:Retorno = self.op1.ejecutar()
        op2:Retorno = self.op2.ejecutar()
        resultado = Retorno(tipo=TipoDato.ERROR, valor=None)

        if self.operador == TipoAritmetica.SUMA:
            # bit
            if op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.BIT:
                resultado.tipo = TipoDato.BIT
                resultado.valor = op1.valor or op2.valor

            elif op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.INT:
                resultado.tipo = TipoDato.INT
                resultado.valor = op1.valor + op2.valor

            elif op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.DECIMAL:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor + op2.valor

            elif op1.tipo == TipoDato.BIT and (op2.tipo == TipoDato.NCHAR or op2.tipo == TipoDato.NVARCHAR):
                resultado.tipo = TipoDato.NVARCHAR
                resultado.valor = str(op1.valor) + op2.valor
            
            # int/decimal
            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.BIT:
                resultado.tipo = TipoDato.INT
                resultado.valor = op1.valor + op2.valor

            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.BIT:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor + op2.valor
            
            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.INT:
                resultado.tipo = TipoDato.INT
                resultado.valor = op1.valor + op2.valor

            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.DECIMAL:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor + op2.valor

            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.DECIMAL:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor + op2.valor
            
            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.INT:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor + op2.valor
            
            elif (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL) and (op2.tipo == TipoDato.NCHAR or op2.tipo == TipoDato.NVARCHAR):
                resultado.tipo = TipoDato.NVARCHAR
                resultado.valor = str(op1.valor) + op2.valor
            
            # nchar/nvarchar
            elif (op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR) and op2.tipo == TipoDato.BIT:
                resultado.tipo = TipoDato.NVARCHAR
                resultado.valor = op1.valor + str(op2.valor)
            
            elif (op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR) and (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL):
                resultado.tipo = TipoDato.NVARCHAR
                resultado.valor = op1.valor + str(op2.valor)
            
            elif (op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR) and (op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR):
                resultado.tipo = TipoDato.NVARCHAR
                resultado.valor = op1.valor + op2.valor
            
            else:
                print('Error en la SUMA')
            
        if self.operador == TipoAritmetica.RESTA:

            # bit
            if op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.INT:
                resultado.tipo = TipoDato.INT
                resultado.valor = op1.valor - op2.valor

            elif op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.DECIMAL:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor - op2.valor
            
            # int/decimal
            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.BIT:
                resultado.tipo = TipoDato.INT
                resultado.valor = op1.valor - op2.valor

            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.BIT:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor - op2.valor
            
            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.INT:
                resultado.tipo = TipoDato.INT
                resultado.valor = op1.valor - op2.valor

            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.DECIMAL:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor - op2.valor

            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.DECIMAL:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor - op2.valor
            
            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.INT:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor - op2.valor
            
            else:
                print('Error en la RESTA')
        if self.operador == TipoAritmetica.MULTIPLICACION:
            # bit
            if op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.BIT:
                resultado.tipo = TipoDato.BIT
                resultado.valor = op1.valor and op2.valor

            elif op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.INT:
                resultado.tipo = TipoDato.INT
                resultado.valor = op1.valor * op2.valor

            elif op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.DECIMAL:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor * op2.valor
            
            # int/decimal
            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.BIT:
                resultado.tipo = TipoDato.INT
                resultado.valor = op1.valor * op2.valor

            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.BIT:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor * op2.valor
            
            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.INT:
                resultado.tipo = TipoDato.INT
                resultado.valor = op1.valor * op2.valor

            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.DECIMAL:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor * op2.valor

            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.DECIMAL:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor * op2.valor
            
            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.INT:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor * op2.valor
            
            elif (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL) and (op2.tipo == TipoDato.NCHAR or op2.tipo == TipoDato.NVARCHAR):
                resultado.tipo = TipoDato.NVARCHAR
                resultado.valor = str(op1.valor) + op2.valor
            
            # date/datetime
            elif (op1.tipo == TipoDato.DATE or op1.tipo == TipoDato.DATETIME) and (op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR):
                resultado.tipo = TipoDato.NVARCHAR
                resultado.valor = op1.valor + op2.valor

            # nchar/nvarchar
            elif (op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR) and (op1.tipo == TipoDato.DATE or op1.tipo == TipoDato.DATETIME):
                resultado.tipo = TipoDato.NVARCHAR
                resultado.valor = op1.valor + op2.valor
            
            else:
                print('Error en la MULTIPLICACION')
        if self.operador == TipoAritmetica.DIVISION:
            # bit
            if op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.INT:
                resultado.tipo = TipoDato.INT
                resultado.valor = op1.valor / op2.valor

            elif op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.DECIMAL:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor / op2.valor

            # int/decimal
            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.BIT:
                resultado.tipo = TipoDato.INT
                resultado.valor = op1.valor / op2.valor

            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.BIT:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor / op2.valor
            
            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.INT:
                resultado.tipo = TipoDato.INT
                resultado.valor = op1.valor / op2.valor

            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.DECIMAL:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor / op2.valor

            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.DECIMAL:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor / op2.valor
            
            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.INT:
                resultado.tipo = TipoDato.DECIMAL
                resultado.valor = op1.valor / op2.valor
            
            # date/datetime
            elif (op1.tipo == TipoDato.DATE or op1.tipo == TipoDato.DATETIME) and (op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR):
                resultado.tipo = TipoDato.NVARCHAR
                resultado.valor = op1.valor + op2.valor

            # nchar/nvarchar
            elif (op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR) and (op1.tipo == TipoDato.DATE or op1.tipo == TipoDato.DATETIME):
                resultado.tipo = TipoDato.NVARCHAR
                resultado.valor = op1.valor + op2.valor
            
            else:
                print('Error en la DIVISION')

        elif self.operador == TipoAritmetica.UNARIO:
            if op1.tipo == TipoDato.INT:
                resultado.tipo = op1.tipo
                resultado.valor = (op1.valor) * -1

            elif op1.tipo == TipoDato.DECIMAL:
                resultado.tipo = op1.tipo
                resultado.valor = op1.valor * -1
            
            else:
                print('Error en la UNARIO')

        return resultado