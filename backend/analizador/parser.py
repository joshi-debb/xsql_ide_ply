from ply.yacc import yacc
from analizador import lexer

from interprete.expresiones.when import When
from interprete.instrucciones.instruccion import Instruccion
from interprete.instrucciones.argumento import Argumento
from interprete.expresiones.Expresion import Expresion
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
from interprete.instrucciones.print import Print
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
from interprete.instrucciones.if_else import IfElse
from interprete.instrucciones.bloque import Bloque
from interprete.instrucciones.reference import Reference
from  interprete.instrucciones.else_if import ElseIf
from interprete.instrucciones.between import Between
from interprete.instrucciones._while import While
from interprete.extra.errores import *
from interprete.expresiones.cas import Cas
from interprete.instrucciones.procedure import Procedure
from interprete.expresiones._return import Return
from interprete.instrucciones.function import Function
from interprete.instrucciones.exec import Exec
from interprete.instrucciones.llamada_funcion import LlamadaFnc
from interprete.expresiones.case import Case
from interprete.expresiones.ternario import OpTernario
from interprete.instrucciones.acceso_tabla import AccesoTabla

from interprete.extra.tipos import *

tokens = lexer.tokens

# Define la función find_column
def find_column(input_text, token):
    last_cr = input_text.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - last_cr) + 1

def getTextVal(instrucciones):
    text_var = ''
    for instruccion in instrucciones:
        text_var += instruccion.text_val
    return text_var

def getTextVal_coma(params):
    text_var = ''
    for i in range(len(params)):
        if i == len(params) - 1:
            text_var += params[i]
        else:
            text_var += params[i] + ', '
    return text_var

def getTextValExp_coma(params):
    text_var = ''
    for i in range(len(params)):
        if isinstance(params[i], Expresion) or isinstance(params[i], Campo) or isinstance(params[i], Atributo) or isinstance(params[i], Declaracion) or isinstance(params[i], Argumento) or isinstance(params[i], LlamadaFnc) or isinstance(params[i], When) or isinstance(params[i], AccesoTabla):
            if i == len(params) - 1:
                text_var += params[i].text_val
            else:
                text_var += params[i].text_val + ', '
    return text_var

def atributoOpcionesToStr(atributos):
    text_val = ''
    for i in range(len(atributos)):   
        atr_str = ''
        if atributos[i] == TipoOpciones.NOTNULL:
            atr_str = 'not null'
        elif atributos[i] == TipoOpciones.NULL:
            atr_str = 'null'
        elif atributos[i] == TipoOpciones.PRIMARYKEY:
            atr_str = 'primary key'
        elif atributos[i] == TipoOpciones.REFERENCE:
            atr_str = 'reference'
        elif isinstance(atributos[i], Reference):
            atr_str = atributos[i].text_val

        if i == len(atributos) - 1:
            text_val += atr_str
        else:
            text_val += atr_str + ' '
    return text_val

def tipoToStr(tipo):
    if tipo == TipoDato.INT:
        return 'int'
    elif tipo == TipoDato.BIT:
        return 'bit'
    elif tipo == TipoDato.DECIMAL:
        return 'decimal'
    elif tipo == TipoDato.DATE:
        return 'date'
    elif tipo == TipoDato.DATETIME:
        return 'datetime'
    elif tipo == TipoDato.NCHAR:
        return 'nchar'
    elif tipo == TipoDato.NVARCHAR:
        return 'nvarchar'
    elif isinstance(tipo, TipoChars):
        return tipo.text_val

