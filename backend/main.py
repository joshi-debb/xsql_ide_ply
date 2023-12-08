from analizador.parser import parser

from xml.dom import minidom
import os

filename = 'backend/structure.xml'

# Verificar si el archivo ya existe
if os.path.exists(filename):
    pass
else:
    # Si no existe, crear la estructura y guardarla en el archivo
    doc = minidom.Document()

    root = doc.createElement('xsqldata')
    doc.appendChild(root)

    with open('backend/structure.xml', 'w', encoding='utf-8') as file:
        doc.writexml(file, indent='\t', addindent='\t', newl='\n')

    print("Structure XML created successfully")

# f = open('backend/entrada.txt', 'r')
f = open('backend/entrada2.txt', 'r')
input = f.read()
# print(input)
instrucciones = parser.parse(input)
# print('Longitud de las intrucciones ', len(instrucciones))
for instruccion in instrucciones:
    instruccion.ejecutar()