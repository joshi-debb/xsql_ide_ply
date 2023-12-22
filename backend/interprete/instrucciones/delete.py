from interprete.extra.ast import *
from interprete.instrucciones.instruccion import Instruccion
from interprete.instrucciones.asignacion_campo import Campo
from interprete.instrucciones.condicion_where import CondicionWhere
from xml.dom import minidom
from interprete.extra.enviroment import Enviroment

class Delete(Instruccion):
    def __init__(self, text_val:str, table_name:str, condicion:CondicionWhere, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.table_name = table_name
        self.condicion = condicion
    
    def ejecutar(self, env:Enviroment):
        with open('backend/structure.xml', 'r+', encoding='utf-8') as file:
            mydoc = minidom.parse(file)
            
            current = mydoc.getElementsByTagName('current')[0]

            #Eliminar registro donde se cumpla la condicion
            for database in mydoc.getElementsByTagName('database'):
                if database.getAttribute('name') == current.getAttribute('name'):
                    for table in database.getElementsByTagName('tables'):
                        for table in table.getElementsByTagName('table'):
                            if table.getAttribute('name') == self.table_name:
                                fields = table.getElementsByTagName('fields')[0]

                                for atribute in fields.getElementsByTagName('field'):
                                    if atribute.getAttribute('name') == self.condicion.id:
                                        print(atribute.getAttribute('name'), '=', self.condicion.id)
                                        for recs in table.getElementsByTagName('records'):
                                            for record in recs.getElementsByTagName('record'):
                                                for rc in record.getElementsByTagName('field'):
                                                    if rc.getAttribute('name') == self.condicion.id:
                                                        if rc.firstChild.data == self.condicion.expresion.ejecutar(env).valor:
                                                            record.parentNode.removeChild(record)
                                                            
            xml_str = mydoc.toxml(encoding='utf-8').decode('utf-8').replace('\n', '').replace('\t', '')
            formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
            file.seek(0)
            file.truncate()
            file.write(formatted_xml)
                                                            

    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='DELETE', hijos=[])
        raiz.addHijo(hijo)                                    
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor=self.table_name, hijos=[]))                                    
        self.condicion.recorrerArbol(hijo)
        