# precedencia de operadores
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'MENOR', 'MAYOR', 'MENOR_IGUAL', 'MAYOR_IGUAL', 'DESIGUALDAD', 'IGUALDAD', 'IGUAL'),
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
    instruccion : clausula PYC
                | declaracion_variable PYC
                | asignacion_variable PYC
                | crear_procedure PYC
                | ejecutar_procedure PYC
                | crear_funcion PYC
                | expresion PYC
                | sentencia_control PYC
    '''
    t[1].text_val += ';\n' 
    t[0] = t[1]

def p_sentencias_control(t):
    '''
    sentencia_control : s_if
                      | s_while
                      | s_return
    '''
    t[0] = t[1]

def p_clausulas(t):
    '''
    clausula : use_db
             | crear_db
             | crear_tb
             | cmd_insert
             | cmd_update
             | cmd_delete
             | cmd_select
             | cmd_drop
             | cmd_truncate
             | cmd_alter
    '''
    t[0] = t[1]

def p_crear_db(t):
    '''
    crear_db : CREATE DATA BASE ID
    '''
    text_val = f'CREATE DATA BASE {t[4]}'
    t[0] = CrearBD(text_val, t[4], t.lineno(1), t.lexpos(1))

def p_use_db(t):
    '''
    use_db : USE ID
    '''
    text_val = f'USE {t[2]}'
    t[0] = Use(text_val, t[2], t.lineno(1), t.lexpos(1))

def p_crear_tabla(t):
    '''
    crear_tb : CREATE TABLE ID PARA atributos PARC
    '''
    text_val = f'CREATE TABLE {t[3]} (\n {getTextValExp_coma(t[5])} \n)'
    t[0] = CrearTB(text_val, t[3], t[5], t.lineno(1), t.lexpos(1))

# INSERT INTO nombre_tabla (col1, col2) VALUES (val1, val2);
def p_cmd_insert(t):
    '''
    cmd_insert : INSERT INTO ID PARA columnas PARC VALUES PARA valores PARC
    '''
    text_val = f'INSERT INTO {t[3]} ({getTextVal_coma(t[5])}) VALUES ({getTextValExp_coma(t[9])})'
    t[0] = Insert(text_val, t[3], t[5], t[9], t.lineno(1), t.lexpos(1))

# UPDATE nombre_tabla SET asignaciones WHERE condiciones;
def p_cmd_update(t):
    '''
    cmd_update : UPDATE ID SET campos WHERE condicion_where
    '''
    text_val = f'UPDATE {t[2]} SET {getTextValExp_coma(t[4])} WHERE {t[6].text_val}'
    t[0] = Update(text_val, t[2], t[4], t[6], t.lineno(1), t.lexpos(1))

# DELETE FROM products WHERE price = 10;
def p_cmd_delete(t):
    '''
    cmd_delete : DELETE FROM ID WHERE condicion_where
    '''
    text_val = f'DELETE FROM {t[3]} WHERE {t[5].text_val}'
    t[0] = Delete(text_val, t[3], t[5], t.lineno(1), t.lexpos(1))

# DROP TABLE nombre_tabla;
def p_cmd_drop(t):
    '''
    cmd_drop : DROP TABLE ID
    '''
    text_val = f'DROP TABLE {t[3]}'
    t[0] = Drop(text_val, t[3], t.lineno(1), t.lexpos(1))

# TRUNCATE TABLE nombre_tabla;
def p_cmd_truncate(t):
    '''
    cmd_truncate : TRUNCATE TABLE ID
    '''
    text_val = f'TRUNCATE TABLE {t[3]}'
    t[0] = Truncate(text_val, t[3], t.lineno(1), t.lexpos(1))

def p_condicion_where(t):
    '''
    condicion_where : ID IGUAL expresion
    '''
    text_val = f'{t[1]} = {t[3].text_val}'
    t[0] = CondicionWhere(text_val, t[1], t[3], linea=t.lineno(1), columna=t.lexpos(1))

def p_condicion_where_expresion(t):
    '''
    condicion_where_select : expresion
                           | ID BETWEEN expresion AND expresion
    '''
    if len(t) == 2:
        t[0] = t[1]
    else:
        text_val = f'{t[1]} BETWEEN {t[3].text_val} && {t[5].text_val}'
        t[0] = Between(text_val=text_val, campo=t[1], op1=t[3], op2=t[5], linea=t.lineno(1), columna=t.lexpos(1))

def p_campos_select(t):
    '''
    campos_select : campos_select COMA expresion
                  | expresion
    '''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[3])
        t[0] = t[1]

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
            | ID PUNTO ID
    '''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = f'{t[1]}.{t[3]}'

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
             | ID tipo 
    '''
    if len(t) == 4:
        text_val = f'{t[1]} {tipoToStr(t[2])} {atributoOpcionesToStr(t[3])}'
        t[0] = Atributo(text_val, t[1], t[2], t[3], t.lineno(1), t.lexpos(1))
    else:
        text_val = f'{t[1]} {tipoToStr(t[2])}'
        t[0] = Atributo(text_val, t[1], t[2], [], t.lineno(1), t.lexpos(1))


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
    atributo_opcion : REFERENCE 
    '''
    t[0] =  TipoOpciones.REFERENCE

def p_atributo_opcion_references_id(t):
    '''
    atributo_opcion : ID PARA ID  PARC
    '''
    text_val = f'{t[1]} ( {t[3]} )'
    t[0] = Reference(text_val, t[1], t[3], t.lineno(1), t.lexpos(1))


