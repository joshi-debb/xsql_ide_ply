from interprete.instrucciones.instruccion import Instruccion
from interprete.instrucciones.asignacion_campo import Campo
from interprete.instrucciones.condicion_where import CondicionWhere
from xml.dom import minidom
from interprete.extra.enviroment import Enviroment

class Update(Instruccion):
    def __init__(self, text_val:str, table_name:str, tupla:Campo, condicion:CondicionWhere, linea:int, columna:int):
        super().__init__(text_val, linea, columna)
        self.table_name = table_name
        self.tupla = tupla                 
        self.condicion = condicion
    
    def ejecutar(self, env:Enviroment):
        print('------------------ UPDATE --------------------------')
        print("> Nombre de tabla: ", self.table_name)

        print("> Tupla: (valores a asignar) ")
        for tup in self.tupla:
            print("     Campo: ", tup.id)
            expresion = tup.expresion.ejecutar(env)
            print("     Expresion: ", expresion.valor)

        # Solo acepta condiciones del tipo: WHERE campo = expresion
        print("> Valor de la condicion: ")
        print("     Campo: ", self.condicion.id)
        expresion = self.condicion.expresion.ejecutar(env)
        print("     Expresion: ", expresion.valor)
        print('-----------------------------------------------------')

        



        with open('backend/structure.xml', 'r+', encoding='utf-8') as file:
            mydoc = minidom.parse(file)
            
            current = mydoc.getElementsByTagName('current')[0]

            #actualizar tabla donde se cumpla la condicion
            for database in mydoc.getElementsByTagName('database'):
                if database.getAttribute('name') == current.getAttribute('name'):
                    for table in database.getElementsByTagName('tables'):
                        for table in table.getElementsByTagName('table'):
                            if table.getAttribute('name') == self.table_name:
                                ##encontrar el campo a actualizar
                                ##UPDATE persona SET nombre = 'aaaaaa' WHERE nombre = 'juanito';
                                ##UPDATE self.table_name SET tup.id = tup.expresion.ejecutar(env).valor WHERE self.condicion.id = self.condicion.expresion.ejecutar(env).valor;
                                ###print('UPDATE ' + self.table_name + ' SET ' + tup.id + ' = ' + tup.expresion.ejecutar(env).valor + ' WHERE ' + self.condicion.id + ' = ' + self.condicion.expresion.ejecutar(env).valor + ';')
                                found = 0
                                cont_records = 0
                                for recs in table.getElementsByTagName('records'):
                                    for record in recs.getElementsByTagName('record'):
                                        cont_records += 1
                                        for rc in record.getElementsByTagName('field'):
                                            #print(rc.getAttribute('name'),' =' , rc.firstChild.data)
                                            if rc.getAttribute('name') == self.condicion.id and rc.firstChild.data == self.condicion.expresion.ejecutar(env).valor:
                                                print(rc.getAttribute('name'), '=', self.condicion.id)
                                                print(rc.firstChild.data, 'es?', self.condicion.expresion.ejecutar(env).valor)
                                                found = cont_records
                                                break

                                for rc in  table.getElementsByTagName('records')[0].getElementsByTagName('record')[found-1].getElementsByTagName('field'):
                                    for tup in self.tupla:
                                        if rc.getAttribute('name') == tup.id:
                                            print(rc.getAttribute('name'), '=', tup.id)
                                            rc.firstChild.data = tup.expresion.ejecutar(env).valor
                                            break
     
            xml_str = mydoc.toxml(encoding='utf-8').decode('utf-8').replace('\n', '').replace('\t', '')
            formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
            file.seek(0)
            file.truncate()
            file.write(formatted_xml)
