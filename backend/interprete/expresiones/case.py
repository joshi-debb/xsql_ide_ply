from interprete.extra.ast import *
from interprete.instrucciones.bloque import Bloque
from interprete.extra.tipos import TipoDato
from interprete.extra.enviroment import Enviroment
from interprete.expresiones.Expresion import Expresion
from interprete.extra.retorno import Retorno
from interprete.extra.errores import *
from interprete.expresiones.when import When
from interprete.expresiones._return import Return
from interprete.extra.generador import Generador


class Case(Expresion):

    def __init__(self, text_val:str, lista_when:When, _else:bool, bloque_else:Bloque, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.lista_when = lista_when
        self._else = _else
        self.bloque_else = bloque_else
    
    def ejecutar(self, env: Enviroment):        
        # Si hay condiciones 'when'
        if len(self.lista_when) != 0:
            for when in self.lista_when:
                if when.evaluarCondicion(env):
                    new_env = Enviroment(ent_anterior=env, ambito="CASE")
                    ret = when.ejecutar(new_env)
                    if isinstance(ret, Return):
                        if not env.dentroDeFuncion():
                            err = Error(tipo='Semántico', linea=ret.linea, columna=ret.columna, descripcion=f'Solo puede haber una sentencia RETURN dentro de una función')
                            TablaErrores.addError(err)
                            return Retorno(tipo=TipoDato.ERROR, valor=None)
                        return ret

                    elif isinstance(ret, Retorno):
                        return ret
                    return self
        
        # Si viene un bloque ELSE
        if self._else == True:
            new_env = Enviroment(ent_anterior=env, ambito="CASE")
            ret = self.bloque_else.ejecutar(new_env)
            if isinstance(ret, Return):
                if not env.dentroDeFuncion():
                    err = Error(tipo='Semántico', linea=ret.linea, columna=ret.columna, descripcion=f'Solo puede haber una sentencia RETURN dentro de una función')
                    TablaErrores.addError(err)
                    return Retorno(tipo=TipoDato.ERROR, valor=None)
                return ret

            elif isinstance(ret, Retorno):
                return ret

        return self
    

    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='CASE', hijos=[])
        raiz.addHijo(hijo)

        for when in self.lista_when:
            when.recorrerArbol(hijo)
        
        if self._else == True:
            id = AST.generarId()
            hijo = Nodo(id=id, valor='ELSE', hijos=[])
            raiz.addHijo(hijo)
            self.bloque_else.recorrerArbol(hijo)
            
    def generar3d(self,env: Enviroment, generador: Generador):
        pass
    