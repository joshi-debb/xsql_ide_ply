from interprete.extra.ast import *
from interprete.extra.enviroment import Enviroment
from .instruccion import Instruccion
from xml.dom import minidom
from interprete.extra.consola import Consola

class Use(Instruccion):
    def __init__(self, text_val:str, id, line, column):
        super().__init__(text_val, line, column)
        self.id = id
        self.line = line
        self.column = column
        
    def ejecutar(self, env:Enviroment):
        with open('backend/structure.xml', 'r+', encoding='utf-8') as file:
            mydoc = minidom.parse(file)
            current = mydoc.getElementsByTagName('current')[0]
            current.setAttribute('name', self.id)
            
            xml_str = mydoc.toxml(encoding='utf-8').decode('utf-8').replace('\n', '').replace('\t', '')
            formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
            file.seek(0)
            file.truncate()
            file.write(formatted_xml)

        Consola.addConsola("Base de datos actual: " + self.id)
        # print("Current database changed to: ", self.id)
    
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='USE', hijos=[])
        raiz.addHijo(hijo)
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor=self.id, hijos=[]))
