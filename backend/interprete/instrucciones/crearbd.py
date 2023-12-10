from .instruccion import Instruccion

from xml.dom import minidom

class CrearBD(Instruccion):
    def __init__(self, id, linea:int, columna:int):
        super().__init__(linea, columna)
        self.id = id
    
    def ejecutar(self):
        with open('backend/structure.xml', 'r+', encoding='utf-8') as file:
            mydoc = minidom.parse(file)
            bases = mydoc.getElementsByTagName('database')
            for elem in bases:
                if elem.getAttribute('name') == self.id:
                    print("Database already exists")
                    return

            raiz = mydoc.documentElement
            bd = mydoc.createElement('database')
            bd.setAttribute('name', self.id)
            raiz.appendChild(bd)

            tables = mydoc.createElement('tables')
            bd.appendChild(tables)
            
            views = mydoc.createElement('views')
            bd.appendChild(views)
            
            functions = mydoc.createElement('functions')
            bd.appendChild(functions)
            
            procedures = mydoc.createElement('procedures')
            bd.appendChild(procedures)
            
            xml_str = mydoc.toxml(encoding='utf-8').decode('utf-8').replace('\n', '').replace('\t', '')
            formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
            file.seek(0)
            file.truncate()
            file.write(formatted_xml)
            
            print("Database created successfully")
                