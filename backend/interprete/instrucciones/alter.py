
from interprete.instrucciones.instruccion import Instruccion
from interprete.extra.tipos import TipoDato
from interprete.expresiones.tipoChars import TipoChars


from xml.dom import minidom
from interprete.extra.enviroment import Enviroment

class AlterADD(Instruccion):
    def __init__(self, name_table, campo, tipo:TipoDato , linea:int, columna:int):
        self.name_table = name_table
        self.campo = campo
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        
    def ejecutar(self, env:Enviroment):
        with open('backend/structure.xml', 'r+', encoding='utf-8') as file:
            mydoc = minidom.parse(file)
            
            current = mydoc.getElementsByTagName('current')[0]
        
            for database in mydoc.getElementsByTagName('database'):
                if database.getAttribute('name') == current.getAttribute('name'):
                    for table in database.getElementsByTagName('tables'):
                        for table in table.getElementsByTagName('table'):
                            if table.getAttribute('name') == self.name_table:
                                for field in table.getElementsByTagName('fields'):
                                    for fl in field.getElementsByTagName('field'):
                                        if fl.getAttribute('name') == self.campo:
                                            print("Error: El campo ya existe")
                                            return

                                nfield = mydoc.createElement('field')
                                nfield.setAttribute('name', self.campo)
                                if isinstance(self.tipo, TipoChars):
                                    nfield.setAttribute('type', str(self.tipo.charTipo))
                                else:
                                    nfield.setAttribute('type', str(self.tipo))
                                
                                nfield.setAttribute('param', 'TipoOpciones.NOTNULL')

                                field.appendChild(nfield)
            
            xml_str = mydoc.toxml(encoding='utf-8').decode('utf-8').replace('\n', '').replace('\t', '')
            formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
            file.seek(0)
            file.truncate()
            file.write(formatted_xml)
            print("Campo agregado")
        
        
    

class AlterDROP(Instruccion):
    def __init__(self, name_table, campo, line, column):
        self.name_table = name_table
        self.campo = campo
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
                                for field in table.getElementsByTagName('fields'):
                                    for fl in field.getElementsByTagName('field'):
                                        print(fl.getAttribute('name') == self.campo)
                                        if fl.getAttribute('name') == self.campo:
                                            if fl.getAttribute('param') == 'TipoOpciones.PRIMARYKEY':
                                                print("Error: No se puede eliminar el campo porque es llave primaria")
                                                return
                                            ## Eliminar campo
                                            field.removeChild(fl)
                                            break

            xml_str = mydoc.toxml(encoding='utf-8').decode('utf-8').replace('\n', '').replace('\t', '')
            formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
            file.seek(0)
            file.truncate()
            file.write(formatted_xml)
            print("Campo Eliminado")