
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion
from interprete.expresiones.Literal import Literal
from interprete.extra.tipos import TipoDato
from xml.dom import minidom

class Insert(Instruccion):
    def __init__(self, text_val:str, name_table, campos, tupla:Literal, line, column):
        super().__init__(text_val, line, column)
        self.name_table = name_table
        self.campos = campos
        self.tupla = tupla
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
                                
                                fields = table.getElementsByTagName('fields')[0]
                                records = table.getElementsByTagName('records')[0]
                                
                                record = mydoc.createElement('record')
                                records.appendChild(record)
                                
                                # count_in_fields = 0
                                # for atribute in fields.getElementsByTagName('field'):
                                #     count_in_fields += 1
                                    
                                count_from_paser = 0
                                for campo in self.campos:
                                    count_from_paser += 1
                                    
                                # if count_in_fields != count_from_paser:
                                #     print("Error: la cantidad de campos no coincide")
                                #     return

                                # counters = 0
                                # for x in range(0, count_from_paser):
                                #     for atribute in fields.getElementsByTagName('field'):
                                #         if atribute.getAttribute('name') == self.campos[x]:
                                #             counters += 1
                                
                                # if counters != count_in_fields:
                                #     print("Error: los campos no coinciden")
                                #     return
                                    
                                for x in range(0, count_from_paser):
                                    for atribute in fields.getElementsByTagName('field'):                                            
                                        campo = self.campos[x]
                                        if campo == atribute.getAttribute('name'):
                                            val = self.tupla[x]
                                            expr = val.ejecutar(env)
                                            
                                            expr.tipo = atribute.getAttribute('type')

                                            if expr.tipo == atribute.getAttribute('type'):
                                                inrecord = mydoc.createElement('field')
                                                inrecord.setAttribute('name', campo)
                                                inrecord.appendChild(mydoc.createTextNode(str(expr.valor)))
                                                record.appendChild(inrecord)
                                            else:
                                                print("Error: el tipo de dato no coincide")
                                                return

                            
            xml_str = mydoc.toxml(encoding='utf-8').decode('utf-8').replace('\n', '').replace('\t', '')
            formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
            file.seek(0)
            file.truncate()
            file.write(formatted_xml)
            
            print("Insertado correctamente")   
            
        
        