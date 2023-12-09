from .instruccion import Instruccion
from .atributo import Atributo
from interprete.extra.tipos import *
from interprete.expresiones.tipoChars import TipoChars


from xml.dom import minidom

class CrearTB(Instruccion):
    def __init__(self, id, atributos:Atributo , linea:int, columna:int):
        super().__init__(linea, columna)
        self.id = id
        self.atributos = atributos
    
    def ejecutar(self):
        print("nombre tabla: ", self.id)
        for atributo in self.atributos:
            print("atributo: ",atributo.id)
            
            if isinstance(atributo.tipo, TipoChars):
                print("tipo: ", atributo.tipo.charTipo)
                print("valor: ", atributo.tipo.valor.ejecutar())
            else:
                print("tipo: ", atributo.tipo)    
            
            for parametro in atributo.parametros:
                if parametro == TipoOpciones.NOTNULL:
                    print("not null")
                elif parametro == TipoOpciones.NULL:
                    print("null")
                elif parametro == TipoOpciones.PRIMARYKEY:
                    print("primary key")
                print(parametro)
            print("------------------")
            