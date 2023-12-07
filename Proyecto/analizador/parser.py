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
                  | instrucciones
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
    crear_tb : CREATE TABLE ID PARA PARC 
    '''

# Error sintactico
def p_error(t):
    if t:
        print(f"Error sintáctico en línea {t.lineno}, posición {t.lexpos}: '{t.value}'")
    else:
        print("Error sintáctico: final de entrada inesperado")


# Build the parser
parser = yacc(debug=True)
