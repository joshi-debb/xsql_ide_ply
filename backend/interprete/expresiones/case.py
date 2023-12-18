from interprete.instrucciones.bloque import Bloque
from interprete.extra.tipos import TipoDato
from interprete.extra.enviroment import Enviroment
from interprete.expresiones.Expresion import Expresion
from interprete.extra.retorno import Retorno
from interprete.extra.errores import *
from interprete.expresiones.when import When
from interprete.expresiones._return import Return

class Case(Expresion):

    def __init__(self, text_val:str, lista_when:When, _else:bool, bloque_else:Bloque, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.lista_when = lista_when
        self._else = _else
        self.bloque_else = bloque_else
    
    def ejecutar(self, env: Enviroment):
        print(self.text_val)
        
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
                    return Retorno(tipo=TipoDato.ERROR, valor=None)
        
        # Si viene un bloque ELSE
        if self._else == True:
            print('SE EJECUTARA EL ELSE')
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

        return Retorno(tipo=TipoDato.ERROR, valor=None)