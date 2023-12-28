from interprete.expresiones.relacional import Relacional
from interprete.extra.retorno import Retorno3d
from interprete.extra.ast import *
from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato, TipoLogico
from interprete.extra.retorno import Retorno
from interprete.extra.enviroment import Enviroment
from interprete.extra.errores import Error, TablaErrores
from interprete.extra.generador import Generador


class Logica(Expresion):
    def __init__(self, text_val:str, op1:Expresion, operador:TipoLogico, op2:Expresion, linea, columna):
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
    
    def setEtiquetas(self, etq_true, etq_false):
        self.etq_true = etq_true
        self.etq_false = etq_false
    
    def getEtqTrue(self):
        return self.etq_true

    def getEtqFalse(self):
        return self.etq_false

    # B -> B1 && B2 | B1.true = B.nuevaEtiqueta
    #               | B1.false = false
    #               | B2.true = B.true
    #               | B2.false = B.false
    #               | B.codigo = B1.codigo + etiqueta(B1.true) + B2.codigo
    def ejecutar3d(self, env:Enviroment, generador:Generador):
        # op1:Retorno3d = self.op1.ejecutar3d(env, generador)
        # op2:Retorno3d = self.op2.ejecutar3d(env, generador)

        # # Que no haya error en los operandos
        # if op1.tipo == TipoDato.ERROR or op2.tipo == TipoDato.ERROR:
        #     # Agregando a la tabla de errores
        #     err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error al realizar la operacion logica.')
        #     TablaErrores.addError(err)
        #     return Retorno3d()
        
        # if op1.tipo != TipoDato.BOOL or op2.tipo != TipoDato.BOOL:
        #     # Agregando a la tabla de errores
        #     err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Ambas expresiones deben ser de tipo logicas (true o false).')
        #     TablaErrores.addError(err)
        #     return Retorno3d()
        
        # if isinstance(self.op1, Relacional) == False:
        #     if isinstance(self.op1, Logica) == False:
        #         return Retorno3d()
        # if isinstance(self.op2, Relacional) == False:
        #     if isinstance(self.op2, Logica) == False:
        #         return Retorno3d()

        if self.operador == TipoLogico.AND:
            self.op1.setEtiquetas(generador.obtenerEtiqueta(), self.etq_false)
            self.op2.setEtiquetas(self.etq_true, self.etq_false)

            op1_res:Retorno3d = self.op1.ejecutar3d(env, generador)
            generador.agregarInstruccion(f'{self.op1.getEtqTrue()}:')
            op2_res:Retorno3d = self.op2.ejecutar3d(env, generador)

            return Retorno3d(etiqueta_verdadera=self.etq_true, etiqueta_falsa=self.etq_false, tipo=TipoDato.BOOL)

        elif self.operador == TipoLogico.OR:
            self.op1.setEtiquetas(self.etq_true, generador.obtenerEtiqueta())
            self.op2.setEtiquetas(self.etq_true, self.etq_false)

            op1_res:Retorno3d = self.op1.ejecutar3d(env, generador)
            generador.agregarInstruccion(f'{self.op1.getEtqFalse()}:')
            op2_res:Retorno3d = self.op2.ejecutar3d(env, generador)

            return Retorno3d(etiqueta_verdadera=self.etq_true, etiqueta_falsa=self.etq_false, tipo=TipoDato.BOOL)

        # elif self.operador == TipoLogico.NOT:
        #     resultado.tipo = TipoDato.BOOL
        #     resultado.valor = not op1.valor
        
        

    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        tipo = ''
        if self.operador == TipoLogico.AND: tipo = '&&'
        elif self.operador == TipoLogico.OR: tipo = '||'
        elif self.operador == TipoLogico.NOT: tipo = '!'
        hijo = Nodo(id=id, valor=tipo, hijos=[])
        raiz.addHijo(hijo)
        self.op1.recorrerArbol(hijo)
        if self.operador == TipoLogico.NOT:
            return
        self.op2.recorrerArbol(hijo)
        