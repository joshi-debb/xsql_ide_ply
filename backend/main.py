
from types import NoneType
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from interprete.instrucciones.asignacion_var import AsignacionVar
from interprete.instrucciones.declaracion_var import Declaracion
from interprete.instrucciones.print import Print
from interprete.instrucciones.if_else import IfElse

from interprete.extra.ast import AST
from analizador.parser import parser
from interprete.extra.enviroment import Enviroment
from interprete.extra.errores import TablaErrores, Error
from xml.dom import minidom
import os
from interprete.instrucciones.select import Select
from interprete.extra.consola import Consola
from interprete.extra.generador import Generador

filename = 'backend/structure.xml'

# Verificar si el archivo ya existe
if os.path.exists(filename):
    pass
else:
    with open('backend/structure.xml', 'w', encoding='utf-8') as file:
        mydoc = minidom.Document()
        root = mydoc.createElement('SCHEMAS')
        mydoc.appendChild(root)
        
        root = mydoc.documentElement
        cbd = mydoc.createElement('current')

        cbd.setAttribute('name', 'default')
        root.appendChild(cbd)
        
        xml_str = mydoc.toxml(encoding='utf-8').decode('utf-8').replace('\n', '').replace('\t', '')
        formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
        file.seek(0)
        file.truncate()
        file.write(formatted_xml)

    print("Structure XML created successfully")


# Solo de se puede generar C3D de las siguientes clases (solo las que logramos hacer)
def puedeGenerarC3D(instruccion):
    if isinstance(instruccion, Declaracion) or isinstance(instruccion, AsignacionVar) or isinstance(instruccion, Print) or isinstance(instruccion, IfElse):
        return True
    return False

# url del servidor
base_url = "http://localhost:5000"

# lista auxiliar para la traduccion
lista_traduccion = []

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin": "*"}})

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/datas" , methods=['POST'])
def datas():
    global lista_traduccion
    if request.method == 'POST':
        data = request.data.decode('utf-8')

        instrucciones = parser.parse(data.lower())
        env = Enviroment(ent_anterior=None, ambito='Global')
        try:
            for instruccion in instrucciones:
                instruccion.ejecutar(env)
        except Exception as e:
            print(f"Error inesperado: {e}")
        
        # Guardar la tabla de simbolos antes de limpiar el Enviroment
        # Para que no se dupliquen las declaraciones, asignaciones, etc.
        # Y esto es lo que se va a enviar
        env_serializado = Enviroment.serializarTodosSimbolos()

        # Limpiar el Enviroment 
        Enviroment.cleanEnviroments()
        env = Enviroment(ent_anterior=None, ambito='Global')
        generador = Generador()

        try:   
            for instruccion in instrucciones:
                if puedeGenerarC3D(instruccion):
                    instruccion.ejecutar3d(env, generador)
        except Exception as e:
            print(f"Error inesperado: {e}")
        
        lista_traduccion = generador.generate_main()
        
        ast = AST(instrucciones)
        ast.getAST() 

        tuple = {'ListConsole': Consola.getConsola(), 'ListError': TablaErrores.serializarTBErrores(), 'ListSymbol': env_serializado}
                
        Enviroment.cleanEnviroments()
        TablaErrores.cleanTablaErrores()
        Consola.cleanConsola()
        return jsonify(tuple) 


@app.route("/xml" , methods=['GET'])
def get_xml_datas():
    
    mydoc = minidom.parse('backend/structure.xml')
    current = mydoc.getElementsByTagName('current')[0].getAttribute('name')
    
    current_db = []
    current_db.append(current)
    
    aux = []
    
    cont = 0
    
    for base in mydoc.getElementsByTagName('database'):
        cont += 1
        name, tables, views, procs, funcs = [], [], [], [], []
        json = {
            'db': [],
            'tables': [],
            'views': [],
            'procs': [],
            'funcs': [],
            'current': []
        }
        name.append(base.getAttribute('name'))
        for table in base.getElementsByTagName('table'):
            tables.append(table.getAttribute('name'))
        for view in base.getElementsByTagName('view'):
            views.append(view.getAttribute('name'))
        for proc in base.getElementsByTagName('procedure'):
            procs.append(proc.getAttribute('name'))
        for func in base.getElementsByTagName('function'):
            funcs.append(func.getAttribute('name'))

        json['db'] = name
        json['tables'] = tables
        json['views'] = views
        json['procs'] = procs
        json['funcs'] = funcs
        json['current'] = current_db
        
        aux.append(json)
    
    if cont == 0:
        name, tables, views, procs, funcs = [], [], [], [], []
        json = {
            'db': [],
            'tables': [],
            'views': [],
            'procs': [],
            'funcs': [],
            'current': []
        }
        name.append('sys')
        json['db'] = name
        json['tables'] = tables
        json['views'] = views
        json['procs'] = procs
        json['funcs'] = funcs
        json['current'] = current_db
        aux.append(json)

    return jsonify(aux)


