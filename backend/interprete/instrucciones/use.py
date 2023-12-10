
from .instruccion import Instruccion

class Use(Instruccion):
    current_db = ''
    
    def __init__(self, id, line, column):
        self.id = id
        self.line = line
        self.column = column
        
    def ejecutar(self):
        Use.current_db = self.id
    
    @classmethod
    def getCurrentDB(cls):
        return cls.current_db