from ply.yacc import yacc
from analizador import lexer

from interprete.expresiones.Literal import Literal
from interprete.extra.tipos import *

tokens = lexer.tokens

# precedencia de operadores
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'MENOR', 'MAYOR', 'MENOR_IGUAL', 'MAYOR_IGUAL', 'DESIGUALDAD', 'IGUALDAD'),
    ('left', 'RESTAR', 'SUMAR'),
    ('left', 'MODULO'),
    ('left', 'MULT', 'DIV'),
    #('left', 'AS'),
    #('left', 'PUNTO'),
    ('right', 'NEGACION'),
    ('right', 'UMENOS')
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
                | select
                | declaracion_variable
                | crear_procedure
                | ejecutar_procedure
                | crear_funcion
                | alter
                | expresion
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

# FUNCIONES DEL SISTEMA
def p_funcion(t):
    '''
    select : SELECT funcion_sistema
    '''

def p_funcion_sistema(t):
    '''
    funcion_sistema : concatenar
                    | substraer
                    | hoy
                    | contar
                    | suma
                    | cast
    '''

def p_concatena(t):
    '''
    concatenar : CONCATENAR PARA expresion COMA expresion PARC
    '''

def p_substraer(t):
    '''
    substraer : SUBSTRAER PARA expresion COMA expresion COMA expresion PARC
    '''

def p_hoy(t):
    '''
    hoy : HOY PARA PARC
    '''

def p_contar(t):
    '''
    contar : CONTAR PARA MULT PARC  FROM ID WHERE expresion
    '''

def p_suma(t):
    '''
    suma : SUMA PARA ID PARC FROM ID WHERE expresion
    '''

def p_cast(t):
    '''
    cast : CAST PARA expresion AS tipo PARC
    '''

# DECLARACION DE VARIABLES
def p_declaracion_variable(t):
    '''
    declaracion_variable : declaracion
                         | declaracion_inicializada
    '''

def p_declaracion(t):
    '''
    declaracion : DECLARE ARROBA ID tipo
    '''

def p_declaracion_inicializada(t):
    '''
    declaracion_inicializada : DECLARE ARROBA ID tipo IGUAL expresion
    '''

def p_asignacion_variable(t):
    '''
    asignacion : ARROBA ID IGUAL expresion
    '''

def p_crear_procedure(t):
    '''
    crear_procedure : CREATE PROCEDURE ID PARA parametros PARC AS 
    '''

def p_crear_funcion(t):
    '''
    crear_funcion : CREATE FUNCTION ID PARA parametros PARC RETURNS tipo AS BEGIN RETURN END
    '''

def p_parametros(t):
    '''
    parametros : parametros COMA parametro
               | parametro
    '''

def p_parametro(t):
    '''
    parametro : ARROBA ID tipo
              | empty
    '''

def p_declaracion_parametro(t):
    ''''''

def p_argumentos(t):
    '''
    argumentos : argumentos COMA argumento
               | argumento
    '''

def p_argumento(t):
    '''
    argumento : expresion COMA expresion
              | empty
    '''

def p_ejecutar_procedure(t):
    '''
    ejecutar_procedure : EXEC ID argumentos
    '''

def p_alter(t):
    '''
    alter : ALTER TABLE ID comp_alter
    '''

def p_comp_alter(t):
    '''
    comp_alter : ADD ID tipo
               | DROP ID
    '''

# Valores como tal. Eje. 123, "hola", var.
def p_expresion(t):
    '''
    expresion : aritmetica
              | relacional
              | logica
              | literal
              | ID
    '''
    t[0] = t[1]

def p_expresion_relacional(t):
    '''
    relacional : expresion IGUAL expresion
               | expresion IGUALDAD expresion
               | expresion DESIGUALDAD expresion
               | expresion MENOR expresion
               | expresion MAYOR expresion
               | expresion MENOR_IGUAL expresion
               | expresion MAYOR_IGUAL expresion
    '''

def p_expresion_aritmetica(t):
    '''
    aritmetica : expresion SUMAR expresion
                | expresion RESTAR expresion
                | expresion MULT expresion
                | expresion DIV expresion
                | RESTAR expresion %prec UMENOS
    '''

def p_expresion_logica(t):
    '''
    logica : NEGACION expresion
           | expresion OR expresion
           | expresion AND expresion
    '''

def p_entero(t):
    '''
    literal : ENTERO
    '''
    t[0] = Literal(TipoDato.INT, t[1], t.lineno(1), t.lexpos(1))

def p_cadena(t):
    '''
    literal : CADENA
    '''
    t[0] = Literal(TipoDato.NCHAR, t[1], t.lineno(1), t.lexpos(1))

def p_decimal(t):
    '''
    literal : FLOAT
    '''
    t[0] = Literal(TipoDato.DECIMAL, t[1], t.lineno(1), t.lexpos(1))

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
    comp_n : PARA expresion PARC
    '''
    t[0] = t[1]

def p_empty(t):
    '''
    empty :
    '''

# Error sintactico
def p_error(t):
    if t:
        print(f"Error sintáctico en línea {t.lineno}, posición {t.lexpos}: '{t.value}'")
    else:
        print("Error sintáctico: final de entrada inesperado")


# Build the parser
parser = yacc(debug=True)
