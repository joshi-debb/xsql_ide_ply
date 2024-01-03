from interprete.extra.ast import *
from interprete.instrucciones.instruccion import Instruccion
from interprete.instrucciones.asignacion_campo import Campo
from interprete.instrucciones.condicion_where import CondicionWhere
from xml.dom import minidom
from interprete.extra.enviroment import Enviroment
from interprete.extra.consola import Consola

class Update(Instruccion):
    def __init__(self, text_val:str, table_name:str, tupla:Campo, condicion:CondicionWhere, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.table_name = table_name
        self.tupla = tupla                 
        self.condicion = condicion
    
    def ejecutar(self, env:Enviroment):

        if self.is_pk_repetido(env):
            Consola.addConsola('Error: Llave primaria repetida')
            return

        if self.look_in_pos(env) < 0:
            Consola.addConsola('Error: Registro no encontrado')
            return

        with open('backend/structure.xml', 'r+', encoding='utf-8') as file:
            mydoc = minidom.parse(file)
            
            current = mydoc.getElementsByTagName('current')[0]

            for database in mydoc.getElementsByTagName('database'):
                if database.getAttribute('name') == current.getAttribute('name'):
                    for table in database.getElementsByTagName('tables'):
                        for table in table.getElementsByTagName('table'):
                            if table.getAttribute('name') == self.table_name:
                                for rc in  table.getElementsByTagName('records')[0].getElementsByTagName('record')[self.look_in_pos(env)].getElementsByTagName('field'):
                                    for tup in self.tupla:
                                        if rc.getAttribute('name') == tup.id:
                                            rc.firstChild.data = tup.expresion.ejecutar(env).valor
                                            Consola.addConsola('Registro actualizado')
                                            break
     
            xml_str = mydoc.toxml(encoding='utf-8').decode('utf-8').replace('\n', '').replace('\t', '')
            formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
            file.seek(0)
            file.truncate()
            file.write(formatted_xml)

    def look_in_pos(self, env:Enviroment) -> int:
        datas = open('backend/structure.xml', 'r+', encoding='utf-8')

        mydoc = minidom.parse(datas)
        
        current = mydoc.getElementsByTagName('current')[0]

        for database in mydoc.getElementsByTagName('database'):
            if database.getAttribute('name') == current.getAttribute('name'):
                for table in database.getElementsByTagName('tables'):
                    for table in table.getElementsByTagName('table'):
                        if table.getAttribute('name') == self.table_name:
                            found = 0
                            cont_records = 0
                            for recs in table.getElementsByTagName('records'):
                                for record in recs.getElementsByTagName('record'):
                                    cont_records += 1
                                    for rc in record.getElementsByTagName('field'):
                                        print(rc.getAttribute('name'), '==', self.condicion.id, 'and', rc.firstChild.data ,'==', self.condicion.expresion.ejecutar(env).valor)
                                        if rc.getAttribute('name') == self.condicion.id and rc.firstChild.data == str(self.condicion.expresion.ejecutar(env).valor):
                                            found = cont_records
                                            break
        return found-1


    def is_pk_repetido(self, env:Enviroment) -> bool:

        is_pk = False
        
        datas = open('backend/structure.xml', 'r+', encoding='utf-8')

        mydoc = minidom.parse(datas)
        
        current = mydoc.getElementsByTagName('current')[0]
    
        for database in mydoc.getElementsByTagName('database'):
            if database.getAttribute('name') == current.getAttribute('name'):                    
                for table in database.getElementsByTagName('tables'):
                    for table in table.getElementsByTagName('table'):
                        if table.getAttribute('name') == self.table_name:
                            fields = table.getElementsByTagName('fields')[0]
                            for field in fields.getElementsByTagName('field'):
                                for tup in self.tupla:
                                    if field.getAttribute('name') == tup.id:
                                        if field.getAttribute('param1') == 'TipoOpciones.PRIMARYKEY' or field.getAttribute('param2') == 'TipoOpciones.PRIMARYKEY': 
                                            is_pk = True
                                            break
                            
                            if is_pk == True:
                                records = table.getElementsByTagName('records')[0]

                                for recs in records.getElementsByTagName('record'):
                                    for rc in recs.getElementsByTagName('field'):
                                        for tup in self.tupla:
                                            if rc.getAttribute('name') == tup.id:
                                                if rc.firstChild.data == tup.expresion.ejecutar(env).valor:
                                                    return True
        
        return False
    
    # self.table_name = table_name
    # self.tupla = tupla                 
    # self.condicion = condicion
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='UPDATE', hijos=[])
        raiz.addHijo(hijo)
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor=self.table_name, hijos=[]))

        # Campos
        for campo in self.tupla:
            campo.recorrerArbol(hijo)
        
        # Condicion
        self.condicion.recorrerArbol(hijo)
