
from interprete.instrucciones.condicion_where import CondicionWhere
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion
from xml.dom import minidom
from interprete.instrucciones.between import Between
from interprete.extra.tipos import TipoDato
from datetime import datetime


from interprete.extra.retorno import Retorno


class Select(Instruccion):
    def __init__(self, text_val:str, campos:str, tablas:str, condicion_where:CondicionWhere, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.campos = campos
        self.tablas = tablas
        self.condicion_where = condicion_where
        self.linea = linea
        self.columna = columna
        self.aux = ''
        self.condicion_bet_aux = ''
        self.condicion_between = 'campo ' + '>='  +' op1 ' + '&&' + ' campo ' + '<=' + ' op2'
        
    def get_valor(self):
        return self.aux
    
    def set_valor(self, aux):
        self.aux = aux
        
    def get_condicion_between(self):
        return self.condicion_between

    def set_condicion_between(self, condicion_between):
        self.condicion_between = condicion_between
        
    def get_condicion_bet_aux(self):
        return self.condicion_bet_aux

    def set_condicion_bet_aux(self, condicion_bet_aux):
        self.condicion_bet_aux = condicion_bet_aux
        

    def ejecutar(self, env:Enviroment):
                
        if self.condicion_where == None:
            if self.campos == '*':
                self.select_all(env)
            else:
                self.select_fields(env)
        else:
            if isinstance(self.condicion_where, Between):
                self.select_where_between(env)
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
                                        
                                        self.set_valor(self.condicion_where.text_val.replace('\'',''))
                                        
                                        for rc in record.getElementsByTagName('field'):
                                            if rc.getAttribute('name') in self.condicion_where.text_val:
                                                self.set_valor(self.get_valor().replace(rc.getAttribute('name'),rc.firstChild.data))
                                              
                                        self.aux += ';'
                                        expresion = parser.parse(self.aux.lower())

                                        retorno:Retorno = expresion[0].ejecutar(env)
                                        if retorno.valor == True:
                                            self.look_in_pos(cont_records-1)
                                            
    
    def select_where_between(self, env:Enviroment):
        if isinstance(self.condicion_where, Between):
            
            from analizador.parser import parser
            
            print('Es between')
            
            
            op1 = self.condicion_where.op1.text_val
            op2 = self.condicion_where.op2.text_val
            campos = self.condicion_where.campo
            
            
            
            op1 = op1.replace(' ','').replace('\'','')
            op2 = op2.replace(' ','').replace('\'','')
            
            if self.is_date_format(op1) and self.is_date_format(op2) or op1.lower() == 'hoy()' or op2.lower() == 'hoy()':
                if op1.lower() == 'hoy()':
                    op1 = datetime.now()
                    op1 = op1.strftime('%d/%m/%Y')
                    op1 = datetime.strptime(op1, '%d/%m/%Y')
                    op1 = str(op1.timestamp())
                else:
                    op1 = datetime.strptime(op1, '%d/%m/%Y')
                    op1 = str(op1.timestamp())
                    
                if op2.lower() == 'hoy()':
                    op2 = datetime.now()
                    op2 = op2.strftime('%d/%m/%Y')
                    op2 = datetime.strptime(op2, '%d/%m/%Y')
                    op2 = str(op2.timestamp())
                    
                else:
                    op2 = datetime.strptime(op2, '%d/%m/%Y')
                    op2 = str(op2.timestamp())
                
                self.set_condicion_between(self.get_condicion_between().replace('op1',op1))
                self.set_condicion_between(self.get_condicion_between().replace('op2',op2))
                self.set_condicion_between(self.get_condicion_between().replace('campo',campos))
                
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
                                                self.set_condicion_bet_aux(self.condicion_between)
                                                for rc in record.getElementsByTagName('field'):
                                                    if rc.getAttribute('name') in self.get_condicion_between():
                                                        value = rc.firstChild.data.replace(' ','').replace('\'','')
                                                        value = datetime.strptime(value, '%d/%m/%Y')
                                                        value = str(value.timestamp())
                                                        self.set_condicion_bet_aux(self.get_condicion_bet_aux().replace(rc.getAttribute('name'),value))
                                                    
                                                self.condicion_bet_aux += ';'
                                                # print(self.condicion_bet_aux)
                                                expresion = parser.parse(self.condicion_bet_aux.lower())

                                                retorno:Retorno = expresion[0].ejecutar(env)
                                                if retorno.valor == True:
                                                    self.look_in_pos(cont_records-1)
                
            elif not self.is_date_format(op1) and not self.is_date_format(op2):
                
                self.set_condicion_between(self.get_condicion_between().replace('op1',op1))
                self.set_condicion_between(self.get_condicion_between().replace('op2',op2))
                self.set_condicion_between(self.get_condicion_between().replace('campo',campos))
                
                
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
                                                self.set_condicion_bet_aux(self.condicion_between)
                                                for rc in record.getElementsByTagName('field'):
                                                    if rc.getAttribute('name') in self.get_condicion_between():
                                                        self.set_condicion_bet_aux(self.get_condicion_bet_aux().replace(rc.getAttribute('name'),rc.firstChild.data))
                                                    
                                                self.condicion_bet_aux += ';'
                                                # print(self.condicion_bet_aux)
                                                expresion = parser.parse(self.condicion_bet_aux.lower())

                                                retorno:Retorno = expresion[0].ejecutar(env)
                                                if retorno.valor == True:
                                                    self.look_in_pos(cont_records-1)
            else:
                print('No se puede operar fecha con otro tipo de dato')
                return
    
    def look_in_pos(self, pos:int):

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
                                    print('-------- CAMPOS {} -----------'.format(tabla))
                                    for field in fields.getElementsByTagName('field'):
                                        print(field.getAttribute('name'))
                                    print('-------- REGISTRO -----------')
                                    for rc in  table.getElementsByTagName('records')[0].getElementsByTagName('record')[pos].getElementsByTagName('field'):
                                        print(rc.firstChild.data)
                        else:
                            for tabla in self.tablas:
                                if table.getAttribute('name') == tabla:
                                    print('-------- CAMPOS {} -----------'.format(tabla))
                                    for campo in self.campos:
                                        print(campo)
                                    
                                    print('-------- REGISTRO -----------')
                                    for rc in  table.getElementsByTagName('records')[0].getElementsByTagName('record')[pos].getElementsByTagName('field'):
                                        for campo in self.campos:
                                            if rc.getAttribute('name') == campo:
                                                print(rc.firstChild.data)

   
    
    def is_date_format(self, date):
        try:
            datetime.strptime(date, '%d/%m/%Y')
            return True
        except ValueError:
            return False
    