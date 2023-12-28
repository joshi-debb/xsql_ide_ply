from interprete.extra.retorno import Retorno3d
from interprete.extra.ast import *
from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato
from interprete.extra.retorno import Retorno
from interprete.extra.enviroment import Enviroment
from interprete.extra.errores import Error, TablaErrores
from interprete.extra.generador import Generador

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
    
    def ejecutar3d(self, env:Enviroment, generador:Generador):
        op1:Retorno3d = self.op1.ejecutar3d(env, generador)
        op2:Retorno3d = self.op2.ejecutar3d(env, generador)

        codigo = ''
        tmp1 = generador.obtenerTemporal()

         # Que no haya error en los operandos
        if op1.tipo == TipoDato.ERROR or op2.tipo == TipoDato.ERROR:
            # Agregando a la tabla de errores
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error al realizar la operación aritmética.')
            TablaErrores.addError(err)
            return Retorno3d(tipo=TipoDato.ERROR)

        if self.operador == TipoAritmetica.SUMA:
            # bit
            if op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.BIT:
                codigo = f'{tmp1} = {op1.temporal} || {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.BIT)

            elif op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.INT:
                codigo = f'{tmp1} = {op1.temporal} + {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.INT)

            elif op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.DECIMAL:
                codigo = f'{tmp1} = {op1.temporal} + {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)

            elif op1.tipo == TipoDato.BIT and (op2.tipo == TipoDato.NCHAR or op2.tipo == TipoDato.NVARCHAR):
                #resultado.tipo = TipoDato.NVARCHAR
                #resultado.valor = str(op1.valor) + op2.valor
                pass
            
            # int/decimal
            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.BIT:
                codigo = f'{tmp1} = {op1.temporal} + {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.INT)

            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.BIT:
                codigo = f'{tmp1} = {op1.temporal} + {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)
            
            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.INT:
                codigo = f'{tmp1} = {op1.temporal} + {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.INT)

            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.DECIMAL:
                codigo = f'{tmp1} = {op1.temporal} + {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)

            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.DECIMAL:
                codigo = f'{tmp1} = {op1.temporal} + {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)
            
            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.INT:
                codigo = f'{tmp1} = {op1.temporal} + {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)
            
            elif (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL) and (op2.tipo == TipoDato.NCHAR or op2.tipo == TipoDato.NVARCHAR):
                # resultado.tipo = TipoDato.NVARCHAR
                # resultado.valor = str(op1.valor) + op2.valor
                pass
            
            # nchar/nvarchar
            elif (op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR) and op2.tipo == TipoDato.BIT:
                #resultado.tipo = TipoDato.NVARCHAR
                #resultado.valor = op1.valor + str(op2.valor)
                pass

            elif (op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR) and (op2.tipo == TipoDato.INT or op2.tipo == TipoDato.DECIMAL):
                # resultado.tipo = TipoDato.NVARCHAR
                #resultado.valor = op1.valor + str(op2.valor)
                pass
            
            elif (op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR) and (op2.tipo == TipoDato.NCHAR or op2.tipo == TipoDato.NVARCHAR):
                tmp2 = generador.obtenerTemporal()
                codigo += f'{tmp2} = HP;'
                codigo += self.concatenar(env, generador, op1)
                codigo += self.concatenar(env, generador, op2)
                codigo += f'heap[HP] = 0;\n'       # Caracter de fin de cadena
                codigo += f'HP = HP + 1;\n'
                print(codigo)
                generador.agregarInstruccion(codigo)

                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp2, tipo=TipoDato.NVARCHAR, valor='')
                
            else:
                # Agregando a la tabla de errores
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error al realizar lo suma. La suma de los tipos no es permitida.')
                TablaErrores.addError(err)
                return Retorno3d(tipo=TipoDato.ERROR)

        if self.operador == TipoAritmetica.RESTA:

            # bit
            if op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.INT:
                codigo = f'{tmp1} = {op1.temporal} - {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.INT)

            elif op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.DECIMAL:
                codigo = f'{tmp1} = {op1.temporal} - {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)
            
            # int/decimal
            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.BIT:
                codigo = f'{tmp1} = {op1.temporal} - {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.INT)

            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.BIT:
                codigo = f'{tmp1} = {op1.temporal} - {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)
            
            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.INT:
                codigo = f'{tmp1} = {op1.temporal} - {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.INT)

            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.DECIMAL:
                codigo = f'{tmp1} = {op1.temporal} - {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)

            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.DECIMAL:
                codigo = f'{tmp1} = {op1.temporal} - {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)
            
            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.INT:
                codigo = f'{tmp1} = {op1.temporal} - {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)
            
            else:
                # Agregando a la tabla de errores
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error al realizar lo resta. La resta de los tipos no es permitida.')
                TablaErrores.addError(err)
                return Retorno3d(tipo=TipoDato.ERROR)
        
        if self.operador == TipoAritmetica.MULTIPLICACION:
            # bit
            if op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.BIT:
                codigo = f'{tmp1} = {op1.temporal} && {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.BIT)

            elif op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.INT:
                codigo = f'{tmp1} = {op1.temporal} * {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.INT)

            elif op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.DECIMAL:
                codigo = f'{tmp1} = {op1.temporal} * {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)
            
            # int/decimal
            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.BIT:
                codigo = f'{tmp1} = {op1.temporal} * {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.INT)

            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.BIT:
                codigo = f'{tmp1} = {op1.temporal} * {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)
            
            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.INT:
                codigo = f'{tmp1} = {op1.temporal} * {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.INT)

            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.DECIMAL:
                codigo = f'{tmp1} = {op1.temporal} * {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)

            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.DECIMAL:
                codigo = f'{tmp1} = {op1.temporal} * {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)
            
            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.INT:
                codigo = f'{tmp1} = {op1.temporal} * {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)
            
            elif (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL) and (op2.tipo == TipoDato.NCHAR or op2.tipo == TipoDato.NVARCHAR):
                # resultado.tipo = TipoDato.NVARCHAR
                # resultado.valor = str(op1.valor) + op2.valor
                # codigo = f'{tmp1} = {op1.temporal} + {op2.temporal};'
                # generador.agregarInstruccion(codigo)
                # return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)
                pass
            
            # date/datetime
            elif (op1.tipo == TipoDato.DATE or op1.tipo == TipoDato.DATETIME) and (op2.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR):
                tmp2 = generador.obtenerTemporal()
                codigo += f'{tmp2} = HP;'
                codigo += self.concatenar(env, generador, op1)
                codigo += self.concatenar(env, generador, op2)
                codigo += f'heap[HP] = 0;\n'       # Caracter de fin de cadena
                codigo += f'HP = HP + 1;\n'
                print(codigo)
                generador.agregarInstruccion(codigo)

                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp2, tipo=TipoDato.NVARCHAR, valor='')

            # nchar/nvarchar
            elif (op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR) and (op2.tipo == TipoDato.DATE or op1.tipo == TipoDato.DATETIME):
                tmp2 = generador.obtenerTemporal()
                codigo += f'{tmp2} = HP;'
                codigo += self.concatenar(env, generador, op1)
                codigo += self.concatenar(env, generador, op2)
                codigo += f'heap[HP] = 0;\n'       # Caracter de fin de cadena
                codigo += f'HP = HP + 1;\n'
                print(codigo)
                generador.agregarInstruccion(codigo)

                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp2, tipo=TipoDato.NVARCHAR, valor='')
            
            else:
                # Agregando a la tabla de errores
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error al realizar lo multiplicaión. La multiplicación de los tipos no es permitida.')
                TablaErrores.addError(err)
                return Retorno3d(tipo=TipoDato.ERROR)
        
        if self.operador == TipoAritmetica.DIVISION:
            # bit
            if op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.INT:
                codigo = f'{tmp1} = {op1.temporal} / {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.INT)

            elif op1.tipo == TipoDato.BIT and op2.tipo == TipoDato.DECIMAL:
                codigo = f'{tmp1} = {op1.temporal} / {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)

            # int/decimal
            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.BIT:
                codigo = f'{tmp1} = {op1.temporal} / {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.INT)

            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.BIT:
                codigo = f'{tmp1} = {op1.temporal} / {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)
            
            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.INT:
                codigo = f'{tmp1} = {op1.temporal} / {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.INT)

            elif op1.tipo == TipoDato.INT and op2.tipo == TipoDato.DECIMAL:
                codigo = f'{tmp1} = {op1.temporal} / {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)

            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.DECIMAL:
                codigo = f'{tmp1} = {op1.temporal} / {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)
            
            elif op1.tipo == TipoDato.DECIMAL and op2.tipo == TipoDato.INT:
                codigo = f'{tmp1} = {op1.temporal} / {op2.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)
            
            # date/datetime
            elif (op1.tipo == TipoDato.DATE or op1.tipo == TipoDato.DATETIME) and (op2.tipo == TipoDato.NCHAR or op2.tipo == TipoDato.NVARCHAR):
                tmp2 = generador.obtenerTemporal()
                codigo += f'{tmp2} = HP;'
                codigo += self.concatenar(env, generador, op1)
                codigo += self.concatenar(env, generador, op2)
                codigo += f'heap[HP] = 0;\n'       # Caracter de fin de cadena
                codigo += f'HP = HP + 1;\n'
                print(codigo)
                generador.agregarInstruccion(codigo)

                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp2, tipo=TipoDato.NVARCHAR, valor='')

            # nchar/nvarchar
            elif (op1.tipo == TipoDato.NCHAR or op1.tipo == TipoDato.NVARCHAR) and (op2.tipo == TipoDato.DATE or op2.tipo == TipoDato.DATETIME):
                tmp2 = generador.obtenerTemporal()
                codigo += f'{tmp2} = HP;'
                codigo += self.concatenar(env, generador, op1)
                codigo += self.concatenar(env, generador, op2)
                codigo += f'heap[HP] = 0;\n'       # Caracter de fin de cadena
                codigo += f'HP = HP + 1;\n'
                print(codigo)
                generador.agregarInstruccion(codigo)

                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp2, tipo=TipoDato.NVARCHAR, valor='')
            
            else:
                # Agregando a la tabla de errores
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error al realizar lo division. La división de los tipos no es permitida.')
                TablaErrores.addError(err)
                return Retorno3d(tipo=TipoDato.ERROR)

        elif self.operador == TipoAritmetica.UNARIO:
            if op1.tipo == TipoDato.INT:
                codigo = f'{tmp1} = -{op1.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.INT)

            elif op1.tipo == TipoDato.DECIMAL:
                codigo = f'{tmp1} = -{op1.temporal};'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal=tmp1, tipo=TipoDato.DECIMAL)
            
            else:
                # Agregando a la tabla de errores
                err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'El operador unario debe ser de tipo INT o DECIMAL.')
                TablaErrores.addError(err)
                return Retorno3d(tipo=TipoDato.ERROR)


    
    def concatenar(self, env:Enviroment, generador:Generador, expresion:Retorno3d):
        codigo = ''
        etq_ciclo = generador.obtenerEtiqueta()
        etq_salida = generador.obtenerEtiqueta()
        caracter = generador.obtenerTemporal()

        codigo += f'{etq_ciclo}:\n'
        codigo += f'{caracter} = heap[(int) {expresion.temporal}];\n'
        codigo += f'if ({caracter} == 0) goto {etq_salida};\n'
        codigo += f'    heap[HP] = {caracter};\n'
        codigo += f'    HP = HP + 1;\n'
        codigo += f'    {expresion.temporal} = {expresion.temporal} + 1;\n'
        codigo += f'    goto {etq_ciclo};\n'
        codigo += f'{etq_salida}:\n'
        return codigo



    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        tipo = ''
        if self.operador == TipoAritmetica.SUMA: tipo = '+'
        elif self.operador == TipoAritmetica.RESTA: tipo = '-'
        elif self.operador == TipoAritmetica.MULTIPLICACION: tipo = '*'
        elif self.operador == TipoAritmetica.DIVISION: tipo = '/'
        elif self.operador == TipoAritmetica.UNARIO: tipo = '-'
        hijo = Nodo(id=id, valor=tipo, hijos=[])
        raiz.addHijo(hijo)
        self.op1.recorrerArbol(hijo)
        if self.operador == TipoAritmetica.UNARIO:
            return
        self.op2.recorrerArbol(hijo)
    
    
    