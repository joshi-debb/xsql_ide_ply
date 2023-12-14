from .instruccion import Instruccion
from .atributo import Atributo
from interprete.extra.tipos import *
from interprete.expresiones.tipoChars import TipoChars
from interprete.instrucciones.reference import Reference
from interprete.extra.enviroment import Enviroment

from xml.dom import minidom

class CrearTB(Instruccion):
    def __init__(self, text_val:str, id, atributos:Atributo , linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.id = id
        self.atributos = atributos
    
    def ejecutar(self, env:Enviroment):
        with open('backend/structure.xml', 'r+', encoding='utf-8') as file:
            mydoc = minidom.parse(file)
            
            current = mydoc.getElementsByTagName('current')[0]  
            bases = mydoc.getElementsByTagName('database')
            
            for elem in bases:
                if elem.getAttribute('name') == current.getAttribute('name'):
                    #vreificar si existe la tabla
                    tables = elem.getElementsByTagName('table')
                    for table in tables:
                        if table.getAttribute('name') == self.id:
                            print("La tabla ya existe")
                            return
                    
                    #crear tabla dentro de la llave tables
                    tablita = elem.getElementsByTagName('tables')[0]

                    ## Crear tabla
                    table = mydoc.createElement('table')
                    table.setAttribute('name', self.id)
                    tablita.appendChild(table)
                    
                    fields = mydoc.createElement('fields')
                    table.appendChild(fields)
                    
                    records = mydoc.createElement('records')
                    table.appendChild(records)
                    
                    ## Crear atributos
                    for atributo in self.atributos:
                        field = mydoc.createElement('field')
                        field.setAttribute('name', atributo.id)
                        if isinstance(atributo.tipo, TipoChars):
                            field.setAttribute('type', str(atributo.tipo.charTipo))
                        else:
                            field.setAttribute('type', str(atributo.tipo))
                        
                        cont = 0
                        ## Crear parametros
                        for parametro in atributo.parametros:
                            if isinstance(parametro, Reference):
                                if self.check_referece(parametro.name_table,parametro.atributo_referenciado) == False:
                                    print("No existe la referencia")
                                    return
                                else:
                                    field.setAttribute('table', str(parametro.name_table))
                                    field.setAttribute('field', str(parametro.atributo_referenciado))
                            else:
                                cont += 1
                                field.setAttribute('param{}'.format(cont), str(parametro))
                            
                            
                        fields.appendChild(field)

                    xml_str = mydoc.toxml(encoding='utf-8').decode('utf-8').replace('\n', '').replace('\t', '')
                    formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
                    file.seek(0)
                    file.truncate()
                    file.write(formatted_xml)
            
                    print("Table created successfully")

                    break

                else:
                    print("En la base de datos actual no se puede crear la tabla")
            
        

    def check_referece(self, name_table, atributo_referenciado) -> bool:
        with open('backend/structure.xml', 'r+', encoding='utf-8') as file:
            mydoc = minidom.parse(file)
            
            bases = mydoc.getElementsByTagName('database')
            
            for elem in bases:
                    #vreificar si existe la tabla
                    tables = elem.getElementsByTagName('table')
                    for table in tables:
                        if table.getAttribute('name') == name_table:
                            fields = table.getElementsByTagName('fields')[0]

                            for atribute in fields.getElementsByTagName('field'):
                                if atribute.getAttribute('param1') == 'TipoOpciones.PRIMARYKEY' or atribute.getAttribute('param2') == 'TipoOpciones.PRIMARYKEY' and atribute.getAttribute('name') == atributo_referenciado:
                                    return True
  
        return False
    
    
            