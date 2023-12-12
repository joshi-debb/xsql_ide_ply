from analizador.parser import parser
from interprete.extra.enviroment import Enviroment
from interprete.extra.errores import TablaErrores
from xml.dom import minidom
import os


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

f = open('backend/entrada2.txt', 'r')
input = f.read()
# print(input)
instrucciones = parser.parse(input.lower())

env = Enviroment(ent_anterior=None, ambito='Global')

# Ejecutando todas las instrucciones
for instruccion in instrucciones:
    instruccion.ejecutar(env)

print("------------ Errores ------------")
for error in TablaErrores.errores:
    print(error.serializar())