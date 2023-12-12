from pickle import NONE
from ply.yacc import yacc
from analizador import lexer

from interprete.expresiones.Literal import Literal
from interprete.expresiones.aritmetica import Aritmetica
from interprete.expresiones.logica import Logica
from interprete.expresiones.relacional import Relacional
from interprete.expresiones.concatenar import Concatenar
from interprete.expresiones.substraer import Substraer
from interprete.expresiones.hoy import Hoy
from interprete.expresiones.suma import Suma
from interprete.expresiones.contar import Contar
from interprete.instrucciones.crearbd import CrearBD
from interprete.instrucciones.creartb import CrearTB
from interprete.instrucciones.atributo import Atributo
from interprete.expresiones.tipoChars import TipoChars
from interprete.instrucciones.use import Use
from interprete.instrucciones.println import Println
from interprete.instrucciones.insert import Insert
from interprete.instrucciones.update import Update
from interprete.instrucciones.delete import Delete
from interprete.instrucciones.asignacion_campo import Campo
from interprete.instrucciones.condicion_where import CondicionWhere
from interprete.instrucciones.drop import Drop
from interprete.instrucciones.truncate import Truncate
from interprete.instrucciones.alter import AlterADD, AlterDROP
from interprete.instrucciones.declaracion_var import Declaracion
from interprete.expresiones.acceso import Acceso
from interprete.instrucciones.asignacion_var import AsignacionVar
from interprete.instrucciones.select import Select


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
                | declaracion_variable PYC
                | asignacion_variable PYC
                | crear_procedure
                | ejecutar_procedure
                | crear_funcion
                | cmd_alter PYC
                | expresion
                | use_db PYC
                | println PYC
    '''
    t[0] = t[1]

def p_println(t):
    '''
    println : PRINTLN PARA expresion PARC
    '''
    t[0] = Println(argumento=t[3], linea=t.lineno(1), columna=t.lexpos(1))

def p_crear_db(t):
    '''
    crear_db : CREATE DATA BASE ID
    '''
    t[0] = CrearBD(t[4], t.lineno(1), t.lexpos(1))

def p_use_db(t):
    '''
    use_db : USE ID
    '''
    t[0] = Use(t[2], t.lineno(1), t.lexpos(1))

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
    t[0] = Insert(t[3], t[5], t[9], t.lineno(1), t.lexpos(1))

# UPDATE nombre_tabla SET asignaciones WHERE condiciones;
def p_cmd_update(t):
    '''
    cmd_update : UPDATE ID SET campos WHERE condicion_where
    '''
    t[0] = Update(t[2], t[4], t[6], t.lineno(1), t.lexpos(1))

# DELETE FROM products WHERE price = 10;
def p_cmd_delete(t):
    '''
    cmd_delete : DELETE FROM ID WHERE condicion_where
    '''
    t[0] = Delete(t[3], t[5], t.lineno(1), t.lexpos(1))


def p_cmd_select(t):
    '''
    cmd_select : SELECT op_select
    '''
    t[0] = Select(t[2], t.lineno(1), t.lexpos(1))

# DROP TABLE nombre_tabla;
def p_cmd_drop(t):
    '''
    cmd_drop : DROP TABLE ID
    '''
    t[0] = Drop(t[3], t.lineno(1), t.lexpos(1))

# TRUNCATE TABLE nombre_tabla;
def p_cmd_truncate(t):
    '''
    cmd_truncate : TRUNCATE TABLE ID
    '''
    t[0] = Truncate(t[3], t.lineno(1), t.lexpos(1))

def p_condicion_where(t):
    '''
    condicion_where : ID IGUAL expresion
    '''
    t[0] = CondicionWhere(t[1], t[3], linea=t.lineno(1), columna=t.lexpos(1))

def p_columnas(t):
    '''
    columnas : columnas COMA columna
             | columna
    '''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[3])
        t[0] = t[1]

def p_columna(t):
    '''
    columna : ID
    '''
    t[0] = t[1]

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
    
def p_atributo_opcion_references(t):
    '''
    atributo_opcion : REFERENCES
    '''
    t[0] = TipoOpciones.REFERENCES

# def p_atributo_opcion_references_id(t):
#     '''
#     atributo_opcion : ID PARA ID  PARC
#     '''


# FUNCIONES DEL SISTEMA
def p_op_select(t):
    '''
    op_select : funcion_sistema
              | select_columnas
    '''
    t[0] = t[1]

def p_select_columnas(t):
    '''
    select_columnas : MULT FROM ID
    '''
    t[0] = t[3]


def p_funcion_sistema(t):
    '''
    funcion_sistema : concatenar
                    | substraer
                    | hoy
                    | contar
                    | suma
                    | cast
    '''
    t[0] = t[1]

def p_concatena(t):
    '''
    concatenar : CONCATENAR PARA expresion COMA expresion PARC
    '''
    t[0] = Concatenar(t[3], t[5], t.lineno(1), t.lexpos(1))

def p_substraer(t):
    '''
    substraer : SUBSTRAER PARA expresion COMA expresion COMA expresion PARC
    '''
    t[0] = Substraer(t[3], t[5], t[7], t.lineno(1), t.lexpos(1))

def p_hoy(t):
    '''
    hoy : HOY PARA PARC
    '''
    t[0] = Hoy(t.lineno(1), t.lexpos(1))

def p_contar(t):
    '''
    contar : CONTAR PARA MULT PARC  FROM ID WHERE condicion_where
    '''
    t[0] = Contar(t[6], t[8], t.lineno(1), t.lexpos(1))

