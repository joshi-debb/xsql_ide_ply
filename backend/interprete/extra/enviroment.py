from interprete.extra.symbol import Symbol
from interprete.extra.tipos import TipoSimbolo
from interprete.extra.symbol_table import TablaSimbolos

class Enviroment():
    def __init__(self, ent_anterior, ambito:str):
        self.ent_anterior:Enviroment = ent_anterior
        self.ambito = ambito
        self.ts_variables = TablaSimbolos()
        self.ts_funciones = TablaSimbolos()
        self.ts_procedures = TablaSimbolos()
        self.dentro_funcion = False
    
    def insertar_simbolo(self, id:str, simbolo:Symbol):
        if simbolo.tipo_simbolo == TipoSimbolo.VARIABLE:
            self.ts_variables.instertarSimbolo(id, simbolo)
        elif simbolo.tipo_simbolo == TipoSimbolo.FUNCTION:
            self.ts_funciones.instertarSimbolo(id, simbolo)
        elif simbolo.tipo_simbolo == TipoSimbolo.PROCEDURE:
            self.ts_procedures.instertarSimbolo(id, simbolo)
    
    def existe_simbolo(self, id:str, tipoSimbolo:TipoSimbolo):
        ent:Enviroment = self

        while ent is not None:
            if(tipoSimbolo == TipoSimbolo.VARIABLE):
                existe = ent.ts_variables.buscarSimbolo(id)
            elif(tipoSimbolo == TipoSimbolo.FUNCTION):
                existe = ent.ts_funciones.buscarSimbolo(id)
            elif(tipoSimbolo == TipoSimbolo.PROCEDURE):
                existe = ent.ts_procedures.buscarSimbolo(id)
            if (existe is not None):
                return True
            ent = ent.ent_anterior
        return False
    
    def getSimbolo(self, id:str, tipo_simbolo:TipoSimbolo):
        ent:Enviroment = self
        
        while ent is not None:
            if (tipo_simbolo == TipoSimbolo.VARIABLE):
                simbolo = ent.ts_variables.getSimbolo(id)
            elif (tipo_simbolo == TipoSimbolo.FUNCTION):
                simbolo = ent.ts_funciones.getSimbolo(id)
            elif (tipo_simbolo == TipoSimbolo.PROCEDURE):
                simbolo = ent.ts_procedures.getSimbolo(id)

            if (simbolo is not None):
                return simbolo
            ent = ent.ent_anterior
        return None
    
    def existe_simbolo_ent_actual(self, id:str, tipo_simbolo:TipoSimbolo):
        if(tipo_simbolo == TipoSimbolo.VARIABLE):
            existe = self.ts_variables.getSimbolo(id)
        elif (tipo_simbolo == TipoSimbolo.FUNCTION):
            existe = self.ts_funciones.getSimbolo(id)
        elif (tipo_simbolo == TipoSimbolo.PROCEDURE):
            existe = self.ts_procedures.getSimbolo(id)
        if(existe is not None):
            return True
        return False
    
    # Valida si hay una funcion en un entorno mas externo
    def dentroDeFuncion(self) -> bool:
        ent:Enviroment = self
        
        while ent is not None:
            if ent.getDentroFunction():
                return True
            ent = ent.ent_anterior
        return False
    
    def setDentroFuncion(self, val:bool):
        self.dentro_funcion = val
    
    def getDentroFunction(self):
        return self.dentro_funcion
    
    