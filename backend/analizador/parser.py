from ply.yacc import yacc
from analizador import lexer

from interprete.expresiones.Literal import Literal
from interprete.instrucciones.crearbd import CrearBD
from interprete.instrucciones.creartb import CrearTB
from interprete.instrucciones.atributo import Atributo
from interprete.expresiones.tipoChars import TipoChars

from interprete.extra.tipos import *

tokens = lexer.tokens

# precedencia de operadores
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'MENOR', 'MAYOR', 'MENOR_IGUAL', 'MAYOR_IGUAL', 'DESIGUALDAD', 'IGUALDAD'),
    ('left', 'RESTAR', 'SUMAR'),
    ('left', 'MULT', 'DIV', 'MODULO'),
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
    instruccion : crear_db PYC
                | crear_tb PYC
                | cmd_insert PYC
                | cmd_update PYC
                | cmd_delete PYC
                | cmd_select PYC
                | cmd_drop PYC
                | cmd_truncate PYC
                | declaracion_variable
                | crear_procedure
                | ejecutar_procedure
                | crear_funcion
                | cmd_alter
                | expresion
    '''
    t[0] = t[1]

def p_crear_db(t):
    '''
    crear_db : CREATE DATA BASE ID
    '''
    t[0] = CrearBD(t[4], t.lineno(1), t.lexpos(1))

def p_crear_tabla(t):
    '''
    crear_tb : CREATE TABLE ID PARA atributos PARC
    '''
    t[0] = CrearTB(t[3], t[5], t.lineno(1), t.lexpos(1))

# INSERT INTO nombre_tabla (col1, col2) VALUES (val1, val2);
def p_cmd_insert(t):
    '''
    cmd_insert : INSERT INTO ID PARA columnas PARC VALUES PARA argumentos PARC
    '''

# UPDATE nombre_tabla SET asignaciones WHERE condiciones;
def p_cmd_update(t):
    '''
    cmd_update : UPDATE ID SET asignaciones_columnas WHERE expresion
    '''

# DELETE FROM products WHERE price = 10;
def p_cmd_delete(t):
    '''
    cmd_delete : DELETE FROM ID WHERE expresion
    '''

def p_cmd_select(t):
    '''
    cmd_select : SELECT op_select
    '''

# DROP TABLE nombre_tabla;
def p_cmd_drop(t):
    '''
    cmd_drop : DROP TABLE ID
    '''

# TRUNCATE TABLE nombre_tabla;
def p_cmd_truncate(t):
    '''
    cmd_truncate : TRUNCATE TABLE ID
    '''

def p_columnas(t):
    '''
    columnas : columnas COMA columna
             | columna
    '''

def p_columna(t):
    '''
    columna : ID
    '''

def p_atributos(t):
    '''
    atributos : atributos COMA atributo
              | atributo
    '''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[3])
        t[0] = t[1]


def p_atributo(t):
    '''
    atributo : ID tipo atributo_opciones
    '''
    # t[0] = Atributo(nombre, tipo, arreglo de opciones)
    t[0] = Atributo(t[1], t[2], t[3], t.lineno(1), t.lexpos(1))

def p_atributo_opciones(t):
    '''
    atributo_opciones : atributo_opciones atributo_opcion
                      | atributo_opcion
    '''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[2])
        t[0] = t[1]

def p_atributo_opcion(t):
    '''
    atributo_opcion : NOT NULL
    '''
    t[0] = TipoOpciones.NOTNULL

def p_atributo_opcion_null(t):
    '''
    atributo_opcion : NULL
    '''
    t[0] = TipoOpciones.NULL

def p_atributo_opcion_primarykey(t):
    '''
    atributo_opcion : PRIMARY KEY
    '''
    t[0] = TipoOpciones.PRIMARYKEY

# FUNCIONES DEL SISTEMA
def p_op_select(t):
    '''
    op_select : funcion_sistema
              | select_columnas
    '''

def p_select_columnas(t):
    '''
    select_columnas : MULT FROM ID
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

# CAST ( expression AS type )
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

def p_asignaciones_columnas(t):
    '''
    asignaciones_columnas : asignaciones_columnas COMA asignacion_campo
                          | asignacion_campo
    '''

def p_asignacion_campo(t):
    '''
    asignacion_campo : ID IGUAL expresion
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
    argumento : expresion
              | empty
    '''

def p_ejecutar_procedure(t):
    '''
    ejecutar_procedure : EXEC ID argumentos
    '''

def p_cmd_alter(t):
    '''
    cmd_alter : ALTER TABLE ID ADD ID tipo
              | ALTER TABLE ID DROP ID
    '''

# def p_comp_alter(t):
#     '''
#     comp_alter : ADD ID tipo
#                | DROP ID
#     '''

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

def p_expresion_parentesis(t):
    '''
    expresion : PARA expresion PARC
    '''
    t[0] = t[2]

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
    t[0] = Literal(TipoDato.INT, int(t[1]), t.lineno(1), t.lexpos(1))

def p_cadena(t):
    '''
    literal : CADENA
    '''
    t[0] = Literal(TipoDato.NCHAR, t[1], t.lineno(1), t.lexpos(1))

def p_decimal(t):
    '''
    literal : FLOAT
    '''
    t[0] = Literal(TipoDato.DECIMAL, float(t[1]), t.lineno(1), t.lexpos(1))

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
    if(t[1] == 'int'):
        t[0] = TipoDato.INT;
    elif(t[1] == 'bit'):
        t[0] = TipoDato.BIT;
    elif(t[1] == 'decimal'):
        t[0] = TipoDato.DECIMAL;
    elif(t[1] == 'date'):
        t[0] = TipoDato.DATE;
    elif(t[1] == 'datetime'):
        t[0] = TipoDato.DATETIME;
    elif(t[1] == 'nchar'):
        t[0] = TipoChars(TipoDato.NCHAR, t[2]);
    elif(t[1] == 'nvarchar'):
        t[0] = TipoChars(TipoDato.NVARCHAR, t[2]);

def p_comp_n(t):
    '''
    comp_n : PARA literal PARC
    '''
    t[0] = t[2]

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
