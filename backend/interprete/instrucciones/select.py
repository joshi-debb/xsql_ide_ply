from interprete.extra.ast import *
from interprete.instrucciones.condicion_where import CondicionWhere
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion
from xml.dom import minidom
from interprete.instrucciones.between import Between
from interprete.extra.tipos import TipoDato
from datetime import datetime
from interprete.extra.select_table import Record, Select_table
from interprete.extra.retorno import Retorno


class Select(Instruccion):
    tabla = {}
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
    
    
    @classmethod
    def get_tabla(cls):
        return cls.tabla
    
    def ejecutar(self, env:Enviroment):
        
        if isinstance(self.condicion_where, Between):            
            self.select_where_between(env)
        else:
            self.select_where(env)
                                                    
    def select_where(self, env:Enviroment):
        from analizador.parser import parser
        
        select = Select_table()
        aux_list = []
        
        cant_campos = 0

        datas = open('backend/structure.xml', 'r+', encoding='utf-8')
        mydoc = minidom.parse(datas)
            
        current = mydoc.getElementsByTagName('current')[0]

        if self.campos == '*':
            for database in mydoc.getElementsByTagName('database'):
                if database.getAttribute('name') == mydoc.getElementsByTagName('current')[0].getAttribute('name'):
                    for table in database.getElementsByTagName('tables')[0].getElementsByTagName('table'):
                        if self.campos == '*':
                            for tabla in self.tablas:
                                if table.getAttribute('name') == tabla:
                                    for field in table.getElementsByTagName('fields')[0].getElementsByTagName('field'):
                                        select.fields.append(field.getAttribute('name'))
                                        cant_campos += 1
        else:
            for campo in self.campos:
                select.fields.append(campo.text_val)
                cant_campos += 1

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
                                            self.look_in_pos(cont_records-1,aux_list)
                                            continue
                                    
                                        else:
                                            self.set_valor(self.condicion_where.text_val.replace('\'',''))
                                            
                                            for rc in record.getElementsByTagName('field'):
                                                aux = table.getAttribute('name') + '.' + rc.getAttribute('name')
                                                if aux in self.condicion_where.text_val:
                                                    self.set_valor(self.get_valor().replace(aux,rc.firstChild.data))
                                                
                                            self.aux += ';'
                                            print('aux: ', self.aux)
                                            expresion = parser.parse(self.aux.lower())

                                            retorno:Retorno = expresion[0].ejecutar(env)
                                            if retorno.valor == True:
                                                self.look_in_pos(cont_records-1,aux_list)
        
        
        for i in range(0, len(aux_list), cant_campos):
            rec = Record()
            for j in range(cant_campos):
                rec.recods.append(aux_list[i+j])
            select.records.append(rec)
        
        Select.tabla = select.serializar()
                                            
    
    def select_where_between(self, env:Enviroment):
        if isinstance(self.condicion_where, Between):
            
            select = Select_table()
            aux_list = []
            cant_campos = 0
            
            from analizador.parser import parser
            
            if self.campos == '*':
                
                datas = open('backend/structure.xml', 'r+', encoding='utf-8')
                mydoc = minidom.parse(datas)
                
                for database in mydoc.getElementsByTagName('database'):
                    if database.getAttribute('name') == mydoc.getElementsByTagName('current')[0].getAttribute('name'):
                        for table in database.getElementsByTagName('tables')[0].getElementsByTagName('table'):
                            if self.campos == '*':
                                for tabla in self.tablas:
                                    if table.getAttribute('name') == tabla:
                                        for field in table.getElementsByTagName('fields')[0].getElementsByTagName('field'):
                                            select.fields.append(field.getAttribute('name'))
                                            cant_campos += 1
            else:
                for campo in self.campos:
                    select.fields.append(campo.text_val)
                    cant_campos += 1
            
            
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
                                                    self.look_in_pos(cont_records-1,aux_list)
                                                    
                                                    
                for i in range(0, len(aux_list), cant_campos):
                    rec = Record()
                    for j in range(cant_campos):
                        rec.recods.append(aux_list[i+j])
                    select.records.append(rec)
                
                Select.tabla = select.serializar()
                
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
                                                    self.look_in_pos(cont_records-1,aux_list)
                                                    
                for i in range(0, len(aux_list), cant_campos):
                    rec = Record()
                    for j in range(cant_campos):
                        rec.recods.append(aux_list[i+j])
                    select.records.append(rec)
                
                Select.tabla = select.serializar()                                    

            else:
                Consola.addConsola('No se puede operar fecha con otro tipo de dato')
                return
    
    def look_in_pos(self, pos:int, aux_list):

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
                                    for rc in  table.getElementsByTagName('records')[0].getElementsByTagName('record')[pos].getElementsByTagName('field'):
                                        aux_list.append(rc.firstChild.data)
                        else: 
                            for tabla in self.tablas:
                                if table.getAttribute('name') == tabla:
                                    # print('-------- REGISTRO -----------')
                                    for rc in  table.getElementsByTagName('records')[0].getElementsByTagName('record')[pos].getElementsByTagName('field'):
                                        for campo in self.campos:
                                            campo_aux = str(campo.text_val).replace(table.getAttribute('name'),'').replace('.','')
                                            if rc.getAttribute('name') == campo_aux:
                                                aux_list.append(rc.firstChild.data)
                                                # print(rc.firstChild.data)
    
    def is_date_format(self, date):
        try:
            datetime.strptime(date, '%d/%m/%Y')
            return True
        except ValueError:
            return False
        
    # self.campos = campos
    # self.tablas = tablas
    # self.condicion_where = condicion_where
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='SELECT', hijos=[])
        raiz.addHijo(hijo)

        id = AST.generarId()
        hijo2 = Nodo(id=id, valor='CAMPOS', hijos=[])
        hijo.addHijo(hijo2)

        # Campos
        if self.campos == '*':
            id = AST.generarId()
            hijo2.addHijo(Nodo(id=id, valor='*', hijos=[]))
        else:
            # Campo es una 'expresion'
            for campo in self.campos:
                campo.recorrerArbol(hijo2)
        
        # Tablas
        for tabla in self.tablas:
            id = AST.generarId()
            hijo.addHijo(Nodo(id=id, valor=tabla, hijos=[]))
        
        # Condicion where
        if self.condicion_where != None:
            id = AST.generarId()
            hijo3 = Nodo(id=id, valor='WHERE', hijos=[])
            hijo.addHijo(hijo3)
            self.condicion_where.recorrerArbol(hijo3)
        