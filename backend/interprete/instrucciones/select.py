
from interprete.instrucciones.condicion_where import CondicionWhere
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion
from xml.dom import minidom
from interprete.expresiones.concatenar import Concatenar

from interprete.extra.retorno import Retorno



class Select(Instruccion):
    def __init__(self, text_val:str, campos:str, tablas:str, condicion_where:CondicionWhere, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.campos = campos
        self.tablas = tablas
        self.condicion_where = condicion_where
        self.linea = linea
        self.columna = columna

    def ejecutar(self, env:Enviroment):
        print('Ejecutando select')
        # for campo in self.campos:
        #     print('Campo: ', campo)
        # for tabla in self.tablas:
        #     print('Tabla: ', tabla)
        # print('Condicion: ', self.condicion_where.text_val)\
            
        
        # print('-----------------')
        # print('tabla: ', self.listar_campos(env)[0])
        # print('campos: ')
        
        # for i in range(1,len(self.listar_campos(env))):
        #     print(self.listar_campos(env)[i])
        
        if self.condicion_where == None:
            if self.campos == '*':
                self.select_all(env)
            else:
                self.select_fields(env)
        else:
            self.select_where(env)
        
            
            
            
    
    def select_all(self, env:Enviroment):
        datas = open('backend/structure.xml', 'r+', encoding='utf-8')

        mydoc = minidom.parse(datas)
        
        current = mydoc.getElementsByTagName('current')[0]

        for database in mydoc.getElementsByTagName('database'):
            if database.getAttribute('name') == current.getAttribute('name'):                    
                for table in database.getElementsByTagName('tables'):
                    for table in table.getElementsByTagName('table'):

                        if self.campos == '*':
                            for tabla in self.tablas:
                                if table.getAttribute('name') == tabla:
                                    fields = table.getElementsByTagName('fields')[0]
                                    records = table.getElementsByTagName('records')[0]
                                    print('-------- CAMPOS {} -----------'.format(tabla))
                                    for field in fields.getElementsByTagName('field'):
                                        print(field.getAttribute('name'))
                                    for record in records.getElementsByTagName('record'):
                                        print('-------- REGISTRO -----------')
                                        for data in record.getElementsByTagName('field'):
                                            print(data.firstChild.data)
        
    
    def select_fields(self, env:Enviroment):
        datas = open('backend/structure.xml', 'r+', encoding='utf-8')

        mydoc = minidom.parse(datas)
        
        current = mydoc.getElementsByTagName('current')[0]

        for database in mydoc.getElementsByTagName('database'):
            if database.getAttribute('name') == current.getAttribute('name'):                    
                for table in database.getElementsByTagName('tables'):
                    for table in table.getElementsByTagName('table'):
                        for tabla in self.tablas:
                            if table.getAttribute('name') == tabla:
                                fields = table.getElementsByTagName('fields')[0]
                                records = table.getElementsByTagName('records')[0]
                                print('-------- CAMPOS {} -----------'.format(tabla))
                                for field in fields.getElementsByTagName('field'):
                                    for campo in self.campos:
                                        if field.getAttribute('name') == campo:
                                            print(field.getAttribute('name'))
                                            for record in records.getElementsByTagName('record'):
                                                print('-------- REGISTRO -----------')
                                                for data in record.getElementsByTagName('field'):
                                                    if data.getAttribute('name') == campo:
                                                        print(data.firstChild.data)
        
    
    
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
                                print('-------- CAMPOS {} -----------'.format(tabla))
                                for rc in  table.getElementsByTagName('records')[0].getElementsByTagName('record')[pos].getElementsByTagName('field'):
                                    for campo in self.campos:
                                        if rc.getAttribute('name') == campo:
                                            print('campo: ' , campo)
                                            print('valor: ', rc.firstChild.data)
                                            
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
                                        for rc in record.getElementsByTagName('field'):
                                            if rc.getAttribute('name') in self.condicion_where.text_val:
                                                aux = self.condicion_where.text_val.replace(rc.getAttribute('name'),rc.firstChild.data)
                                                aux += ';'
                                                
                                                expresion = parser.parse(aux.lower())

                                                retorno:Retorno = expresion[0].ejecutar(env)
                                                if retorno.valor == True:
                                                    

                                                    self.look_in_pos(cont_records-1)
                                                    break
    
    
    def select_where_between(self, env:Enviroment):
        pass                                                