def p_cmd_select(t):
    '''
    cmd_select : SELECT op_select
               | op_select
    '''
    if len(t) == 3:
        t[2].text_val = 'SELECT ' + t[2].text_val
        t[0] = t[2]
    else:
        t[0] = t[1]

# FUNCIONES DEL SISTEMA
def p_op_select(t):
    '''
    op_select : select_tabla
              | print
    '''
    t[0] = t[1]


def p_select_tabla(t):
    '''
    select_tabla : campos_select FROM nombre_tablas WHERE condicion_where_select
    '''
    text_val = f'{getTextValExp_coma(t[1])} FROM {getTextVal_coma(t[3])} WHERE {t[5].text_val}'
    t[0] = Select(text_val=text_val, campos=t[1], tablas=t[3], condicion_where=t[5], linea=t.lineno(1), columna=t.lexpos(1))

def p_select_tabla_1(t):
    '''
    select_tabla : campos_select FROM nombre_tablas empty
    '''
    text_val = f'{getTextValExp_coma(t[1])} FROM {getTextVal_coma(t[3])}'
    t[0] = Select(text_val=text_val, campos=t[1], tablas=t[3], condicion_where=None, linea=t.lineno(1), columna=t.lexpos(1))

def p_select_tabla_2(t):
    '''
    select_tabla : MULT FROM nombre_tablas WHERE condicion_where_select
    '''
    text_val = f'* FROM {getTextVal_coma(t[3])} WHERE {t[5].text_val}'
    t[0] = Select(text_val=text_val, campos=t[1], tablas=t[3], condicion_where=t[5], linea=t.lineno(1), columna=t.lexpos(1))

def p_select_tabla_3(t):
    '''
    select_tabla : MULT FROM nombre_tablas
    '''
    text_val = f'* FROM {getTextVal_coma(t[3])}'
    t[0] = Select(text_val=text_val, campos=t[1], tablas=t[3], condicion_where=None, linea=t.lineno(1), columna=t.lexpos(1))


def p_lista_tablas(t):
    '''
    nombre_tablas : columnas
    '''
    t[0] = t[1]


def p_println(t):
    '''
    print : expresion
    '''
    text_val = f'{t[1].text_val}'
    t[0] = Print(text_val=text_val, argumento=t[1], linea=t.lineno(1), columna=t.lexpos(1))


def p_funcion_sistema(t):
    '''
    funcion_sistema : concatenar
                    | substraer
                    | hoy
                    | contar
                    | suma
                    | cas
    '''
    t[0] = t[1]

def p_concatena(t):
    '''
    concatenar : CONCATENAR PARA expresion COMA expresion PARC
    '''
    text_val = f'CONCATENA ({t[3].text_val}, {t[5].text_val})'
    t[0] = Concatenar(text_val, t[3], t[5], t.lineno(1), t.lexpos(1))

def p_substraer(t):
    '''
    substraer : SUBSTRAER PARA expresion COMA expresion COMA expresion PARC
    '''
    text_val = f'SUBSTRAER ({t[3].text_val}, {t[5].text_val}, {t[7].text_val})'
    t[0] = Substraer(text_val, t[3], t[5], t[7], t.lineno(1), t.lexpos(1))

def p_hoy(t):
    '''
    hoy : HOY PARA PARC
    '''
    text_val = f'HOY()'
    t[0] = Hoy(text_val, t.lineno(1), t.lexpos(1))

def p_contar(t):
    '''
    contar : CONTAR PARA MULT PARC FROM nombre_tablas WHERE condicion_where_select
    '''
    text_val = f'CONTAR (*) FROM {getTextVal_coma(t[6])} WHERE {t[8].text_val}'
    t[0] = Contar(text_val=text_val, campos=t[3], tablas=t[6], condicion_where=t[8], linea=t.lineno(1), columna=t.lexpos(1))

def p_contar_1(t):
    '''
    contar : CONTAR PARA MULT PARC FROM nombre_tablas
    '''
    text_val = f'CONTAR (*) FROM {getTextVal_coma(t[6])}'
    t[0] = Contar(text_val=text_val, campos=t[3], tablas=t[6], condicion_where=None, linea=t.lineno(1), columna=t.lexpos(1))

# def p_select_tabla_2(t):
#     '''
#     select_tabla : MULT FROM nombre_tablas WHERE condicion_where_select
#     '''
#     text_val = f'* FROM {getTextVal_coma(t[3])} WHERE {t[5].text_val}'
#     t[0] = Select(text_val=text_val, campos=t[1], tablas=t[3], condicion_where=t[5], linea=t.lineno(1), columna=t.lexpos(1))

