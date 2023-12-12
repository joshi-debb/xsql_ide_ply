from interprete.instrucciones.instruccion import Instruccion
from interprete.instrucciones.asignacion_campo import Campo
from interprete.instrucciones.condicion_where import CondicionWhere
from xml.dom import minidom
from interprete.extra.enviroment import Enviroment

class Update(Instruccion):
    def __init__(self, table_name:str, tupla:Campo, condicion:CondicionWhere, linea:int, columna:int):
        super().__init__(linea, columna)
        self.table_name = table_name
        self.tupla = tupla                 
        self.condicion = condicion
    
    def ejecutar(self, env:Enviroment):  
        with open('backend/structure.xml', 'r+', encoding='utf-8') as file:
            mydoc = minidom.parse(file)
            
            current = mydoc.getElementsByTagName('current')[0]

            #actualizar tabla donde se cumpla la condicion
            for database in mydoc.getElementsByTagName('database'):
                if database.getAttribute('name') == current.getAttribute('name'):
                    for table in database.getElementsByTagName('tables'):
                        for table in table.getElementsByTagName('table'):
                            if table.getAttribute('name') == self.table_name:
                                fields = table.getElementsByTagName('fields')[0]

                                for atribute in fields.getElementsByTagName('field'):
                                    if atribute.getAttribute('name') == self.condicion.id:
                                        for recs in table.getElementsByTagName('records'):
                                            for rc in recs.getElementsByTagName('field'):
                                                for tup in self.tupla:
                                                    if rc.getAttribute('name') == tup.id:
                                                        if rc.getAttribute('param') == 'TipoOpciones.PRIMARYKEY':
                                                            print("Error: No se puede actualizar la llave primaria")
                                                            return
                                                        rc.firstChild.data = tup.expresion.ejecutar(env).valor
        
            xml_str = mydoc.toxml(encoding='utf-8').decode('utf-8').replace('\n', '').replace('\t', '')
            formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
            file.seek(0)
            file.truncate()
            file.write(formatted_xml)
