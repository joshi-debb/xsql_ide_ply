from interprete.extra.ast import *
from interprete.expresiones._return import Return
from xmlrpc.client import Boolean
from interprete.extra.tipos import TipoDato
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion
from interprete.expresiones.Expresion import Expresion
from interprete.extra.retorno import Retorno
from interprete.extra.errores import *
from interprete.instrucciones.else_if import ElseIf

class IfElse(Instruccion):

    def __init__(self, text_val:str, condicion:Expresion, bloque:Instruccion, bandera_else:Boolean, bloque_else:Instruccion, elseifs:ElseIf, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.condicion = condicion
        self.bloque = bloque
        self.bandera_else = bandera_else
        self.bloque_else = bloque_else
        self.elseifs = elseifs              # Lista de elif
        self.linea = linea
        self.columna = columna
        
    def ejecutar(self, env: Enviroment):        
        val_condicion:Retorno = self.condicion.ejecutar(env)

        if val_condicion.tipo == TipoDato.ERROR:
            # Agregando a la tabla de errores
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error al evaluar la condicion IF.')
            TablaErrores.addError(err)
            return Retorno(tipo=TipoDato.ERROR, valor=None)
        
        if val_condicion.tipo != TipoDato.BOOL:
            # Agregando a la tabla de errores
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Se esperaba una expresión expresión de tipo booleano en la condición IF.')
            TablaErrores.addError(err)
            return Retorno(tipo=TipoDato.ERROR, valor=None)
        
        new_env = Enviroment(ent_anterior=env, ambito="IF")

        # Ejecutando bloque de instrucciones dentro de if
        if val_condicion.valor == True:
            ret = self.bloque.ejecutar(new_env)

            if isinstance(ret, Return):
                if not env.dentroDeFuncion():
                    err = Error(tipo='Semántico', linea=ret.linea, columna=ret.columna, descripcion=f'Solo puede haber una sentencia RETURN dentro de una función')
                    TablaErrores.addError(err)
                    return self
                return ret
            return self
        
        # Si hay condiciones else if
        if len(self.elseifs) != 0:
            for elseif in self.elseifs:
                if elseif.evaluarCondicion(env):
                    new_env = Enviroment(ent_anterior=env, ambito="IF")
                    ret = elseif.ejecutar(new_env)
                    if isinstance(ret, Return):
                        if not env.dentroDeFuncion():
                            err = Error(tipo='Semántico', linea=ret.linea, columna=ret.columna, descripcion=f'Solo puede haber una sentencia RETURN dentro de una función')
                            TablaErrores.addError(err)
                            return self
                        return ret
                    return self
                
        # Si hay un bloque else...
        if self.bandera_else == True:
            new_env = Enviroment(ent_anterior=env, ambito="IF")
            ret = self.bloque_else.ejecutar(new_env)
            if isinstance(ret, Return):
                if not env.dentroDeFuncion():
                    err = Error(tipo='Semántico', linea=ret.linea, columna=ret.columna, descripcion=f'Solo puede haber una sentencia RETURN dentro de una función')
                    TablaErrores.addError(err)
                    return self
                return ret

        return self

# self.condicion = condicion
#         self.bloque = bloque
#         self.bandera_else = bandera_else
#         self.bloque_else = bloque_else
#         self.elseifs = elseifs              # Lista de elif

    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='IF', hijos=[])
        raiz.addHijo(hijo)
        self.condicion.recorrerArbol(hijo)
        self.bloque.recorrerArbol(hijo)

        for elseif in self.elseifs:
            elseif.recorrerArbol(hijo)
        
        if self.bandera_else == True:
            id = AST.generarId()
            hijo2 = Nodo(id=id, valor='ELSE', hijos=[])
            hijo.addHijo(hijo2)
            self.bloque_else.recorrerArbol(hijo2)
