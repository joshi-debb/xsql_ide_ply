from interprete.extra.symbol import Symbol
from interprete.extra.tipos import TipoSimbolo
from interprete.extra.symbol_table import TablaSimbolos

class Enviroment():
    env_list = []
    def __init__(self, ent_anterior, ambito:str):
        self.ent_anterior:Enviroment = ent_anterior
        self.ambito = ambito
        self.ts_variables = TablaSimbolos()
        self.ts_funciones = TablaSimbolos()
        self.ts_procedures = TablaSimbolos()
        self.dentro_funcion = False
        self.generador = None
        self.tamanio = 0                    # Para manejo de funciones/procedimientos (es como un offset)
        Enviroment.addEnviroment(self)
    
    # Incrementa el tamaño del entorno
    def incrementarTamanio(self):
        self.tamanio += 1

    def getTamanio(self):
        return self.tamanio

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
    
    # Serializa la tabla de simbolos de un entorno
    def getTablaSimbolos(self):
        simbolos = []
        # Llenado de variables
        for simbolo in self.ts_variables.getTS():
            template = {
                'simbolo': simbolo.tipo_simbolo.name,
                'tipo': simbolo.tipo.name,
                'id': simbolo.id,
                'valor': simbolo.valor,
                'parametros': simbolo.serializarParametros(),
                'ambito': simbolo.ambito
            }
            simbolos.append(template)

        # Llenado de funciones
        for simbolo in self.ts_funciones.getTS():
            template = {
                'simbolo': simbolo.tipo_simbolo.name,
                'tipo': simbolo.tipo.name,
                'id': simbolo.id,
                'valor': '',
                'parametros': simbolo.serializarParametros(),
                'ambito': simbolo.ambito
            }
            simbolos.append(template)

        # Llenado de procedmientos
        for simbolo in self.ts_procedures.getTS():
            template = {
                'simbolo': simbolo.tipo_simbolo.name,
                'tipo': simbolo.tipo.name,
                'id': simbolo.id,
                'valor': '',
                'parametros': simbolo.serializarParametros(),
                'ambito': simbolo.ambito
            }
            simbolos.append(template)
        
        return simbolos

    
    @classmethod
    def addEnviroment(cls, env):
        cls.env_list.append(env)
    
    @classmethod
    def getEnviroments(cls):
        return cls.env_list
    
    # Obtiene los simbolos de todos los entornos creados
    @classmethod
    def serializarTodosSimbolos(cls):
        simbolos = []
        for env in cls.env_list:
            simbolos = simbolos + env.getTablaSimbolos()
        return simbolos

    @classmethod
    def cleanEnviroments(cls):
        cls.env_list = []