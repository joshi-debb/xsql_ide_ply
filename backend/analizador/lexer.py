from ply import lex

lex_pos_actual = 0

reservadas = {
    'create': 'CREATE',
    'data': 'DATA',
    'base': 'BASE',
    'table': 'TABLE',
    'where': 'WHERE',
    
    'null': 'NULL',
    'not': 'NOT',
    'primary': 'PRIMARY',
    'key': 'KEY',
    
    'int': 'INT',
    'bit': 'BIT',
    'decimal': 'DECIMAL',
    'date': 'DATE',
    'datetime': 'DATETIME',
    'nchar': 'NCHAR',
    'nvarchar': 'NVARCHAR',
    
}


tokens = [
    'ENTERO',
    'CADENA',
    'MAS',
    'MENOS',
    'DIV',
    'MULT',
    'ID',
    'PARA',
    'PARC',
    'PYC',
    'COMA'
] + list(reservadas.values())

# Caracteres ignorados
t_ignore = ' \t'

# Tokens con regex
t_MAS = r'\+'
t_MENOS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_PYC = r';'
t_PARA = r'\('
t_PARC = r'\)'
t_COMA = r','


def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

def t_CADENA(t):
    r'\'[^\"]*\''
    return t

def t_salto_linea(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')
    #lex_pos_actual = t.lexpos
    print('Lineno: ', t.lexpos)
    t.lexpos = 0


# Manejo de errores lexicos
def t_error(t):
    print(f"Caracter no reconocido: '{t.value[0]}' en la línea {t.lexer.lineno}, posición {t.lexpos}")
    t.lexer.skip(1)


lex.lex()