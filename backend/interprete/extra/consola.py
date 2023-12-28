
class Consola:
    consola:str = []
    def __init__(self):
        pass
    
    @classmethod
    def serializar(cls):
        return {
            'consola': cls.consola 
        }

    @classmethod
    def addConsola(cls, datos:str):
        cls.consola.append(datos)
        # cls.consola += f'{datos}\n'
    
    @classmethod
    def getConsola(cls):
        return cls.consola
    
    @classmethod
    def cleanConsola(cls):
        cls.consola = []