from interprete.extra.tipos import TipoDato

class Retorno:
    def __init__(self, tipo:TipoDato, valor:any):
        self.tipo = tipo
        self.valor = valor