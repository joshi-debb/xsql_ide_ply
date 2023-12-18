from interprete.expresiones.tipoChars import TipoChars
from .instruccion import Instruccion
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.declaracion_var import Declaracion
from interprete.instrucciones.bloque import Bloque
from interprete.extra.tipos import *
from interprete.extra.errores import *
from interprete.extra.symbol import Symbol

class Function(Instruccion):

    def __init__(self, text_val:str, tipo_ret:TipoDato, id:str, parametros:Instruccion, instrucciones:Bloque, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        if isinstance(tipo_ret, TipoChars): self.tipo_ret = tipo_ret.charTipo
        else:                               self.tipo_ret = tipo_ret
        self.id = id
        if parametros[0] == None: self.parametros = []            # Arreglo de declaraciones
        else:                     self.parametros = parametros
        self.instrucciones = instrucciones
    
    def ejecutar(self, env: Enviroment):
        # Guardar la funcion en el XML en la base de datos actual
        # Validar que no exista un funcion con el mismo nombre antes de insertar en XML
        with open('backend/ejemplo.txt', 'w', encoding='utf-8') as file:
            file.write(self.text_val)
        
        return self
    
    # Insertar un nuevo simbolo (procedimiento) a la tabla de simbolos
    def guardarEnTablaSimbolos(self, env:Enviroment):
        simbolo = Symbol(TipoSimbolo.FUNCTION, TipoDato.UNDEFINED, self.id, None, env.ambito, self.parametros, self.instrucciones)
        env.insertar_simbolo(self.id, simbolo)
    
    def getTipoRetorno(self):
        return self.tipo_ret