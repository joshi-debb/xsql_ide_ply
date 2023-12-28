
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

from interprete.extra.ast import AST
from analizador.parser import parser
from interprete.extra.enviroment import Enviroment
from interprete.extra.errores import TablaErrores
from xml.dom import minidom
import os
from interprete.instrucciones.select import Select
from interprete.extra.consola import Consola
from interprete.extra.generador import Generador

# # url del servidor
# base_url = "http://localhost:5000"

# # lista auxiliar para la traduccion
# lista_traduccion = []

# app = Flask(__name__)
# cors = CORS(app, resources={r"/*": {"origin": "*"}})

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# filename = 'backend/structure.xml'

# # Verificar si el archivo ya existe
# if os.path.exists(filename):
#     pass
# else:
#     with open('backend/structure.xml', 'w', encoding='utf-8') as file:
#         mydoc = minidom.Document()
#         root = mydoc.createElement('SCHEMAS')
#         mydoc.appendChild(root)
        
#         root = mydoc.documentElement
#         cbd = mydoc.createElement('current')

#         cbd.setAttribute('name', 'default')
#         root.appendChild(cbd)
        
#         xml_str = mydoc.toxml(encoding='utf-8').decode('utf-8').replace('\n', '').replace('\t', '')
#         formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
#         file.seek(0)
#         file.truncate()
#         file.write(formatted_xml)

#     print("Structure XML created successfully")

# @app.route("/datas" , methods=['POST'])
# def datas():
#     global lista_traduccion
#     if request.method == 'POST':
#         data = request.data.decode('utf-8')
#         print('-----------')
#         print(data);
#         instrucciones = parser.parse(data.lower())
#         env = Enviroment(ent_anterior=None, ambito='Global')
#         for instruccion in instrucciones:
#             instruccion.ejecutar(env)
            
#         generador = Generador()
#         for instruccion in instrucciones:
#             instruccion.ejecutar3d(env, generador)

#         lista_traduccion = generador.generate_main()
        
#         ast = AST(instrucciones)
#         ast.getAST() 
        
#         tuple = {'ListConsole': Consola.getConsola(), 'ListError': TablaErrores.serializarTBErrores(), 'ListSymbol': Enviroment.serializarTodosSimbolos()}
        
#         Enviroment.cleanEnviroments()
#         TablaErrores.cleanTablaErrores()
#         Consola.cleanConsola()
#         return jsonify(tuple)     

# @app.route("/traduccion" , methods=['GET'])
# def traduccion():
#     return jsonify(res = lista_traduccion)

# @app.route("/selects" , methods=['GET'])
# def selects():
#     return jsonify(res = Select.get_tabla()) 

# @app.route('/get_image')
# def get_image():
#     image_path = 'AST.png'
#     return send_file(image_path, mimetype='image/png')

# if __name__=='__main__':
#     app.run(debug = True, port = 5000)
    
    
# SI SE VA A USAR EL SERVIDOR DE FLASK
# DESCOMENTAR EL CODIGO DE ARRIBA Y COMENTAR EL CODIGO DE ABAJO

# SI NO SE VA A USAR EL SERVIDOR DE FLASK
# SE PUEDE USAR ESTE CODIGO PARA EJECUTAR EL ANALIZADOR

f = open('backend/entrada.txt', 'r')
entrada = f.read()
instrucciones = parser.parse(entrada.lower())

# print('--------Creando enviroment---------')
env = Enviroment(ent_anterior=None, ambito='Global')

# print('--------Ejecutando instrucciones---------')
for instruccion in instrucciones:
    instruccion.ejecutar(env)


# print('--------Generando C3D---------')
generador = Generador()
for instruccion in instrucciones:
    instruccion.ejecutar3d(env, generador)

with open('backend/C3D.txt', 'w', encoding='utf-8') as file:
    file.write(generador.generate_main())


# print('--------selects---------')
print(Select.get_tabla())

# print('--------AST---------')
ast = AST(instrucciones)
ast.getAST()    

# print('--------Consola---------')
print(Consola.getConsola())

# print('--------Enviroments---------')
print(Enviroment.serializarTodosSimbolos())

# print("------------ Errores ------------")
print(TablaErrores.serializarTBErrores())
