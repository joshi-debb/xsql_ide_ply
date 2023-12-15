from interprete.instrucciones.instruccion import Instruccion
from interprete.extra.enviroment import Enviroment

from xml.dom import minidom


class Procedure(Instruccion):
    def __init__(self, text_val, nombre_proc, parametros, instrucciones, line, column):
        Instruccion.__init__(self,None,line,column)
  
        
        self.nombre_proc = 'nombre del procedure'
        self.body = 'instrucciones de procedure'

    def ejecutar(self, env:Enviroment):

        with open('backend/structure.xml', 'r+', encoding='utf-8') as file:
            mydoc = minidom.parse(file)
            
            current = mydoc.getElementsByTagName('current')[0]
            
            for database in mydoc.getElementsByTagName('database'):
                if database.getAttribute('name') == current.getAttribute('name'):
                    for procedure in database.getElementsByTagName('procedures'):
                        if procedure.getAttribute('name') == self.nombre_proc:
                            print("El procedimiento ya existe")
                            return
                        
                        #crear procedimiento
                        procedure = mydoc.createElement('procedure')
                        procedure.setAttribute('name', self.nombre_proc)
                        
                        procedure.appendChild(mydoc.createTextNode(self.body))
                        
                        database.appendChild(procedure)
                        
                        xml_str = mydoc.toxml(encoding='utf-8').decode('utf-8').replace('\n', '').replace('\t', '')
                        formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
                        file.seek(0)
                        file.truncate()
                        file.write(formatted_xml)
                
                        print("Table created successfully")

                        break
                
                else:
                    print("En la base de datos actual no se puede crear el procedimiento")
        
        
    
    # def ejecutar_proc(self, env:Enviroment):

    #     body_recuperado = 'del xml'
        
        
    #     from analizador.parser import parser

    #     instruccion = parser.parse(body_recuperado.lower())

    #     for instruccion in instruccion:                 
    #         retorno = instruccion.ejecutar(env)