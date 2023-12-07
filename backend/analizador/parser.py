from ply.yacc import yacc
from analizador import lexer

tokens = lexer.tokens

precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULT', 'DIV'),
)

def p_inicio(t):
    '''
    ini : instrucciones
    '''
    t[0] = t[1]
    print('Entrada correcta')

def p_instrucciones(t):
    '''
    instrucciones : instrucciones instruccion
    '''
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t):
    '''
    instrucciones : instruccion
    '''
    t[0] = [t[1]]

def p_instruccion(t):
    '''
    instruccion : crear_db
                | crear_tb
    '''
    t[0] = t[1]

def p_crear_db(t):
    '''
    crear_db : CREATE DATA BASE ID PYC
    '''
    t[0] = t[1]

def p_crear_tabla(t):
    '''
    crear_tb : CREATE TABLE ID PARA atributos PARC
    '''
    t[0] = t[1]

def p_atributos(t):
    '''
    atributos : atributos COMA atributo
              | atributo
    '''
    t[0] = t[1]


def p_atributo(t):
    '''
    atributo : ID tipo atributo_opciones
    '''
    t[0] = t[1]

def p_atributo_opciones(t):
    '''
    atributo_opciones : atributo_opciones atributo_opcion
                      | atributo_opcion
    '''
    t[0] = t[1] 

def p_atributo_opcion(t):
    '''
    atributo_opcion : NOT NULL
        | NULL
        | PRIMARY KEY
    '''
    t[0] = t[1]


def p_tipo(t):
    '''
    tipo : INT
        | BIT
        | DECIMAL
        | DATE
        | DATETIME
        | NCHAR comp_n
        | NVARCHAR comp_n
    '''
    t[0] = t[1]

def p_comp_n(t):
    '''
    comp_n : PARA ENTERO PARC
    '''
    t[0] = t[1]

# Error sintactico
def p_error(t):
    if t:
        print(f"Error sintáctico en línea {t.lineno}, posición {t.lexpos}: '{t.value}'")
    else:
        print("Error sintáctico: final de entrada inesperado")


# Build the parser
parser = yacc(debug=True)
