from interprete.extra.symbol import Symbol
from interprete.extra.tipos import TipoDato, TipoSimbolo
from .instruccion import Instruccion
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.declaracion_var import Declaracion
from interprete.instrucciones.bloque import Bloque
from interprete.extra.errores import *

from xml.dom import minidom


class Procedure(Instruccion):
    def __init__(self, text_val:str, id:str, parametros:Declaracion, instrucciones:Bloque, linea, columna):
        super().__init__(text_val, linea, columna)
        self.id = id
        if parametros[0] == None: self.parametros = []            # Arreglo de declaraciones
        else:                     self.parametros = parametros
        self.instrucciones = instrucciones      

    def ejecutar(self, env:Enviroment):

        # Guardar el procedimiento en el XML en la base de datos actual
        # Validar que no exista un procedimiento con el mismo nombre antes de insertar en XML
        with open('backend/ejemplo.txt', 'w', encoding='utf-8') as file:
            file.write(self.text_val)

        return self
        
    
    # Insertar un nuevo simbolo (procedimiento) a la tabla de simbolos
    def guardarEnTablaSimbolos(self,env:Enviroment):
        simbolo = Symbol(TipoSimbolo.PROCEDURE, TipoDato.UNDEFINED, self.id, None, env.ambito, self.parametros, self.instrucciones)
        env.insertar_simbolo(self.id, simbolo)

        # with open('backend/structure.xml', 'r+', encoding='utf-8') as file:
        #     mydoc = minidom.parse(file)
            
        #     current = mydoc.getElementsByTagName('current')[0]
            
        #     for database in mydoc.getElementsByTagName('database'):
        #         if database.getAttribute('name') == current.getAttribute('name'):
        #             for procedure in database.getElementsByTagName('procedures'):
        #                 if procedure.getAttribute('name') == self.id:
        #                     print("El procedimiento ya existe")
        #                     return
                        
        #                 #crear procedimiento
        #                 procedure = mydoc.createElement('procedure')
        #                 procedure.setAttribute('name', self.id)
                        
        #                 procedure.appendChild(mydoc.createTextNode(str(self.text_val)))
                        
        #                 database.appendChild(procedure)
                        
        #                 xml_str = mydoc.toxml(encoding='utf-8').decode('utf-8').replace('\n', '').replace('\t', '')
        #                 formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
        #                 file.seek(0)
        #                 file.truncate()
        #                 file.write(formatted_xml)
                
        #                 print("Table created successfully")

        #                 break
                
        #         else:
        #             print("En la base de datos actual no se puede crear el procedimiento")
        
        
    
    # def ejecutar_proc(self, env:Enviroment):

    #     body_recuperado = 'del xml'
        
        
    #     from analizador.parser import parser

    #     instruccion = parser.parse(body_recuperado.lower())

    #     for instruccion in instruccion:                 
    #         retorno = instruccion.ejecutar(env)