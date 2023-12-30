from interprete.extra.ast import *
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion
from xml.dom import minidom
from interprete.extra.consola import Consola

class Truncate(Instruccion):
    def __init__(self, text_val:str, name_table, line, column):
        super().__init__(text_val, line, column)
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
                                Consola.addConsola('Tabla truncada con exito')
                                xml_str = mydoc.toxml(encoding='utf-8').decode('utf-8').replace('\n', '').replace('\t', '')
                                formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
                                file.seek(0)
                                file.truncate()
                                file.write(formatted_xml)
                                return
                    Consola.addConsola('Error: no existe la tabla')
                    return
                Consola.addConsola('Error: En la base de datos actual no existe la tabla')
                return  
    

    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='TRUNCATE', hijos=[])
        raiz.addHijo(hijo)
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor=self.name_table, hijos=[]))