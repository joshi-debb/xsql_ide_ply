from analizador.parser import parser

# f = open('backend/entrada.txt', 'r')
f = open('./entrada.txt', 'r')
input = f.read()
# print(input)
instrucciones = parser.parse(input)
# print('Longitud de las intrucciones ', len(instrucciones))
# for instruccion in instrucciones:
#     instruccion.ejecutar()