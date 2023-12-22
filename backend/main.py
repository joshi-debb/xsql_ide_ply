from interprete.extra.ast import AST
from analizador.parser import parser
from interprete.extra.enviroment import Enviroment
from interprete.extra.errores import TablaErrores
from xml.dom import minidom
import os
from interprete.instrucciones.select import Select


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

f = open('backend/entrada_real1.txt', 'r')
entrada = f.read()
# print(input)
instrucciones = parser.parse(entrada.lower())

env = Enviroment(ent_anterior=None, ambito='Global')

# Ejecutando todas las instrucciones
# try:
for instruccion in instrucciones:
    instruccion.ejecutar(env)
# except Exception as e:
#    print(f'ERROR al ejecutar las instrucciones')

print('--------selects---------')
print(Select.get_tabla())


print("------------ Errores ------------")
for error in TablaErrores.errores:
    print(error.serializar())
    


# Generando AST
ast = AST(instrucciones)
ast.getAST()
    
# opt = input('Borrar archivo structure.xml? s/n: ')
# if opt == 's':    
#     # Verificar si el archivo existe antes de intentar borrarlo
#     if os.path.exists('backend/structure.xml'):
#         os.remove('backend/structure.xml')
#         print(f"El archivo {'backend/structure.xml'} ha sido borrado con éxito.")
#     else:
#         print(f"El archivo {'backend/structure.xml'} no existe.")