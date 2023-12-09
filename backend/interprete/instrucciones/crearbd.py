from .instruccion import Instruccion

from xml.dom import minidom

class CrearBD(Instruccion):
    
    def __init__(self, id, linea:int, columna:int):
        super().__init__(linea, columna)
        self.id = id
    
    def ejecutar(self):
 
        datas = open('backend/structure.xml', 'r+', encoding='utf-8')
        mydoc = minidom.parse(datas)
        bases = mydoc.getElementsByTagName('database')
        for elem in bases:
            if elem.getAttribute('name') == self.id:
                print("Database already exists")
                return

        raiz = mydoc.documentElement
        bd = mydoc.createElement('database')
        bd.setAttribute('name', self.id)
        raiz.appendChild(bd)
        print("Database created successfully")
    
        with open('backend/structure.xml', 'w', encoding='utf-8') as file:
            mydoc.writexml(file, indent='\t', addindent='\t', newl='\n')
        