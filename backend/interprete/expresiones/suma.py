from interprete.expresiones.acceso import Acceso
from .Expresion import Expresion
from interprete.extra.tipos import TipoAritmetica, TipoDato
from interprete.extra.retorno import Retorno
from interprete.instrucciones.condicion_where import CondicionWhere
from interprete.extra.enviroment import Enviroment

from xml.dom import minidom

class Suma(Expresion):
    
    def __init__(self, text_val:str, campos:str, tablas:str, condicion_where:CondicionWhere, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.campos = campos
        self.tablas = tablas
        self.condicion_where = condicion_where
        self.counter = 0
        self.aux = ''
    
    def get_valor(self):
        return self.aux
    
    def set_valor(self, aux):
        self.aux = aux

    def ejecutar(self, env:Enviroment):        
        resultado = Retorno(tipo=TipoDato.INT, valor=0)

        if self.condicion_where != None:
            self.select_where(env)
        else:
            print('Suma no admite sin where')
            return
        
        # Cuando se obtenga la suma, modificar la variable resultado con el con el total
        resultado.valor = self.counter
        # print('RESULTADO: ', resultado.valor)

        return resultado
    

    def select_where(self, env:Enviroment):
        from analizador.parser import parser
        
        datas = open('backend/structure.xml', 'r+', encoding='utf-8')
        mydoc = minidom.parse(datas)
            
        current = mydoc.getElementsByTagName('current')[0]

        for database in mydoc.getElementsByTagName('database'):
            if database.getAttribute('name') == current.getAttribute('name'):
                for table in database.getElementsByTagName('tables'):
                    for table in table.getElementsByTagName('table'):
                        for tabla in self.tablas:
                            if table.getAttribute('name') == tabla:
                                cont_records = 0
                                for recs in table.getElementsByTagName('records'):
                                    for record in recs.getElementsByTagName('record'):
                                        cont_records += 1
                                        
                                        self.set_valor(self.condicion_where.text_val.replace('\'',''))
                                        
                                        for rc in record.getElementsByTagName('field'):
                                            if rc.getAttribute('name') in self.condicion_where.text_val:
                                                if self.is_integer(rc.firstChild.data) or self.is_flot(rc.firstChild.data):
                                                    self.set_valor(self.get_valor().replace(rc.getAttribute('name'),rc.firstChild.data))
                                                else:
                                                    print('No se puede sumar campos no numericos')
                                                    return
                                        self.aux += ';'
                                        expresion = parser.parse(self.aux.lower())

                                        retorno:Retorno = expresion[0].ejecutar(env)
                                        if retorno.valor == True:
                                            self.look_in_pos(cont_records-1)

    def look_in_pos(self, pos:int):

        datas = open('backend/structure.xml', 'r+', encoding='utf-8')

        mydoc = minidom.parse(datas)
                
        current = mydoc.getElementsByTagName('current')[0]

        for database in mydoc.getElementsByTagName('database'):
            if database.getAttribute('name') == current.getAttribute('name'):
                for table in database.getElementsByTagName('tables'):
                    for table in table.getElementsByTagName('table'):
                            for tabla in self.tablas:
                                if table.getAttribute('name') == tabla:
                                    print('-------- CAMPOS {} -----------'.format(tabla))
                                    for campo in self.campos:
                                        print(campo)
                                    
                                    print('-------- SUMA -----------')
                                    for rc in  table.getElementsByTagName('records')[0].getElementsByTagName('record')[pos].getElementsByTagName('field'):
                                        for campo in self.campos:
                                            if rc.getAttribute('name') == campo:
                                                self.counter += int(rc.firstChild.data)


    def is_integer(self,cadena):
        return cadena.isdigit()

    def is_flot(self,cadena):
        try:
            float_cadena = float(cadena)
            return True
        except ValueError:
            return False                       