def p_suma(t):
    '''
    suma : SUMA PARA expresion PARC FROM ID WHERE condicion_where
    '''
    t[0] = Suma(t[3], t[6], t[8], t.lineno(1), t.lexpos(1))
    print(t[3])

# CAST ( expression AS type )
def p_cast(t):
    '''
    cast : CAST PARA expresion AS tipo PARC
    '''

# DECLARACION DE VARIABLES
def p_declaracion_variable(t):
    '''
    declaracion_variable : declaracion
    '''
    t[0] = t[1]

def p_declaracion(t):
    '''
    declaracion : DECLARE ARROBA ID tipo
    '''
    t[0] = Declaracion(t[3], t[4], t.lineno(1), t.lexpos(1))

def p_declaracion_inicializada(t):
    '''
    declaracion_inicializada : DECLARE ARROBA ID tipo IGUAL expresion
    '''

def p_asignacion_variable(t):
    '''
    asignacion_variable : SET ARROBA ID IGUAL expresion
    '''
    t[0] = AsignacionVar(t[3], t[5], t.lineno(1), t.lexpos(1))

def p_asignaciones_columnas(t):
    '''
    campos : campos COMA campo
           | campo
    '''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[3])
        t[0] = t[1]

def p_asignacion_campo(t):
    '''
    campo : ID IGUAL expresion
    '''
    t[0] = Campo(t[1], t[3], linea=t.lineno(1), columna=t.lexpos(1))

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

def p_argumentos(t):
    '''
    argumentos : argumentos COMA argumento
               | argumento
    '''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[3])
        t[0] = t[1]

def p_argumento(t):
    '''
    argumento : expresion
              | empty
    '''
    t[0] = t[1]

def p_ejecutar_procedure(t):
    '''
    ejecutar_procedure : EXEC ID argumentos
    '''
    t[0] = t[3]

def p_cmd_alter(t):
    '''
    cmd_alter : ALTER TABLE ID ADD cmd_alter_comp tipo
    '''
    t[0] = AlterADD(t[3], t[5], t[6], t.lineno(1), t.lexpos(1))

def p_cmd_alter_drop(t):
    '''
    cmd_alter : ALTER TABLE ID DROP cmd_alter_comp
    '''
    t[0] = AlterDROP(t[3], t[5], t.lineno(1), t.lexpos(1))


def p_cmd_alter_comp(t):
    '''
    cmd_alter_comp : COLUMN ID
                    | ID
    '''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = t[2]



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
    '''
    t[0] = t[1]

def p_expresion_parentesis(t):
    '''
    expresion : PARA expresion PARC
    '''
    t[0] = t[2]

def p_acceso_var(t):
    '''
    expresion : ARROBA ID
    '''
    t[0] = Acceso(t[2], linea=t.lineno(1), columna=t.lexpos(1))

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
    if t[2] == '==':
        t[0] = Relacional(op1=t[1], operador=TipoRelacional.IGUALDAD, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))
    elif t[2] == '!=':
        t[0] = Relacional(op1=t[1], operador=TipoRelacional.DESIGUALDAD, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))
    elif t[2] == '<':
        t[0] = Relacional(op1=t[1], operador=TipoRelacional.MENOR, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))
    elif t[2] == '>':
        t[0] = Relacional(op1=t[1], operador=TipoRelacional.MAYOR, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))
    elif t[2] == '<=':
        t[0] = Relacional(op1=t[1], operador=TipoRelacional.MENOR_IGUAL, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))
    elif t[2] == '>=':
        t[0] = Relacional(op1=t[1], operador=TipoRelacional.MAYOR_IGUAL, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))

def p_expresion_aritmetica(t):
    '''
    aritmetica : expresion SUMAR expresion
                | expresion RESTAR expresion
                | expresion MULT expresion
                | expresion DIV expresion
    '''
    if t[2] == '+':
        t[0] = Aritmetica(op1=t[1], operador=TipoAritmetica.SUMA, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))
    elif t[2] == '-':
        t[0] = Aritmetica(op1=t[1], operador=TipoAritmetica.RESTA, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))
    elif t[2] == '*':
        t[0] = Aritmetica(op1=t[1], operador=TipoAritmetica.MULTIPLICACION, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))
    elif t[2] == '/':
        t[0] = Aritmetica(op1=t[1], operador=TipoAritmetica.DIVISION, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))

def p_expresion_unaria(t):
    '''
    aritmetica : RESTAR expresion %prec UMENOS
    '''
    t[0] = Aritmetica(op1=t[2], operador=TipoAritmetica.UNARIO, op2=Literal(TipoDato.UNDEFINED, None, t.lineno(1), t.lexpos(1)), linea=t.lineno(1), columna=t.lexpos(1))

def p_expresion_logica(t):
    '''
    logica : NEGACION expresion
           | expresion OR expresion
           | expresion AND expresion
    '''
    if len(t) == 3:
        t[0] = Logica(op1=t[2], operador=TipoLogico.NOT, op2=Literal(TipoDato.BOOL, False, t.lineno(1), t.lexpos(1)), linea=t.lineno(1), columna=0)
    elif t[2] == '||':
        t[0] = Logica(op1=t[1], operador=TipoLogico.OR, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))
    elif t[2] == '&&':
        t[0] = Logica(op1=t[1], operador=TipoLogico.AND, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))

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
    t[0] = None

# Error sintactico
def p_error(t):
    if t:
        print(f"Error sintáctico en línea {t.lineno}, posición {t.lexpos}: '{t.value}'")
    else:
        print("Error sintáctico: final de entrada inesperado")


# Build the parser
parser = yacc(debug=True)
