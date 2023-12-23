from interprete.extra.ast import *
from interprete.expresiones.tipoChars import TipoChars
from .instruccion import Instruccion
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.declaracion_var import Declaracion
from interprete.instrucciones.bloque import Bloque
from interprete.extra.tipos import *
from interprete.extra.errores import *
from interprete.extra.symbol import Symbol

from xml.dom import minidom

class Function(Instruccion):

    def __init__(self, text_val:str, tipo_ret:TipoDato, id:str, parametros:Instruccion, instrucciones:Bloque, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        if isinstance(tipo_ret, TipoChars): self.tipo_ret = tipo_ret.charTipo
        else:                               self.tipo_ret = tipo_ret
        self.id = id
        if parametros[0] == None: self.parametros = []            # Arreglo de declaraciones
        else:                     self.parametros = parametros
        self.instrucciones = instrucciones
    
    def ejecutar(self, env: Enviroment):
        
        with open('backend/structure.xml', 'r+', encoding='utf-8') as file:
            mydoc = minidom.parse(file)
            
            current = mydoc.getElementsByTagName('current')[0]  
            bases = mydoc.getElementsByTagName('database')
            
            for elem in bases:
                if elem.getAttribute('name') == current.getAttribute('name'):
                    #vreificar si existe la tabla
                    functions = elem.getElementsByTagName('function')
                    for function in functions:
                        if function.getAttribute('name') == self.id:
                            print("La funcion ya existe")
                            return
                    
                    #crear function dentro de la llave functions
                    funcs = elem.getElementsByTagName('functions')[0]

                    ## Crear function
                    fnc = mydoc.createElement('function')
                    fnc.setAttribute('name', self.id)
                    fnc.appendChild(mydoc.createTextNode(str(self.text_val)))
                    funcs.appendChild(fnc)
                    

                    xml_str = mydoc.toxml(encoding='utf-8').decode('utf-8').replace('\n', '').replace('\t', '')
                    formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
                    file.seek(0)
                    file.truncate()
                    file.write(formatted_xml)
            
                    print("Funcion creada exitosamente")

                    break

                else:
                    print("En la base de datos actual no se puede crear la funcion")
        
        # Validar que no exista una función con el mismo nombre antes de insertar en XML en la base de dato en uso.
        
        # Guardar la función en el XML en la base de datos actual.
        
        # Escribir el contenido de la función en el XML
        # with open('backend/ejemplo.txt', 'w', encoding='utf-8') as file:
        #     file.write(self.text_val)
        
        return self     # Este retorno se queda asi
    
    # Insertar un nuevo simbolo (procedimiento) a la tabla de simbolos
    def guardarEnTablaSimbolos(self, env:Enviroment):
        simbolo = Symbol(TipoSimbolo.FUNCTION, self.tipo_ret, self.id, None, env.ambito, self.parametros, self.instrucciones)
        env.insertar_simbolo(self.id, simbolo)
    
    def getTipoRetorno(self):
        return self.tipo_ret

    # if isinstance(tipo_ret, TipoChars): self.tipo_ret = tipo_ret.charTipo
    # else:                               self.tipo_ret = tipo_ret
    # self.id = id
    # if parametros[0] == None: self.parametros = []            # Arreglo de declaraciones
    # else:                     self.parametros = parametros
    # self.instrucciones = instrucciones
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='FUNCTION', hijos=[])
        raiz.addHijo(hijo)
        id = AST.generarId()
        hijo.addHijo(Nodo(id=id, valor=self.id, hijos=[]))
        
        id = AST.generarId()
        hijo1 = Nodo(id=id, valor='RETURN', hijos=[])
        hijo.addHijo(hijo1)
        id = AST.generarId()
        hijo1.addHijo(Nodo(id=id, valor=self.tipo_ret.name, hijos=[]))
        
        if len(self.parametros) != 0:
            id = AST.generarId()
            hijo2 = Nodo(id=id, valor='PARAMETROS', hijos=[])
            hijo.addHijo(hijo2)
            # Parametros (arreglo de declaraciones de variables)
            for parametro in self.parametros:
                parametro.recorrerArbol(hijo2)
        
        # Instrucciones
        self.instrucciones.recorrerArbol(hijo)