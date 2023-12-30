from interprete.extra.ast import *
from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato
from interprete.extra.retorno import Retorno
from interprete.instrucciones.condicion_where import CondicionWhere
from interprete.extra.enviroment import Enviroment
from interprete.extra.generador import Generador
from interprete.extra.consola import Consola

from xml.dom import minidom

class Contar(Expresion):
    
    def __init__(self, text_val:str, campos: str, tablas:str, condicion_where:CondicionWhere, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.campos = campos
        self.tablas = tablas
        self.condicion_where = condicion_where
        self.counter = 0
        self.aux = ''
    
    def get_valor(self):
        return self.aux
    
    def set_valor(self, aux):
        self.aux = aux
    
    def ejecutar(self, env:Enviroment):
        resultado = Retorno(tipo=TipoDato.INT, valor=0)

        if self.campos != '*':
            # print('Contar no admite campos')
            Consola.addConsola('Contar no admite campos')
            return

        self.count_where(env)

        # Cuando se obtenga la suma, modificar la variable resultado con el con el total
        resultado.valor = self.counter
        # print('RESULTADO: ', resultado.valor)

        return resultado
    
    def count_where(self, env:Enviroment):
        from analizador.parser import parser
        
        datas = open('backend/structure.xml', 'r+', encoding='utf-8')
        mydoc = minidom.parse(datas)
            
        current = mydoc.getElementsByTagName('current')[0]

        for database in mydoc.getElementsByTagName('database'):
            if database.getAttribute('name') == current.getAttribute('name'):
                for table in database.getElementsByTagName('tables'):
                    for table in table.getElementsByTagName('table'):
                        for tabla in self.tablas:
                            if table.getAttribute('name') == tabla:
                                cont_records = 0
                                for recs in table.getElementsByTagName('records'):
                                    for record in recs.getElementsByTagName('record'):
                                        cont_records += 1
                                        
                                        if self.condicion_where == None:
                                            self.counter += 1
                                            continue
                                        
                                        self.set_valor(self.condicion_where.text_val.replace('\'',''))
                                        
                                        for rc in record.getElementsByTagName('field'):
                                            if rc.getAttribute('name') in self.condicion_where.text_val:
                                                self.set_valor(self.get_valor().replace(rc.getAttribute('name'),rc.firstChild.data))
                                              
                                        self.aux += ';'

                                        expresion = parser.parse(self.aux.lower())

                                        retorno:Retorno = expresion[0].ejecutar(env)
                                        if retorno.valor == True:
                                            self.counter += 1
    
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='CONTAR', hijos=[])
        raiz.addHijo(hijo)                                    
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor='*', hijos=[]))

        # Tablas
        for tabla in self.tablas:
            id = AST.generarId()
            hijo.addHijo(Nodo(id=id, valor=tabla, hijos=[]))
        
        # Where
        if self.condicion_where != None:
            self.condicion_where.recorrerArbol(hijo)
    
    def ejecutar3d(self, env:Enviroment, generador:Generador):
        pass


