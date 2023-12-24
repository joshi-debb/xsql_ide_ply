from interprete.extra.ast import *
from .instruccion import Instruccion
from interprete.extra.enviroment import Enviroment
from xml.dom import minidom
from interprete.extra.consola import Consola

class CrearBD(Instruccion):
    def __init__(self, text_val:str, id, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.id = id
    
    def ejecutar(self, env:Enviroment):
        with open('backend/structure.xml', 'r+', encoding='utf-8') as file:
            mydoc = minidom.parse(file)
            bases = mydoc.getElementsByTagName('database')
            for elem in bases:
                if elem.getAttribute('name') == self.id:
                    # print("Database already exists")
                    Consola.addConsola('La base de datos ya existe')
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
            
            # print("Database created successfully")
            Consola.addConsola('Base de datos creada exitosamente')
    
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='CREATE DATA BASE', hijos=[])
        raiz.addHijo(hijo)
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor=self.id, hijos=[]))
