from analizador.parser import parser

f = open('backend/entrada.txt', 'r')
input = f.read()
print(input)
parser.parse(input)
