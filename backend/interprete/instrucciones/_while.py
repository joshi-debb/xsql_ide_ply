from interprete.extra.ast import *
from interprete.expresiones._return import Return
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion
from interprete.expresiones.Expresion import Expresion
from interprete.instrucciones.bloque import Bloque
from interprete.extra.tipos import *
from interprete.extra.retorno import Retorno
from interprete.extra.errores import *

class While(Instruccion):

    def __init__(self, text_val:str, condicion:Expresion, bloque:Bloque, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.condicion = condicion
        self.bloque = bloque
    
    def ejecutar(self, env:Enviroment):
        val_condicion:Retorno = self.condicion.ejecutar(env)

        if val_condicion.tipo == TipoDato.ERROR:
            # Agregando a la tabla de errores
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Error al evaluar la condicion WHILE.')
            TablaErrores.addError(err)
            return Retorno(tipo=TipoDato.ERROR, valor=None)
        
        if val_condicion.tipo != TipoDato.BOOL:
            # Agregando a la tabla de errores
            err = Error(tipo='Semántico', linea=self.linea, columna=self.columna, descripcion=f'Se esperaba una expresión de tipo booleano en la condición IF pero se obtuvo {val_condicion.tipo.name}')
            TablaErrores.addError(err)
            return Retorno(tipo=TipoDato.ERROR, valor=None)
        
        # Ejecutando bloque de instrucciones dentro del while
        while val_condicion.valor == True:
            new_env = Enviroment(ent_anterior=env, ambito="WHILE")
            ret = self.bloque.ejecutar(new_env)
            if isinstance(ret, Return):
                if not env.dentroDeFuncion():
                    err = Error(tipo='Semántico', linea=ret.linea, columna=ret.columna, descripcion=f'Solo puede haber una sentencia RETURN dentro de una función')
                    TablaErrores.addError(err)
                    return self
                return ret
            val_condicion = self.condicion.ejecutar(new_env)

        return self        
    
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='WHILE', hijos=[])
        raiz.addHijo(hijo)
        self.condicion.recorrerArbol(hijo)
        self.bloque.recorrerArbol(hijo)
