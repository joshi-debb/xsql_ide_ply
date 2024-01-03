from interprete.extra.retorno import Retorno3d
from interprete.extra.ast import *
from .Expresion import Expresion
from interprete.extra.tipos import TipoDato, TipoRelacional
from interprete.extra.retorno import Retorno
from interprete.extra.enviroment import Enviroment
from interprete.extra.errores import Error, TablaErrores
from interprete.extra.generador import Generador


class Relacional(Expresion):
    def __init__(self, text_val:str, op1:Expresion, operador:TipoRelacional, op2:Expresion, linea, columna):
        super().__init__(text_val, linea, columna)
        self.op1 = op1
        self.op2 = op2
        self.operador = operador
        self.etq_true = ''
        self.etq_false = ''
    
    def ejecutar(self, env:Enviroment):
        op1:Retorno = self.op1.ejecutar(env)
        op2:Retorno = self.op2.ejecutar(env)
        resultado = Retorno(tipo=TipoDato.ERROR, valor=None)

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
                
            if (op1.tipo == TipoDato.NVARCHAR or op1.tipo == TipoDato.NCHAR) and (op2.tipo == TipoDato.NVARCHAR or op2.tipo == TipoDato.NCHAR):
                resultado.tipo = TipoDato.BOOL
                resultado.valor = (op1.valor == op2.valor)
                
        elif self.operador == TipoRelacional.DESIGUALDAD:
            # Agregar cadena con cadena
            if (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL) and (op2.tipo == TipoDato.INT or op2.tipo == TipoDato.DECIMAL):
                resultado.tipo = TipoDato.BOOL
                resultado.valor = (op1.valor != op2.valor)
        
        return resultado
    
    def setEtiquetas(self, etq_true, etq_false):
        self.etq_true = etq_true
        self.etq_false = etq_false
    
    def getEtqTrue(self):
        return self.etq_true

    def getEtqFalse(self):
        return self.etq_false
        
    def ejecutar3d(self, env:Enviroment, generador:Generador):
        '''
            if a < b goto B.true
            goto B.false
        '''
        codigo = ''
        op1:Retorno3d = self.op1.ejecutar3d(env, generador)
        op2:Retorno3d = self.op2.ejecutar3d(env, generador)
        resultado = Retorno(tipo=TipoDato.ERROR, valor=None)

        # Que no haya error en los operandos
        if op1.tipo == TipoDato.ERROR or op2.tipo == TipoDato.ERROR:
            print("Error al realizar la operacion Relacional. En la linea " + str(self.linea))
            # Agregando a la tabla de errores
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error al realizar operacion relacional.')
            TablaErrores.addError(err)
            return resultado
        
        if self.operador == TipoRelacional.MAYOR:
            if (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL) and (op2.tipo == TipoDato.INT or op2.tipo == TipoDato.DECIMAL):
                codigo += f'if ({op1.temporal} > {op2.temporal}) goto {self.etq_true};\n'
                codigo += f'goto {self.etq_false};\n'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal='', tipo=TipoDato.BOOL, etiqueta_verdadera=self.etq_true, etiqueta_falsa=self.etq_false)

        
        elif self.operador == TipoRelacional.MENOR:
            if (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL) and (op2.tipo == TipoDato.INT or op2.tipo == TipoDato.DECIMAL):
                codigo += f'if ({op1.temporal} < {op2.temporal}) goto {self.etq_true};\n'
                codigo += f'goto {self.etq_false};\n'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal='', tipo=TipoDato.BOOL, etiqueta_verdadera=self.etq_true, etiqueta_falsa=self.etq_false)
        
        elif self.operador == TipoRelacional.MAYOR_IGUAL:
            if (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL) and (op2.tipo == TipoDato.INT or op2.tipo == TipoDato.DECIMAL):
                codigo += f'if ({op1.temporal} >= {op2.temporal}) goto {self.etq_true};\n'
                codigo += f'goto {self.etq_false};\n'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal='', tipo=TipoDato.BOOL, etiqueta_verdadera=self.etq_true, etiqueta_falsa=self.etq_false)
        
        elif self.operador == TipoRelacional.MENOR_IGUAL:
            if (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL) and (op2.tipo == TipoDato.INT or op2.tipo == TipoDato.DECIMAL):
                codigo += f'if ({op1.temporal} <= {op2.temporal}) goto {self.etq_true};\n'
                codigo += f'goto {self.etq_false};\n'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal='', tipo=TipoDato.BOOL, etiqueta_verdadera=self.etq_true, etiqueta_falsa=self.etq_false)
        
        elif self.operador == TipoRelacional.IGUALDAD or self.operador == TipoRelacional.IGUAL:
            if (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL) and (op2.tipo == TipoDato.INT or op2.tipo == TipoDato.DECIMAL):
                codigo += f'if ({op1.temporal} == {op2.temporal}) goto {self.etq_true};\n'
                codigo += f'goto {self.etq_false};\n'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal='', tipo=TipoDato.BOOL, etiqueta_verdadera=self.etq_true, etiqueta_falsa=self.etq_false)
                
        elif self.operador == TipoRelacional.DESIGUALDAD:
            # Agregar cadena con cadena
            if (op1.tipo == TipoDato.INT or op1.tipo == TipoDato.DECIMAL) and (op2.tipo == TipoDato.INT or op2.tipo == TipoDato.DECIMAL):
                codigo += f'if ({op1.temporal} != {op2.temporal}) goto {self.etq_true};\n'
                codigo += f'goto {self.etq_false};\n'
                generador.agregarInstruccion(codigo)
                return Retorno3d(codigo=codigo, etiqueta='', temporal='', tipo=TipoDato.BOOL, etiqueta_verdadera=self.etq_true, etiqueta_falsa=self.etq_false)

    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        tipo = ''
        if self.operador == TipoRelacional.IGUALDAD: tipo = '=='
        elif self.operador == TipoRelacional.DESIGUALDAD: tipo = '!='
        elif self.operador == TipoRelacional.MENOR_IGUAL: tipo = '<='
        elif self.operador == TipoRelacional.MAYOR_IGUAL: tipo = '>='
        elif self.operador == TipoRelacional.MENOR: tipo = '<'
        elif self.operador == TipoRelacional.MAYOR: tipo = '>'
        elif self.operador == TipoRelacional.IGUAL: tipo = '='
        hijo = Nodo(id=id, valor=tipo, hijos=[])
        raiz.addHijo(hijo)
        self.op1.recorrerArbol(hijo)
        self.op2.recorrerArbol(hijo)
    