from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato
from interprete.extra.retorno import Retorno
from interprete.extra.enviroment import Enviroment
from interprete.extra.errores import Error, TablaErrores

class Aritmetica(Expresion):
    def __init__(self, text_val:str, op1:Expresion, operador:TipoAritmetica, op2:Expresion, linea, columna):
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
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error al realizar la operación aritmética.')
            TablaErrores.addError(err)
            return resultado

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
            
            elif (op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR) and (op2.tipo == TipoDato.INT or op2.tipo == TipoDato.DECIMAL):
                resultado.tipo = TipoDato.NVARCHAR
                resultado.valor = op1.valor + str(op2.valor)
            
            elif (op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR) and (op2.tipo == TipoDato.NCHAR or op2.tipo == TipoDato.NVARCHAR):
                resultado.tipo = TipoDato.NVARCHAR
                resultado.valor = op1.valor + op2.valor
            
            else:
                # Agregando a la tabla de errores
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error al realizar lo suma. La suma de los tipos no es permitida.')
                TablaErrores.addError(err)

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
                # Agregando a la tabla de errores
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error al realizar lo resta. La resta de los tipos no es permitida.')
                TablaErrores.addError(err)

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
            elif (op1.tipo == TipoDato.DATE or op1.tipo == TipoDato.DATETIME) and (op2.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR):
                resultado.tipo = TipoDato.NVARCHAR
                resultado.valor = op1.valor + op2.valor

            # nchar/nvarchar
            elif (op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR) and (op2.tipo == TipoDato.DATE or op1.tipo == TipoDato.DATETIME):
                resultado.tipo = TipoDato.NVARCHAR
                resultado.valor = op1.valor + op2.valor
            
            else:
                # Agregando a la tabla de errores
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error al realizar lo multiplicaión. La multiplicación de los tipos no es permitida.')
                TablaErrores.addError(err)
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
            elif (op1.tipo == TipoDato.DATE or op1.tipo == TipoDato.DATETIME) and (op2.tipo == TipoDato.NCHAR or op2.tipo == TipoDato.NVARCHAR):
                resultado.tipo = TipoDato.NVARCHAR
                resultado.valor = op1.valor + op2.valor

            # nchar/nvarchar
            elif (op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR) and (op2.tipo == TipoDato.DATE or op2.tipo == TipoDato.DATETIME):
                resultado.tipo = TipoDato.NVARCHAR
                resultado.valor = op1.valor + op2.valor
            
            else:
                # Agregando a la tabla de errores
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error al realizar lo division. La división de los tipos no es permitida.')
                TablaErrores.addError(err)

        elif self.operador == TipoAritmetica.UNARIO:
            if op1.tipo == TipoDato.INT:
                resultado.tipo = op1.tipo
                resultado.valor = (op1.valor) * -1

            elif op1.tipo == TipoDato.DECIMAL:
                resultado.tipo = op1.tipo
                resultado.valor = op1.valor * -1
            
            else:
                # Agregando a la tabla de errores
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'El operador unario debe ser de tipo INT o DECIMAL.')
                TablaErrores.addError(err)

        return resultado