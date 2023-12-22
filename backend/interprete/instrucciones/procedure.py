from interprete.extra.ast import *
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
        
        with open('backend/structure.xml', 'r+', encoding='utf-8') as file:
            mydoc = minidom.parse(file)
            
            current = mydoc.getElementsByTagName('current')[0]  
            bases = mydoc.getElementsByTagName('database')
            
            for elem in bases:
                if elem.getAttribute('name') == current.getAttribute('name'):
                    #vreificar si existe la tabla
                    procedures = elem.getElementsByTagName('procedure')
                    for procedure in procedures:
                        if procedure.getAttribute('name') == self.id:
                            print("El procedimiento ya existe")
                            return
                    
                    #crear procedure dentro de la llave procedures
                    procs = elem.getElementsByTagName('procedures')[0]

                    ## Crear procedure
                    prc = mydoc.createElement('procedure')
                    prc.setAttribute('name', self.id)
                    prc.appendChild(mydoc.createTextNode(str(self.text_val)))
                    procs.appendChild(prc)
                    

                    xml_str = mydoc.toxml(encoding='utf-8').decode('utf-8').replace('\n', '').replace('\t', '')
                    formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
                    file.seek(0)
                    file.truncate()
                    file.write(formatted_xml)
            
                    print("Procedimiento creado exitosamente")

                    break

                else:
                    print("En la base de datos actual no se puede crear el procedimiento")

        # Validar que no exista un procedimiento con el mismo nombre antes de insertar en XML en la base de dato en uso.
        
        # Guardar el procedimiento en el XML en la base de datos actual.
        
        # Escribir el contenido del procedimiento en el XML
        # with open('backend/ejemplo.txt', 'w', encoding='utf-8') as file:
        #     file.write(self.text_val)

        return self         # Este retorno se queda asi
        
    
    # Insertar un nuevo simbolo (procedimiento) a la tabla de simbolos
    def guardarEnTablaSimbolos(self, env:Enviroment):
        simbolo = Symbol(TipoSimbolo.PROCEDURE, TipoDato.UNDEFINED, self.id, None, env.ambito, self.parametros, self.instrucciones)
        env.insertar_simbolo(self.id, simbolo)

    # self.id = id
    # if parametros[0] == None: self.parametros = []            # Arreglo de declaraciones
    # else:                     self.parametros = parametros
    # self.instrucciones = instrucciones    
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='PROCEDURE', hijos=[])
        raiz.addHijo(hijo)
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor=self.id, hijos=[]))

        id = AST.generarId()
        hijo1 = Nodo(id=id, valor='PAMETROS', hijos=[])
        hijo.addHijo(hijo1)
        # Parametros (arreglo de declaraciones de variables)
        for parametro in self.parametros:
            parametro.recorrerArbol(hijo1)
        
        # Instrucciones
        self.instrucciones.recorrerArbol(hijo)
    