
from interprete.instrucciones.condicion_where import CondicionWhere
from interprete.extra.enviroment import Enviroment
from interprete.instrucciones.instruccion import Instruccion
from xml.dom import minidom
from interprete.expresiones.concatenar import Concatenar
from interprete.extra.retorno import Retorno

class Select(Instruccion):
    def __init__(self, campos:str, tablas:str, condicion_where:CondicionWhere, linea:int, columna:int):
        self.campos = campos
        self.tablas = tablas
        self.condicion_where = condicion_where
        self.linea = linea
        self.columna = columna

    def ejecutar(self, env:Enviroment):
        print('-------- CAMPOS -----------')
        if self.campos == '*': # Seleccionar toda la tabla(s)
            print('*')
            # Buscar las tablas de las que se quiere extraer la informacion
            texto = 'cantidad*tbdetallefactura.price / 1.12 > 100'
            for tabla in self.tablas:
                print(tabla)
                if self.condicion_where != None:
                    nombre_campo = self.condicion_where.id
                    valor_campo:Retorno = self.condicion_where.expresion.ejecutar(env)
                    # Validar que la fila cumpra con la condicion
                    print('Nombre del campo: ', nombre_campo)
                    print('Valor del campo: ',  valor_campo.valor)

                    # campo actual 'cantidad'
                    # campo actual 'tbdetallefactura'

                    # valor_campo_tabla = 4
                    # valor_campo_tabla = 6
                    
                    # texto = sustituir(campo, valor_campo_tabla, text)
                    # texto = '4*6 / 1.12 > 100'
            
            # escribimos en el archivo
            # parseamos el archivo
            # ejecutamos instrucciones
            # Si devuelve True, guardar en una lista


            
        else:
            for tabla in self.tablas:
                for campo in self.campos:
                    print(tabla)
                    if self.condicion_where != None:
                        nombre_campo = campo
                        valor_campo:Retorno = self.condicion_where.expresion.ejecutar(env)
                        # Validar que la fila cumpra con la condicion
                        print('Nombre del campo: ', nombre_campo)
                        print('Valor del campo: ',  valor_campo.valor)

                        #lista_ids = parser.parse_where('id==3 && precio==90')
                        

                    else:
                        pass
        
        print('-------- NOMBRES TABLAS -----------')
        for tabla in self.tablas:
            print(tabla)