@app.route("/export" , methods=['GET'])
def get_xml_export():
    
    mydoc = minidom.parse('backend/structure.xml')
    current = mydoc.getElementsByTagName('current')[0].getAttribute('name')

    lista_export = []
    
    for base in mydoc.getElementsByTagName('database'):
        if base.getAttribute('name') == current:
            for table in base.getElementsByTagName('tables')[0].getElementsByTagName('table'):
                
                records = table.getElementsByTagName('records')[0]
                for record in records.getElementsByTagName('record'):
                    export = 'INSERT INTO ' + table.getAttribute('name') + ' ('
                    fields = table.getElementsByTagName('fields')[0]
                    for column in fields.getElementsByTagName('field'):
                        export += column.getAttribute('name') + ','
                    export = export[:-1]
                    export += ') VALUES ('
                    for rc in record.getElementsByTagName('field'):
                        export += '\'' + rc.firstChild.data + '\','
                    export = export[:-1]
                    export += ');'                    
                    lista_export.append(export)

    return jsonify(datas = lista_export)


@app.route("/dump" , methods=['GET'])
def get_xml_dump():
    
    mydoc = minidom.parse('backend/structure.xml')
    current = mydoc.getElementsByTagName('current')[0].getAttribute('name')

    lista_dump = []
    
    for base in mydoc.getElementsByTagName('database'):
        if base.getAttribute('name') == current:
            for table in base.getElementsByTagName('tables')[0].getElementsByTagName('table'):
                dump = 'CREATE TABLE ' + table.getAttribute('name') + ' ('
                fields = table.getElementsByTagName('fields')[0]
                for column in fields.getElementsByTagName('field'):
                    dump += column.getAttribute('name') + ' ' + column.getAttribute('type') + ' '
                    if column.getAttribute('param1') != '':
                        dump += column.getAttribute('param1') + ' '
                    if column.getAttribute('param2') != '':
                        dump += column.getAttribute('param2') + ' '
                    dump += ','                  
                dump = dump[:-1]
                dump += ');'
                
                if 'TipoDato.NVARCHAR' in dump:
                    dump = dump.replace('TipoDato.NVARCHAR', 'NVARCHAR(10)')
                if 'TipoDato.INT' in dump:
                    dump = dump.replace('TipoDato.INT', 'INT')
                if 'TipoDato.DECIMAL' in dump:
                    dump = dump.replace('TipoDato.DECIMAL', 'DECIMAL')
                if 'TipoDato.DATE' in dump:
                    dump = dump.replace('TipoDato.DATE', 'DATE')
                if 'TipoDato.BOOLEAN' in dump:
                    dump = dump.replace('TipoDato.BOOLEAN', 'BOOLEAN')
                if 'TipoDato.NCHAR' in dump:
                    dump = dump.replace('TipoDato.NCHAR', 'NCHAR(10)')
                if 'TipoDato.DATETIME' in dump:
                    dump = dump.replace('TipoDato.DATETIME', 'DATETIME')
                if 'TipoDato.BIT' in dump:
                    dump = dump.replace('TipoDato.BIT', 'BIT')
                if 'TipoDato.NULL' in dump:
                    dump = dump.replace('TipoDato.NULL', 'NULL')
                if 'TipoDato.ERROR' in dump:
                    dump = dump.replace('TipoDato.ERROR', 'ERROR')
                if 'TipoOpciones.NOTNULL' in dump:
                    dump = dump.replace('TipoOpciones.NOTNULL', 'NOT NULL')
                if 'TipoOpciones.NULL' in dump:
                    dump = dump.replace('TipoOpciones.NULL', 'NULL')
                if 'TipoOpciones.PRIMARYKEY' in dump:
                    dump = dump.replace('TipoOpciones.PRIMARYKEY', 'PRIMARY KEY')
                if 'TipoOpciones.REFERENCE' in dump:
                    dump = dump.replace('TipoOpciones.REFERENCE', 'REFERENCES')

                dump = dump.replace(' ,', ',').replace(' )', ')')
                
                lista_dump.append(dump)
                
    return jsonify(datas = lista_dump)

@app.route("/traduccion" , methods=['GET'])
def traduccion():
    return jsonify(res = lista_traduccion)

@app.route("/selects" , methods=['GET'])
def selects():
    print(Select.get_tabla())
    return jsonify(res = Select.get_tabla()) 

@app.route('/get_image')
def get_image():
    image_path = 'AST.png'
    return send_file(image_path, mimetype='image/png')

if __name__=='__main__':
    app.run(debug = True, port = 5000)
    
