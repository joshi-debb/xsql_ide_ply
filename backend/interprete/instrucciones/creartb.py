from .instruccion import Instruccion
from .atributo import Atributo
from interprete.extra.tipos import *
from interprete.expresiones.tipoChars import TipoChars

from xml.dom import minidom

class CrearTB(Instruccion):
    def __init__(self, id, atributos:Atributo , linea:int, columna:int):
        super().__init__(linea, columna)
        self.id = id
        self.atributos = atributos
    
    def ejecutar(self):
        
        current_database = 'productos'
       
        datas = open('backend/structure.xml', 'r+', encoding='utf-8')
        mydoc = minidom.parse(datas)
        bases = mydoc.getElementsByTagName('database')
        for elem in bases:
            if elem.getAttribute('name') == current_database:
                # ##vreificar si existe la tabla
                # tables = elem.getElementsByTagName('table')
                # for table in tables:
                #     if table.getAttribute('name') == self.id:
                #         print("La tabla ya existe")
                #         return
                
                ## Crear tabla
                table = mydoc.createElement('table')
                table.setAttribute('name', self.id)
                elem.appendChild(table)
                
                ## Crear atributos
                for atributo in self.atributos:
                    attr = mydoc.createElement('atribute')
                    attr.setAttribute('value', atributo.id)
                    if isinstance(atributo.tipo, TipoChars):
                        attr.setAttribute('type', str(atributo.tipo.charTipo))
                    else:
                        attr.setAttribute('type', str(atributo.tipo))
                    
                    ## Crear parametros
                    for parametro in atributo.parametros:
                        attr.setAttribute('param', str(parametro))
                        
                    table.appendChild(attr)
            
                with open('backend/structure.xml', 'w', encoding='utf-8') as file:
                    mydoc.writexml(file, indent='\t', addindent='\t', newl='\n')
                print("Table created successfully")
                
            else:
                print("La base de datos no existe")
                
    
    
            