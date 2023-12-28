from interprete.extra.tipos import TipoDato

class Retorno:
    def __init__(self, tipo:TipoDato, valor:any):
        self.tipo = tipo
        self.valor = valor
        
class Retorno3d:
    def __init__(self, codigo='', etiqueta='', temporal='', tipo=None, valor='', etiqueta_verdadera='', etiqueta_falsa=''):
        self.codigo = codigo
        self.etiqueta = etiqueta
        self.temporal = temporal
        self.tipo = tipo
        self.valor = valor
        self.etiqueta_verdadera = ''
        self.etiqueta_falsa = ''

    
    def iniciarRetorno(self, codigo, etiqueta, temporal, tipo):
        self.codigo = codigo            
        self.etiqueta = etiqueta
        self.temporal = temporal
        self.tipo = tipo