def p_suma(t):
    '''
    suma : SUMA PARA columnas PARC FROM nombre_tablas WHERE condicion_where_select
    '''
    text_val = f'SUMA ({getTextVal_coma(t[3])}) FROM {getTextVal_coma(t[6])} WHERE {t[8].text_val}'
    t[0] = Suma(text_val=text_val, campos=t[3], tablas=t[6], condicion_where=t[8], linea=t.lineno(1), columna=t.lexpos(1))

def p_suma_1(t):
    '''
    suma : SUMA PARA columnas PARC FROM nombre_tablas
    '''
    text_val = f'SUMA ({getTextVal_coma(t[3])}) FROM {getTextVal_coma(t[6])}'
    t[0] = Suma(text_val=text_val, campos=t[3], tablas=t[6], condicion_where=None, linea=t.lineno(1), columna=t.lexpos(1))

def p_suma_2(t):
    '''
    suma : SUMA PARA MULT PARC FROM nombre_tablas WHERE condicion_where_select
    '''
    text_val = f'SUMA ({t[3]}) FROM {getTextVal_coma(t[6])} WHERE {t[8].text_val}'
    t[0] = Suma(text_val=text_val, campos=t[3], tablas=t[6], condicion_where=t[8], linea=t.lineno(1), columna=t.lexpos(1))


# CAS ( expression AS type )
def p_cast(t):
    '''
    cas : CAS PARA ARROBA ID AS tipo PARC
    '''
    text_val = f'CAS (@{t[4]} AS {tipoToStr(t[6])})'
    t[0] = Cas(text_val=text_val, id_var=t[4], tipo=t[6], linea=t.lineno(1), columna=t.lexpos(1))

# DECLARACION DE VARIABLES
def p_declaracion_variable(t):
    '''
    declaracion_variable : declaracion
    '''
    t[0] = t[1]

def p_declaracion(t):
    '''
    declaracion : DECLARE ARROBA ID tipo
                | DECLARE ARROBA ID AS tipo
    '''
    if len(t) == 5:
        text_val = f'DECLARE @{t[3]} {tipoToStr(t[4])}'
        t[0] = Declaracion(text_val, t[3], t[4], t.lineno(1), t.lexpos(1))
    elif len(t) == 6:
        text_val = f'DECLARE @{t[3]} AS {tipoToStr(t[5])}'
        t[0] = Declaracion(text_val, t[3], t[5], t.lineno(1), t.lexpos(1))

def p_declaracion_inicializada(t):
    '''
    declaracion_inicializada : DECLARE ARROBA ID tipo IGUAL expresion
    '''

def p_asignacion_variable(t):
    '''
    asignacion_variable : SET ARROBA ID IGUAL expresion
    '''
    text_val = f'SET @ {t[3]} = {t[5].text_val}'
    t[0] = AsignacionVar(text_val, t[3], t[5], t.lineno(1), t.lexpos(1))

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
    text_val = f'{t[1]} = {t[3].text_val}'
    t[0] = Campo(text_val, t[1], t[3], linea=t.lineno(1), columna=t.lexpos(1))

def p_crear_procedure(t):
    '''
    crear_procedure : CREATE PROCEDURE ID PARA parametros PARC AS BEGIN bloque END
    '''
    text_val = f'CREATE PROCEDURE {t[3]} ({getTextValExp_coma(t[5])}) \nAS \nBEGIN \n{getTextVal(t[9])}END'
    bloque = Bloque(getTextVal(t[9]), t[9], linea=t.lineno(1), columna=t.lexpos(1))
    t[0] = Procedure(text_val=text_val, id=t[3], parametros=t[5], instrucciones=bloque, linea=t.lineno(1), columna=t.lexpos(1))

def p_crear_funcion(t):
    '''
    crear_funcion : CREATE FUNCTION ID PARA parametros PARC RETURN tipo AS BEGIN bloque END
    '''
    text_val = f'CREATE FUNCTION {t[3]} ({getTextValExp_coma(t[5])}) \nRETURN {tipoToStr(t[8])} \nAS \nBEGIN {getTextVal(t[11])} END'
    bloque = Bloque(getTextVal(t[11]), t[11], linea=t.lineno(1), columna=t.lexpos(1))
    t[0] = Function(text_val=text_val, tipo_ret=t[8], id=t[3], parametros=t[5], instrucciones=bloque, linea=t.lineno(1), columna=t.lexpos(1))

def p_parametros(t):
    '''
    parametros : parametros COMA parametro
               | parametro
    '''
    if len(t) == 2: 
        t[0] = [t[1]]
    else:           
        t[1].append(t[3])
        t[0] = t[1]


