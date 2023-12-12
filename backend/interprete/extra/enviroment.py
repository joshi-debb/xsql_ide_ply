from interprete.extra.symbol import Symbol
from interprete.extra.tipos import TipoSimbolo
from interprete.extra.symbol_table import TablaSimbolos

class Enviroment():
    def __init__(self, ent_anterior, ambito:str):
        self.ent_anterior:Enviroment = ent_anterior
        self.ambito = ambito
        self.ts_variables = TablaSimbolos()
    
    def insertar_simbolo(self, id:str, simbolo:Symbol):
        if simbolo.tipo_simbolo == TipoSimbolo.VARIABLE:
            self.ts_variables.instertarSimbolo(id, simbolo)
    
    def existe_simbolo(self, id:str, tipoSimbolo:TipoSimbolo):
        ent:Enviroment = self

        while ent is not None:
            if(tipoSimbolo == TipoSimbolo.VARIABLE):
                existe = ent.ts_variables.buscarSimbolo(id)
            # elif(tipoSimbolo == TipoSimbolo.FUNCION):
            #     existe = ent.tsFunciones.buscar_simbolo(id)
            if (existe is not None):
                return True
            ent = ent.ent_anterior
        return False
    
    def getSimbolo(self, id:str, tipo_simbolo:TipoSimbolo):
        ent:Enviroment = self
        
        while ent is not None:
            if (tipo_simbolo == TipoSimbolo.VARIABLE):
                simbolo = ent.ts_variables.getSimbolo(id)
            # elif (tipo_simbolo == TipoSimbolo.FUNCION):
            #     simbolo = ent.tsFunciones.buscar_simbolo(id)

            if (simbolo is not None):
                return simbolo
            ent = ent.ent_anterior
        return None
    
    def existe_simbolo_ent_actual(self, id:str, tipo_simbolo:TipoSimbolo):
        if(tipo_simbolo == TipoSimbolo.VARIABLE):
            existe = self.ts_variables.getSimbolo(id)
        # elif (tipoSimbolo == TipoSimbolo.FUNCION):
        #     existe = self.tsFunciones.get_simbolo(id)

        if(existe is not None):
            return True
        return False
    
    