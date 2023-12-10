from interprete.instrucciones.instruccion import Instruccion
from interprete.instrucciones.asignacion_campo import Campo
from interprete.instrucciones.condicion_where import CondicionWhere

class Update(Instruccion):
    def __init__(self, name_table, asignaciones, where:CondicionWhere, line, column):
        self.name_table = name_table
        self.asignaciones = asignaciones
        self.where = where
        self.line = line
        self.columna = column

    def ejecutar(self):
        print("ejecutar")
        print(self.name_table)
        print(self.asignaciones)
        print(self.where)
        print(self.line)
        print(self.columna)
        # with open('backend/structure.xml', 'r+', encoding='utf-8') as file:
        #     mydoc = minidom.parse(file)
        #     
        #     current = mydoc.getElementsByTagName('current')[0]
        # 
        #     for database in mydoc.getElementsByTagName('database'):
        #         if database.getAttribute('name') == current.getAttribute('name'):
        #             for table in database.getElementsByTagName('tables'):
        #                 for table in table.getElementsByTagName('table'):
        #                     if table.getAttribute('name') == self.name_table:
        #                         fields = table.getElementsByTagName('fields')[0]
        #                         records = table.getElementsByTagName('records')[0]
        #                         
        #                         count_in_fields = 0
        #                         for atribute in fields.getElementsByTagName('field'):
        #                             count_in_fields += 1
        #                             
        #                         for record in records.getElementsByTagName('record'):
        #                             for atribute in record.getElementsByTagName('atribute'):
        #                                 print(atribute.getAttribute('name'))
        #                                 print(atribute.firstChild.data)
        #                                 
        #                                 for x in range(0, count_in_fields):
        #                                     for atribute in fields.getElementsByTagName('field'):
        #                                         if atribute.getAttribute('name') == self.campos[x]:
        #                                             counters += 1
        #                                 
        #                                 if counters != count_in_fields:
        #                                     print("Error: los campos no coinciden")
        #                                     return
        #                                     
        #                                 for x in range(0, count_in_fields):
        #                                     for atribute in fields.getElementsByTagName('field'):
        #                                         if atribute.getAttribute('param') == 'TipoOpciones.PRIMARYKEY':
        #                                             primary_key = atribute.getAttribute('name')
        #                                             for recs in table.getElementsByTagName('records'):
        #                                                 for record in recs.getElementsByTagName('record'):
        #                                                     for atribute in record.getElementsByTagName('atribute'):
        #                                                         if atribute.getAttribute('name') == primary_key:
        #                                                             if atribute.firstChild.data == self.campos[x]:
        #                                                                 print("Error: no se puede actualizar la llave primaria")
        #                                                                 return
        #                                                                 
        #
        
        
