from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion
from xml.dom import minidom

class Truncate(Instruccion):
    def __init__(self, name_table, line, column):
        self.name_table = name_table
        self.line = line
        self.columna = column

    def ejecutar(self, env:Enviroment):
        with open('backend/structure.xml', 'r+', encoding='utf-8') as file:
            mydoc = minidom.parse(file)
            
            current = mydoc.getElementsByTagName('current')[0]
        
            for database in mydoc.getElementsByTagName('database'):
                if database.getAttribute('name') == current.getAttribute('name'):
                    for table in database.getElementsByTagName('tables'):
                        for table in table.getElementsByTagName('table'):
                            if table.getAttribute('name') == self.name_table:
                                records = table.getElementsByTagName('records')[0]
                                for record in records.getElementsByTagName('record'):
                                    record.parentNode.removeChild(record)
                                    print("Tabla truncada")
                                    xml_str = mydoc.toxml(encoding='utf-8').decode('utf-8').replace('\n', '').replace('\t', '')
                                    formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
                                    file.seek(0)
                                    file.truncate()
                                    file.write(formatted_xml)
                                    return
                    print("Error: no existe la tabla")
                    return
                print("Error: En la base de datos actual no existe la tabla")
                return  