
from interprete.instrucciones.condicion_where import CondicionWhere
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion
from xml.dom import minidom
from interprete.expresiones.concatenar import Concatenar
from interprete.extra.retorno import Retorno



class Select(Instruccion):
    def __init__(self, text_val:str, campos:str, tablas:str, condicion_where:CondicionWhere, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.campos = campos
        self.tablas = tablas
        self.condicion_where = condicion_where
        self.linea = linea
        self.columna = columna

    def ejecutar(self, env:Enviroment):

        if self.condicion_where != None:
            print('La condicion where es: ', self.condicion_where.text_val)

            from analizador.parser import parser

            # instruccion = parser.parse(self.condicion_where.text_val.lower())
            print('La condicion where es: ', self.condicion_where.text_val.lower())

            # instruccion = parser.parse('SELECT nombre FROM persona WHERE edad > 0;'.lower())

            # for instruccion in instruccion:                 
            #     retorno = instruccion.ejecutar(env)

            #     if retorno.valor == True:
            #         print("La condicion where es verdadera")
    

        # datas = open('backend/structure.xml', 'r+', encoding='utf-8')

        # mydoc = minidom.parse(datas)
        
        # current = mydoc.getElementsByTagName('current')[0]
    
        # for database in mydoc.getElementsByTagName('database'):
        #     if database.getAttribute('name') == current.getAttribute('name'):                    
        #         for table in database.getElementsByTagName('tables'):
        #             for table in table.getElementsByTagName('table'):

        #                 if self.campos == '*':
        #                     for tabla in self.tablas:
        #                         if table.getAttribute('name') == tabla:
        #                             fields = table.getElementsByTagName('fields')[0]
        #                             records = table.getElementsByTagName('records')[0]
        #                             print('-------- CAMPOS {} -----------'.format(tabla))
        #                             for field in fields.getElementsByTagName('field'):
        #                                 print(field.getAttribute('name'))
        #                             for record in records.getElementsByTagName('record'):
        #                                 print('-------- REGISTRO -----------')
        #                                 for data in record.getElementsByTagName('field'):
        #                                     print(data.firstChild.data)
        #                 else:

        #                     for tabla in self.tablas:
        #                         if table.getAttribute('name') == tabla:
        #                             fields = table.getElementsByTagName('fields')[0]
        #                             records = table.getElementsByTagName('records')[0]
        #                             nombre_campo = ''
        #                             print('-------- CAMPOS {} -----------'.format(tabla))
        #                             for field in fields.getElementsByTagName('field'):
        #                                 for campo in self.campos:
        #                                     if self.condicion_where != None:
        #                                         print(field.getAttribute('name'))
        #                                         nombre_campo = campo
        #                                         valor_campo:Retorno = self.condicion_where.expresion.ejecutar(env)
        #                                         # Validar que la fila cumpra con la condicion
        #                                         # print('Nombre del campo: ', nombre_campo)
        #                                         # print('Valor del campo: ',  valor_campo.valor)
        #                                         # print(field.getAttribute('name'))
        #                                         for record in records.getElementsByTagName('record'):
        #                                             print('-------- REGISTRO -----------')
        #                                             for data in record.getElementsByTagName('field'):
        #                                                 # print(data.getAttribute('name'), '==', nombre_campo, '&&', data.firstChild.data, '==', valor_campo.valor)
        #                                                 #print(str(data.firstChild.data), '==', valor_campo.valor)
        #                                                 if str(data.firstChild.data) == valor_campo.valor:
        #                                                     print('a',data.getAttribute('name'))
        #                                                     print(data.firstChild.data)
                                            
        #                                     else:
        #                                         if field.getAttribute('name') == campo:
        #                                             print(field.getAttribute('name'))
        #                                             for record in records.getElementsByTagName('record'):
        #                                                 print('-------- REGISTRO -----------')
        #                                                 for data in record.getElementsByTagName('field'):
        #                                                     if data.getAttribute('name') == campo:
        #                                                         print(data.firstChild.data)          
                                    