
class Error:
    def __init__(self, tipo:str, linea:int, columna:int, descripcion:str):
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        self.descripcion = descripcion
    
    def serializar(self):
        return {
            'tipo': self.tipo,
            'linea': self.linea,
            'columna': self.columna,
            'descripcion': self.descripcion
        }

class TablaErrores:
    errores:Error = []   # Lista de errores
    
    def __init__(self):
        pass

    @classmethod
    def addError(cls, error:Error):
        cls.errores.append(error)
    
    @classmethod
    def getTablaErrores(cls):
        return cls.errores
    
    @classmethod
    def serializarTBErrores(cls):
        errores = []
        for error in cls.errores:
            errores.append(error.serializar())
        return errores
    
    