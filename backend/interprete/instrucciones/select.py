
from interprete.instrucciones.instruccion import Instruccion
from xml.dom import minidom

class Select(Instruccion):
    def __init__(self, caso, distinct, all, distinct_on, exps, froms, where, groupby, having, orderby, limit, offset):
        self.caso = caso
        self.distinct = distinct
        self.all = all