def p_parametro(t):
    '''
    parametro : ARROBA ID tipo
              | ARROBA ID AS tipo
              | empty
    '''
    if len(t) == 4:
        text_val = f'@{t[2]} {tipoToStr(t[3])}'
        t[0] = Declaracion(text_val=text_val, id=t[2], tipo=t[3], linea=t.lineno(1), columna=t.lexpos(1))
    elif len(t) == 5:
        text_val = f'@{t[2]} AS {tipoToStr(t[4])}'
        t[0] = Declaracion(text_val=text_val, id=t[2], tipo=t[4], linea=t.lineno(1), columna=t.lexpos(1))

def p_valores(t):
    '''
    valores : valores COMA valor
            | valor
    '''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[3])
        t[0] = t[1]

def p_valor(t):
    '''
    valor     : expresion
              | empty
    '''
    t[0] = t[1]

def p_ejecutar_procedure(t):
    '''
    ejecutar_procedure : EXEC ID argumentos
    '''
    text_val = f'EXEC {t[2]} {getTextValExp_coma(t[3])}'
    t[0] = Exec(text_val=text_val, nombre_proc=t[2], argumentos=t[3], linea=t.lineno(1), columna=t.lexpos(1))

def p_ejecutar_procedure_1(t):
    '''
    ejecutar_procedure : EXEC ID PARA argumentos PARC
    '''
    text_val = f'EXEC {t[2]} ({getTextValExp_coma(t[4])})'
    t[0] = Exec(text_val=text_val, nombre_proc=t[2], argumentos=t[4], linea=t.lineno(1), columna=t.lexpos(1))

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
    argumento : ARROBA ID IGUAL expresion
              | expresion
              | empty
    '''
    if len(t) == 2 and (isinstance(t[1], Expresion) or isinstance(t[1], Instruccion)):
        text_val = f'{t[1].text_val}'
        t[0] = Argumento(text_val=text_val, id=None, expresion=t[1], linea=t.lineno(1), columna=t.lexpos(1))
    elif len(t) == 5:
        text_val = f'@{t[2]} = {t[4].text_val}'
        t[0] = Argumento(text_val=text_val, id=t[2], expresion=t[4], linea=t.lineno(1), columna=t.lexpos(1))

def p_cmd_alter(t):
    '''
    cmd_alter : ALTER TABLE ID ADD COLUMN ID tipo
              | ALTER TABLE ID ADD ID tipo
    '''
    if len(t) == 8:
        text_val = f'ALTER TABLE {t[3]} ADD {t[6]} {tipoToStr(t[7])}'
        t[0] = AlterADD(text_val, t[3], t[5], t[7], t.lineno(1), t.lexpos(1))
    else:
        text_val = f'ALTER TABLE {t[3]} ADD {t[5]} {tipoToStr(t[6])}'
        t[0] = AlterADD(text_val, t[3], t[5], t[6], t.lineno(1), t.lexpos(1))

def p_cmd_alter_drop(t):
    '''
    cmd_alter : ALTER TABLE ID DROP COLUMN ID
              | ALTER TABLE ID DROP ID
    '''
    if len(t) == 7:
        text_val = f'ALTER TABLE {t[3]} DROP COLUMN {t[6]}'
        t[0] = AlterDROP(text_val, t[3], t[6], t.lineno(1), t.lexpos(1))
    else:
        text_val = f'ALTER TABLE {t[3]} DROP {t[5]}'
        t[0] = AlterDROP(text_val, t[3], t[5], t.lineno(1), t.lexpos(1))


def p_cmd_alter_comp(t):
    '''
    cmd_alter_comp : COLUMN ID
                    | ID
    '''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = t[2]

def p_sentencia_return(t):
    '''
    s_return : RETURN expresion
    '''
    text_val = f'RETURN {t[2].text_val}'
    t[0] = Return(text_val=text_val, exp_ret=t[2], linea=t.lineno(1), columna=t.lexpos(1))

def p_sentencia_if(t):
    '''
    s_if : IF expresion BEGIN bloque END IF
                 | IF expresion BEGIN bloque lista_else_if END IF
                 | IF expresion BEGIN bloque lista_else_if ELSE BEGIN bloque END IF
                 | IF expresion BEGIN bloque ELSE BEGIN bloque END IF
    '''
    if len(t) == 7: # if
        text_val = f'IF {t[2].text_val} BEGIN\n {getTextVal(t[4])} END IF'
        t[0] = IfElse(text_val=text_val, condicion=t[2], bloque=Bloque(getTextVal(t[4]), t[4], linea=t.lineno(1), columna=t.lexpos(1)), bandera_else=False, bloque_else=[], elseifs=[], linea=t.lineno(1), columna=t.lexpos(1))
    
    elif len(t) == 8: # if - else if
        text_val = f'IF {t[2].text_val} BEGIN\n {getTextVal(t[4])} {getTextVal(t[5])} END IF'
        bloque = Bloque(getTextVal(t[4]), t[4], linea=t.lineno(1), columna=t.lexpos(1))
        t[0] = IfElse(text_val=text_val, condicion=t[2], bloque=bloque, bandera_else=False, bloque_else=[], elseifs=t[5], linea=t.lineno(1), columna=t.lexpos(1))
    
    elif len(t) == 11: # if - else if - else
        text_val = f'IF {t[2].text_val} BEGIN\n {getTextVal(t[4])} {getTextVal(t[5])} ELSE BEGIN\n {getTextVal(t[8])} END IF'
        bloque = Bloque(getTextVal(t[4]), t[4], linea=t.lineno(1), columna=t.lexpos(1))
        bloque_else = Bloque(getTextVal(t[8]), t[8], linea=t.lineno(1), columna=t.lexpos(1))
        t[0] = IfElse(text_val=text_val, condicion=t[2], bloque=bloque, bandera_else=True, bloque_else=bloque_else, elseifs=t[5], linea=t.lineno(1), columna=t.lexpos(1))

    elif len(t) == 10:   # If - else
        text_val = f'IF {t[2].text_val} BEGIN\n {getTextVal(t[4])} \nELSE BEGIN\n {getTextVal(t[7])} END IF'
        bloque = Bloque(getTextVal(t[4]), t[4], linea=t.lineno(1), columna=t.lexpos(1))
        bloque_else = Bloque(getTextVal(t[7]), t[7], linea=t.lineno(1), columna=t.lexpos(1))
        t[0] = IfElse(text_val=text_val, condicion=t[2], bloque=bloque, bandera_else=True, bloque_else=bloque_else, elseifs=[], linea=t.lineno(1), columna=t.lexpos(1))

def p_lista_else_if(t):
    '''
    lista_else_if : lista_else_if ELSE IF expresion BEGIN bloque
                  | ELSE IF expresion BEGIN bloque
    '''
    if len(t) == 7:
        text_val = f'ELSE IF {t[4].text_val} BEGIN\n {getTextVal(t[6])}\n'
        bloque = Bloque(getTextVal(t[6]), t[6], linea=t.lineno(1), columna=t.lexpos(1))
        t[1].append(ElseIf(text_val=text_val, condicion=t[4], bloque=bloque, linea=t.lineno(1), columna=t.lexpos(1)))
        t[0] = t[1]
    else:
        text_val = f'ELSE IF {t[3].text_val} BEGIN\n {getTextVal(t[5])}\n'
        bloque = Bloque(getTextVal(t[5]), t[5], linea=t.lineno(1), columna=t.lexpos(1))
        t[0] = [ElseIf(text_val=text_val, condicion=t[3], bloque=bloque, linea=t.lineno(1), columna=t.lexpos(1))]


def p_sentencia_while(t):
    '''
    s_while : WHILE expresion BEGIN bloque END
    '''
    text_val = f'WHILE {t[2].text_val} \nBEGIN \n{getTextVal(t[4])} END'
    bloque = Bloque(getTextVal(t[4]), t[4], linea=t.lineno(1), columna=t.lexpos(1))
    t[0] = While(text_val=text_val, condicion=t[2], bloque=bloque, linea=t.lineno(1), columna=t.lexpos(1))

def p_bloque(t):
    '''
    bloque : instrucciones
    '''
    t[0] = t[1]


# Valores como tal. Eje. 123, "hola", var.
def p_expresion(t):
    '''
    expresion : aritmetica
              | relacional
              | logica
              | literal
              | llamada_fnc
              | case
              | ternario
    '''
    t[0] = t[1]

def p_expresion_parentesis(t):
    '''
    expresion : PARA expresion PARC
    '''
    t[2].text_val = t[1] + t[2].text_val + t[3]
    t[0] = t[2]

def p_acceso_var(t):
    '''
    expresion : ARROBA ID
    '''
    text_val = t[1] + t[2]  
    t[0] = Acceso(text_val, t[2], linea=t.lineno(1), columna=t.lexpos(1))

def p_acceso_tabla(t):
    '''
    expresion : ID PUNTO ID
    '''
    text_val = f'{t[1]}.{t[3]}'
    t[0] = AccesoTabla(text_val=text_val, nom_tabla=t[1], nom_campo=t[3], linea=t.lineno(1), columna=t.lexpos(1))

def p_case(t):
    '''
    case : CASE lista_when ELSE THEN bloque END comp_case
         | CASE lista_when END comp_case
    '''
    if len(t) == 5:
        text_val = f'CASE {getTextValExp_coma(t[2])} END {t[4]}'
        t[0] = Case(text_val=text_val, lista_when=t[2], _else=False, bloque_else=[], linea=t.lineno(1), columna=t.lexpos(1))
    else:
        text_val = f'CASE {getTextValExp_coma(t[2])} ELSE THEN {getTextVal(t[5])} END {t[7]}'
        bloque = Bloque(getTextVal(t[5]), t[5], linea=t.lineno(1), columna=t.lexpos(1))
        t[0] = Case(text_val=text_val, lista_when=t[2], _else=True, bloque_else=bloque, linea=t.lineno(1), columna=t.lexpos(1))

def p_complemento_else_case(t):
    '''
    comp_case : ID
              | empty
    '''
    t[0] = t[1]

def p_case_lista_when(t):
    '''
    lista_when : lista_when c_when
               | c_when
    '''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[2])
        t[0] = t[1]

def p_case_when(t):
    '''
    c_when : WHEN expresion THEN bloque
    '''
    text_val = f'WHEN {t[2].text_val} THEN {getTextVal(t[4])}'
    bloque = Bloque(getTextVal(t[4]), t[4], linea=t.lineno(1), columna=t.lexpos(1))
    t[0] = When(text_val=text_val, condicion=t[2], bloque=bloque, linea=t.lineno(1), columna=t.lexpos(1))

def p_llamada_funcion(t):
    '''
    llamada_fnc : ID PARA argumentos PARC
    '''
    text_val = f'{t[1]} ({getTextValExp_coma(t[3])})'
    t[0] = LlamadaFnc(text_val=text_val, nombre_fnc=t[1], argumentos=t[3], linea=t.lineno(1), columna=t.lexpos(1))

def p_llamada_funciones_sistema(t):
    '''
    llamada_fnc : funcion_sistema
    '''
    t[0] = t[1]

def p_op_ternario(t):
    '''
    ternario : IF PARA expresion COMA expresion COMA expresion PARC 
    '''
    text_val = f'IF ({t[3].text_val}, {t[5].text_val}, {t[7].text_val})'
    t[0] = OpTernario(text_val=text_val, condicion=t[3], instruccionTrue=t[5], instruccionFalse=t[7], linea=t.lineno(1), columna=t.lexpos(1))

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
    text_val = f'{t[1].text_val}  {t[2]}  {t[3].text_val}'
    if t[2] == '=':
        t[0] = Relacional(text_val=text_val, op1=t[1], operador=TipoRelacional.IGUAL, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))
    elif t[2] == '==':
        t[0] = Relacional(text_val=text_val, op1=t[1], operador=TipoRelacional.IGUALDAD, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))
    elif t[2] == '!=':
        t[0] = Relacional(text_val=text_val, op1=t[1], operador=TipoRelacional.DESIGUALDAD, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))
    elif t[2] == '<':
        t[0] = Relacional(text_val=text_val, op1=t[1], operador=TipoRelacional.MENOR, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))
    elif t[2] == '>':
        t[0] = Relacional(text_val=text_val, op1=t[1], operador=TipoRelacional.MAYOR, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))
    elif t[2] == '<=':
        t[0] = Relacional(text_val=text_val, op1=t[1], operador=TipoRelacional.MENOR_IGUAL, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))
    elif t[2] == '>=':
        t[0] = Relacional(text_val=text_val, op1=t[1], operador=TipoRelacional.MAYOR_IGUAL, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))

def p_expresion_aritmetica(t):
    '''
    aritmetica : expresion SUMAR expresion
                | expresion RESTAR expresion
                | expresion MULT expresion
                | expresion DIV expresion
    '''
    text_val = f'{t[1].text_val} {t[2]} {t[3].text_val}'
    if t[2] == '+':
        t[0] = Aritmetica(text_val=text_val, op1=t[1], operador=TipoAritmetica.SUMA, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))
    elif t[2] == '-':
        t[0] = Aritmetica(text_val=text_val,op1=t[1], operador=TipoAritmetica.RESTA, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))
    elif t[2] == '*':
        t[0] = Aritmetica(text_val=text_val,op1=t[1], operador=TipoAritmetica.MULTIPLICACION, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))
    elif t[2] == '/':
        t[0] = Aritmetica(text_val=text_val,op1=t[1], operador=TipoAritmetica.DIVISION, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))

def p_expresion_unaria(t):
    '''
    aritmetica : RESTAR expresion %prec UMENOS
    '''
    text_val = f'-{t[2].text_val}'
    t[0] = Aritmetica(text_val=text_val, op1=t[2], operador=TipoAritmetica.UNARIO, op2=Literal(t[2], TipoDato.UNDEFINED, None, t.lineno(1), t.lexpos(1)), linea=t.lineno(1), columna=t.lexpos(1))

def p_expresion_logica(t):
    '''
    logica : NEGACION expresion
           | expresion OR expresion
           | expresion AND expresion
    '''
    if len(t) == 3:
        text_val = f'- {t[1]} {t[2].text_val}'
        t[0] = Logica(text_val, op1=t[2], operador=TipoLogico.NOT, op2=Literal('', TipoDato.BOOL, False, t.lineno(1), t.lexpos(1)), linea=t.lineno(1), columna=t.lexpos(1))

    elif t[2] == '||':
        text_val = f'{t[1].text_val} || {t[3].text_val}'
        t[0] = Logica(text_val, op1=t[1], operador=TipoLogico.OR, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))

    elif t[2] == '&&':
        text_val = f'{t[1].text_val} && {t[3].text_val}'
        t[0] = Logica(text_val=text_val, op1=t[1], operador=TipoLogico.AND, op2=t[3], linea=t.lineno(1), columna=t.lexpos(1))

def p_entero(t):
    '''
    literal : ENTERO
    '''
    t[0] = Literal(t[1], TipoDato.INT, int(t[1]), t.lineno(1), t.lexpos(1))

def p_cadena(t):
    '''
    literal : CADENA
    '''
    t[0] = Literal(f"'{t[1]}'", TipoDato.NCHAR, t[1], t.lineno(1), t.lexpos(1))

def p_decimal(t):
    '''
    literal : FLOAT
    '''
    t[0] = Literal(t[1], TipoDato.DECIMAL, float(t[1]), t.lineno(1), t.lexpos(1))

def p_id(t):
    '''
    literal : ID
    '''
    t[0] = Acceso(t[1], t[1], linea=t.lineno(1), columna=t.lexpos(1))

def p_null(t):
    '''
    literal : NULL
    '''
    t[0] = Literal(t[1], valor=t[1], tipo=TipoDato.NULL, linea=t.lineno(1), columna=t.lexpos(1))

# def p_acceso_atributo_tabla(t):
#     '''
#     expresion : ID PT ID
#     '''
#     t[0] = AccesoAtributo(table_name=t[1], atribute_name=t[3], linea=t.lineno(1), columna=t.lexpos(1))

