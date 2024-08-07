from ply import lex
from interprete.extra.errores import *

lex_pos_actual = 0

reservadas = {
    'column': 'COLUMN',
    'use': 'USE',
    'create': 'CREATE',
    'data': 'DATA',
    'base': 'BASE',
    'table': 'TABLE',
    'where': 'WHERE',
    'select': 'SELECT',
    'insert': 'INSERT',
    'into': 'INTO',
    'values': 'VALUES',
    'update': 'UPDATE',
    'delete': 'DELETE',
    'drop': 'DROP',
    'truncate': 'TRUNCATE',
    'from': 'FROM',
    'as': 'AS',
    'procedure': 'PROCEDURE',
    'exec': 'EXEC',
    'function': 'FUNCTION',
    'returns': 'RETURNS',
    'return': 'RETURN',
    'begin': 'BEGIN',
    'end': 'END',
    'declare': 'DECLARE',
    'set': 'SET',
    'alter': 'ALTER',
    'add': 'ADD',
    'drop': 'DROP',
    'if': 'IF',
    'else': 'ELSE',
    'then': 'THEN',
    'while': 'WHILE',
    'as': 'AS',
    'between': 'BETWEEN',
    'case': 'CASE',
    'when': 'WHEN',
    
    'null': 'NULL',
    'not': 'NOT',
    'primary': 'PRIMARY',
    'key': 'KEY',
    'reference': 'REFERENCE',
    
    # TIPOS DE DATOS
    'int': 'INT',
    'bit': 'BIT',
    'decimal': 'DECIMAL',
    'date': 'DATE',
    'datetime': 'DATETIME',
    'nchar': 'NCHAR',
    'nvarchar': 'NVARCHAR',
    
    # FUNCIONES DEL SISTEMA
    'concatena': 'CONCATENAR',
    'substraer': 'SUBSTRAER',
    'hoy': 'HOY',
    'contar': 'CONTAR',
    'suma': 'SUMA',
    'cas': 'CAS',

    'println': 'PRINTLN'
}


tokens = [
    'ENTERO',
    'CADENA',
    'FLOAT',
    'SUMAR',
    'RESTAR',
    'DIV',
    'MODULO',
    'MULT',
    'IGUAL',
    'IGUALDAD',
    'DESIGUALDAD',
    'MENOR_IGUAL',
    'MAYOR_IGUAL',
    'MENOR',
    'MAYOR',
    'OR',
    'AND',
    'NEGACION',
    'ID',
    'PARA',
    'PARC',
    'PYC',
    'PUNTO',
    'COMA',
    'ARROBA'
] + list(reservadas.values())

# Caracteres ignorados
t_ignore = ' \t'



# Tokens con regex
t_SUMAR = r'\+'
t_RESTAR = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'%'
t_PYC = r';'
t_PARA = r'\('
t_PARC = r'\)'
t_COMA = r','
t_IGUALDAD = r'=='
t_DESIGUALDAD = r'!='
t_MENOR_IGUAL = r'<='
t_MAYOR_IGUAL = r'>='
t_MENOR = r'<'
t_MAYOR = r'>'
t_IGUAL = r'='
t_OR = r'\|\|'
t_AND = r'&&'
t_NEGACION = r'!'
t_ARROBA = r'@'
t_PUNTO = r'\.'

def t_FLOAT(t):
    r'\d+\.\d+'
    try:
        t.value = t.value
    except ValueError:
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = t.value
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

def t_CADENA(t):
    r'[\'\"][^\'\"]*[\'\"]'
    t.value = t.value[1:-1]
    return t

def t_salto_linea(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_comentario(t):
    r'--.*'
    pass

def t_multicomentarios(t):
    r'[/][*][^*]*[*]+([^/*][^*]*[*]+)*[/]'
    pass

# manejo de errores léxicos
def t_error(t):
    # Agregando a la tabla de erorres
    err = Error(tipo='Léxico', linea=t.lexer.lineno, columna=find_column(t.lexer.lexdata, t), descripcion=f'Caracter no reconocido: {t.value[0]}')
    TablaErrores.addError(err)
    t.lexer.skip(1)


def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos + 1) + 1
    return (token.lexpos - line_start) + 1

def t_eof(t):
    t.lexer.lineno = 0
    print('FIN DEL ARCHIVO', t)


lex.lex()