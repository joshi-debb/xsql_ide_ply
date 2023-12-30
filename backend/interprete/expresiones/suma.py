from interprete.extra.ast import *
from interprete.expresiones.acceso import Acceso
from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato
from interprete.extra.retorno import Retorno
from interprete.instrucciones.condicion_where import CondicionWhere
from interprete.extra.enviroment import Enviroment
from interprete.extra.generador import Generador
from interprete.extra.consola import Consola

from xml.dom import minidom

class Suma(Expresion):
    
    def __init__(self, text_val:str, campos:str, tablas:str, condicion_where:CondicionWhere, linea:int, columna:int):
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
        
        for campo in self.campos:
            print(self.get_tipo(campo))
            if self.get_tipo(campo) == 'TipoDato.INT' or self.get_tipo(campo) == 'TipoDato.DECIMAL':
                self.select_where(env)
            else:
                Consola.addConsola('No se puede sumar campos no numericos')

        # Cuando se obtenga la suma, modificar la variable resultado con el con el total
        resultado.valor = self.counter

        return resultado
    

    def select_where(self, env:Enviroment):
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
                                            for rc in record.getElementsByTagName('field'):
                                                for campo in self.campos:
                                                    if rc.getAttribute('name') == campo:
                                                        if self.is_integer(rc.firstChild.data):
                                                            self.counter += int(rc.firstChild.data)
                                                        elif self.is_flot(rc.firstChild.data):
                                                            self.counter += float(rc.firstChild.data)
                                               
                                        elif self.condicion_where != None:
                                            self.set_valor(self.condicion_where.text_val.replace('\'',''))
                                            
                                            for rc in record.getElementsByTagName('field'):
                                                if rc.getAttribute('name') in self.condicion_where.text_val:
                                                    self.set_valor(self.get_valor().replace(rc.getAttribute('name'),rc.firstChild.data))

                                            self.aux += ';'
                                            expresion = parser.parse(self.aux.lower())

                                            retorno:Retorno = expresion[0].ejecutar(env)
                                            if retorno.valor == True:
                                                self.look_in_pos(cont_records-1)


    
    def look_in_pos(self, pos:int):

        datas = open('backend/structure.xml', 'r+', encoding='utf-8')

        mydoc = minidom.parse(datas)
                
        current = mydoc.getElementsByTagName('current')[0]

        for database in mydoc.getElementsByTagName('database'):
            if database.getAttribute('name') == current.getAttribute('name'):
                for table in database.getElementsByTagName('tables'):
                    for table in table.getElementsByTagName('table'):
                            for tabla in self.tablas:
                                if table.getAttribute('name') == tabla:
                                    for rc in  table.getElementsByTagName('records')[0].getElementsByTagName('record')[pos].getElementsByTagName('field'):
                                        for campo in self.campos:
                                            if rc.getAttribute('name') == campo:
                                                if self.is_integer(rc.firstChild.data):
                                                    self.counter += int(rc.firstChild.data)
                                                elif self.is_flot(rc.firstChild.data):
                                                    self.counter += float(rc.firstChild.data)
                                                
    
    #obtener el tipo del dato del campo a sumar
    def get_tipo(self, campo:str):
        datas = open('backend/structure.xml', 'r+', encoding='utf-8')
        mydoc = minidom.parse(datas)
            
        current = mydoc.getElementsByTagName('current')[0]

        for database in mydoc.getElementsByTagName('database'):
            if database.getAttribute('name') == current.getAttribute('name'):
                for table in database.getElementsByTagName('tables'):
                    for table in table.getElementsByTagName('table'):
                        for tabla in self.tablas:
                            if table.getAttribute('name') == tabla:
                                for fields in table.getElementsByTagName('fields'):
                                    for field in fields.getElementsByTagName('field'):
                                        if field.getAttribute('name') == campo:
                                            return field.getAttribute('type')


    def is_integer(self, num:str) -> bool:
        try:
            int(num)
            return True
        except ValueError:
            return False
    
    def is_flot(self, num:str) -> bool:
        try:
            float(num)
            return True
        except ValueError:
            return False        

    # self.campos = campos
    # self.tablas = tablas
    # self.condicion_where = condicion_where

    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='SUMA', hijos=[])
        raiz.addHijo(hijo)
        
        # Campos
        for campo in self.campos:                               
            id = AST.generarId()
            hijo.addHijo(Nodo(id=id, valor=campo, hijos=[]))

        # Tablas
        for tabla in self.tablas:
            id = AST.generarId()
            hijo.addHijo(Nodo(id=id, valor=tabla, hijos=[]))
        
        # Where
        if self.condicion_where != None:
            self.condicion_where.recorrerArbol(hijo)
    
    def ejecutar3d(self, env:Enviroment, generador:Generador):
        pass