def p_tipo(t):
    '''
    tipo : INT
        | BIT
        | DECIMAL
        | DATE
        | DATETIME
        | NCHAR
        | NVARCHAR
        | NCHAR PARA literal PARC
        | NVARCHAR PARA literal PARC
    '''
    if(t[1] == 'int'):
        t[0] = TipoDato.INT;
    elif(t[1] == 'bit'):
        t[0] = TipoDato.BIT;
    elif(t[1] == 'decimal'):
        t[0] = TipoDato.DECIMAL;
    elif(t[1] == 'datetime'):
        t[0] = TipoDato.DATETIME;
    elif(t[1] == 'date'):
        t[0] = TipoDato.DATE;
    elif(t[1] == 'nchar'):
        if len(t) == 2:
            t[0] = TipoDato.NCHAR
        else:
            text_val = f'NCHAR({t[3].text_val})'
            t[0] = TipoChars(text_val, TipoDato.NCHAR, t[2]);
    elif(t[1] == 'nvarchar'):
        if len(t) == 2:
            t[0] = TipoDato.NVARCHAR
        else:
            text_val = f'NVARCHAR({t[3].text_val})'
            t[0] = TipoChars(text_val, TipoDato.NVARCHAR, t[2]);


def p_empty(t):
    '''
    empty :
    '''
    t[0] = None

# Error sintáctico
def p_error(t):
    if t:
        # Agregando a la tabla de erorres
        err = Error(tipo='Sintáctico', linea=t.lineno, columna=find_column(t.lexer.lexdata, t), descripcion=f'Error sintáxis en token: {t.value}')
    else:
        # Agregando a la tabla de erorres
        err = Error(tipo='Sintáctico', linea=0, columna=0, descripcion=f'Final inesperado.')
    TablaErrores.addError(err)


# Build the parser
parser = yacc(debug=True)
