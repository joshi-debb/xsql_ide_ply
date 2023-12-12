
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftMENORMAYORMENOR_IGUALMAYOR_IGUALDESIGUALDADIGUALDADleftRESTARSUMARleftMULTDIVMODULOrightNEGACIONrightUMENOSADD ALTER AND ARROBA AS BASE BEGIN BIT CADENA CAST COLUMN COMA CONCATENAR CONTAR CREATE DATA DATE DATETIME DECIMAL DECLARE DELETE DESIGUALDAD DIV DROP END ENTERO EXEC FLOAT FROM FUNCTION HOY ID IF IGUAL IGUALDAD INSERT INT INTO KEY MAYOR MAYOR_IGUAL MENOR MENOR_IGUAL MODULO MULT NCHAR NEGACION NOT NULL NVARCHAR OR PARA PARC PRIMARY PRINTLN PROCEDURE PYC REFERENCE RESTAR RETURN RETURNS SELECT SET SUBSTRAER SUMA SUMAR TABLE TRUNCATE UPDATE USE VALUES WHERE\n    ini : instrucciones\n    \n    instrucciones : instrucciones instruccion\n    \n    instrucciones : instruccion\n    \n    instruccion : crear_db PYC\n                | crear_tb PYC\n                | cmd_insert PYC\n                | cmd_update PYC\n                | cmd_delete PYC\n                | cmd_select PYC\n                | cmd_drop PYC\n                | cmd_truncate PYC\n                | declaracion_variable\n                | crear_procedure\n                | ejecutar_procedure\n                | crear_funcion\n                | cmd_alter PYC\n                | expresion\n                | use_db PYC\n                | println\n    \n    println : PRINTLN PARA expresion PARC\n    \n    crear_db : CREATE DATA BASE ID\n    \n    use_db : USE ID\n    \n    crear_tb : CREATE TABLE ID PARA atributos PARC\n    \n    cmd_insert : INSERT INTO ID PARA columnas PARC VALUES PARA argumentos PARC\n    \n    cmd_update : UPDATE ID SET campos WHERE condicion_where\n    \n    cmd_delete : DELETE FROM ID WHERE condicion_where\n    \n    cmd_select : SELECT op_select\n    \n    cmd_drop : DROP TABLE ID\n    \n    cmd_truncate : TRUNCATE TABLE ID\n    \n    condicion_where : ID IGUAL expresion\n    \n    columnas : columnas COMA columna\n             | columna\n    \n    columna : ID\n    \n    atributos : atributos COMA atributo\n              | atributo\n    \n    atributo : ID tipo atributo_opciones\n    \n    atributo_opciones : atributo_opciones atributo_opcion\n                      | atributo_opcion\n    \n    atributo_opcion : NOT NULL\n    \n    atributo_opcion : NULL\n    \n    atributo_opcion : PRIMARY KEY\n    \n    atributo_opcion : REFERENCE \n    \n    atributo_opcion : ID PARA ID  PARC\n    \n    op_select : funcion_sistema\n              | select_columnas\n    \n    select_columnas : MULT FROM ID\n    \n    funcion_sistema : concatenar\n                    | substraer\n                    | hoy\n                    | contar\n                    | suma\n                    | cast\n    \n    concatenar : CONCATENAR PARA expresion COMA expresion PARC\n    \n    substraer : SUBSTRAER PARA expresion COMA expresion COMA expresion PARC\n    \n    hoy : HOY PARA PARC\n    \n    contar : CONTAR PARA MULT PARC  FROM ID WHERE condicion_where\n    \n    suma : SUMA PARA expresion PARC FROM ID WHERE condicion_where\n    \n    cast : CAST PARA expresion AS tipo PARC\n    \n    declaracion_variable : declaracion\n                         | declaracion_inicializada\n    \n    declaracion : DECLARE ARROBA ID tipo\n    \n    declaracion_inicializada : DECLARE ARROBA ID tipo IGUAL expresion\n    \n    asignacion : ARROBA ID IGUAL expresion\n    \n    campos : campos COMA campo\n           | campo\n    \n    campo : ID IGUAL expresion\n    \n    crear_procedure : CREATE PROCEDURE ID PARA parametros PARC AS \n    \n    crear_funcion : CREATE FUNCTION ID PARA parametros PARC RETURNS tipo AS BEGIN RETURN END\n    \n    parametros : parametros COMA parametro\n               | parametro\n    \n    parametro : ARROBA ID tipo\n              | empty\n    \n    argumentos : argumentos COMA argumento\n               | argumento\n    \n    argumento : expresion\n              | empty\n    \n    ejecutar_procedure : EXEC ID argumentos\n    \n    cmd_alter : ALTER TABLE ID ADD cmd_alter_comp tipo\n    \n    cmd_alter : ALTER TABLE ID DROP cmd_alter_comp\n    \n    cmd_alter_comp : COLUMN ID\n                    | ID\n    \n    expresion : aritmetica\n              | relacional\n              | logica\n              | literal\n              | ID\n    \n    expresion : PARA expresion PARC\n    \n    relacional : expresion IGUAL expresion\n               | expresion IGUALDAD expresion\n               | expresion DESIGUALDAD expresion\n               | expresion MENOR expresion\n               | expresion MAYOR expresion\n               | expresion MENOR_IGUAL expresion\n               | expresion MAYOR_IGUAL expresion\n    \n    aritmetica : expresion SUMAR expresion\n                | expresion RESTAR expresion\n                | expresion MULT expresion\n                | expresion DIV expresion\n    \n    aritmetica : RESTAR expresion %prec UMENOS\n    \n    logica : NEGACION expresion\n           | expresion OR expresion\n           | expresion AND expresion\n    \n    literal : ENTERO\n    \n    literal : CADENA\n    \n    literal : FLOAT\n    \n    tipo : INT\n        | BIT\n        | DECIMAL\n        | DATE\n        | DATETIME\n        | NCHAR comp_n\n        | NVARCHAR comp_n\n    \n    comp_n : PARA literal PARC\n    \n    empty :\n    '
    
_lr_action_items = {'CREATE':([0,2,3,12,13,14,15,17,19,21,29,30,33,34,35,36,42,43,44,45,46,47,48,49,50,51,52,53,54,68,95,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,132,133,134,135,155,158,159,160,161,162,163,164,188,194,196,217,227,239,259,],[20,20,-3,-12,-13,-14,-15,-17,-19,-86,-59,-60,-82,-83,-84,-85,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,-18,-114,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,-77,-74,-75,-76,-114,-20,-61,-106,-107,-108,-109,-110,-73,-111,-112,-62,-67,-113,-68,]),'INSERT':([0,2,3,12,13,14,15,17,19,21,29,30,33,34,35,36,42,43,44,45,46,47,48,49,50,51,52,53,54,68,95,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,132,133,134,135,155,158,159,160,161,162,163,164,188,194,196,217,227,239,259,],[23,23,-3,-12,-13,-14,-15,-17,-19,-86,-59,-60,-82,-83,-84,-85,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,-18,-114,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,-77,-74,-75,-76,-114,-20,-61,-106,-107,-108,-109,-110,-73,-111,-112,-62,-67,-113,-68,]),'UPDATE':([0,2,3,12,13,14,15,17,19,21,29,30,33,34,35,36,42,43,44,45,46,47,48,49,50,51,52,53,54,68,95,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,132,133,134,135,155,158,159,160,161,162,163,164,188,194,196,217,227,239,259,],[24,24,-3,-12,-13,-14,-15,-17,-19,-86,-59,-60,-82,-83,-84,-85,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,-18,-114,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,-77,-74,-75,-76,-114,-20,-61,-106,-107,-108,-109,-110,-73,-111,-112,-62,-67,-113,-68,]),'DELETE':([0,2,3,12,13,14,15,17,19,21,29,30,33,34,35,36,42,43,44,45,46,47,48,49,50,51,52,53,54,68,95,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,132,133,134,135,155,158,159,160,161,162,163,164,188,194,196,217,227,239,259,],[25,25,-3,-12,-13,-14,-15,-17,-19,-86,-59,-60,-82,-83,-84,-85,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,-18,-114,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,-77,-74,-75,-76,-114,-20,-61,-106,-107,-108,-109,-110,-73,-111,-112,-62,-67,-113,-68,]),'SELECT':([0,2,3,12,13,14,15,17,19,21,29,30,33,34,35,36,42,43,44,45,46,47,48,49,50,51,52,53,54,68,95,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,132,133,134,135,155,158,159,160,161,162,163,164,188,194,196,217,227,239,259,],[26,26,-3,-12,-13,-14,-15,-17,-19,-86,-59,-60,-82,-83,-84,-85,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,-18,-114,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,-77,-74,-75,-76,-114,-20,-61,-106,-107,-108,-109,-110,-73,-111,-112,-62,-67,-113,-68,]),'DROP':([0,2,3,12,13,14,15,17,19,21,29,30,33,34,35,36,42,43,44,45,46,47,48,49,50,51,52,53,54,68,95,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,132,133,134,135,136,155,158,159,160,161,162,163,164,188,194,196,217,227,239,259,],[27,27,-3,-12,-13,-14,-15,-17,-19,-86,-59,-60,-82,-83,-84,-85,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,-18,-114,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,-77,-74,-75,-76,157,-114,-20,-61,-106,-107,-108,-109,-110,-73,-111,-112,-62,-67,-113,-68,]),'TRUNCATE':([0,2,3,12,13,14,15,17,19,21,29,30,33,34,35,36,42,43,44,45,46,47,48,49,50,51,52,53,54,68,95,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,132,133,134,135,155,158,159,160,161,162,163,164,188,194,196,217,227,239,259,],[28,28,-3,-12,-13,-14,-15,-17,-19,-86,-59,-60,-82,-83,-84,-85,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,-18,-114,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,-77,-74,-75,-76,-114,-20,-61,-106,-107,-108,-109,-110,-73,-111,-112,-62,-67,-113,-68,]),'EXEC':([0,2,3,12,13,14,15,17,19,21,29,30,33,34,35,36,42,43,44,45,46,47,48,49,50,51,52,53,54,68,95,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,132,133,134,135,155,158,159,160,161,162,163,164,188,194,196,217,227,239,259,],[31,31,-3,-12,-13,-14,-15,-17,-19,-86,-59,-60,-82,-83,-84,-85,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,-18,-114,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,-77,-74,-75,-76,-114,-20,-61,-106,-107,-108,-109,-110,-73,-111,-112,-62,-67,-113,-68,]),'ALTER':([0,2,3,12,13,14,15,17,19,21,29,30,33,34,35,36,42,43,44,45,46,47,48,49,50,51,52,53,54,68,95,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,132,133,134,135,155,158,159,160,161,162,163,164,188,194,196,217,227,239,259,],[32,32,-3,-12,-13,-14,-15,-17,-19,-86,-59,-60,-82,-83,-84,-85,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,-18,-114,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,-77,-74,-75,-76,-114,-20,-61,-106,-107,-108,-109,-110,-73,-111,-112,-62,-67,-113,-68,]),'ID':([0,2,3,12,13,14,15,17,19,21,22,24,29,30,31,33,34,35,36,37,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,72,74,76,93,94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,119,121,123,124,125,128,129,132,133,134,135,140,143,147,155,156,157,158,159,160,161,162,163,164,172,178,179,180,183,184,188,191,193,194,196,197,199,205,209,212,213,217,220,221,223,225,227,235,239,240,241,242,243,245,247,248,255,259,],[21,21,-3,-12,-13,-14,-15,-17,-19,-86,21,75,-59,-60,95,-82,-83,-84,-85,97,21,21,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,21,21,21,21,21,21,21,21,21,21,21,21,21,-18,116,117,118,120,122,130,131,21,136,21,138,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,139,-87,144,148,21,21,21,21,-77,-74,-75,-76,167,175,181,21,189,189,-20,-61,-106,-107,-108,-109,-110,202,21,181,144,21,21,-73,216,21,-111,-112,219,167,175,21,236,237,-62,219,-38,-40,-42,-67,21,-113,249,-37,-39,-41,21,181,181,-43,-68,]),'PARA':([0,2,3,12,13,14,15,17,19,21,22,29,30,33,34,35,36,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,87,88,89,90,91,92,95,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,116,117,118,119,120,124,125,128,129,132,133,134,135,155,158,159,160,161,162,163,164,165,166,178,183,184,188,193,194,196,209,217,219,227,231,235,239,245,259,],[22,22,-3,-12,-13,-14,-15,-17,-19,-86,22,-59,-60,-82,-83,-84,-85,98,22,22,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,22,22,22,22,22,22,22,22,22,22,22,22,22,-18,124,125,126,127,128,129,22,22,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,140,141,142,-87,143,22,22,22,22,-77,-74,-75,-76,22,-20,-61,-106,-107,-108,-109,-110,195,195,22,22,22,-73,22,-111,-112,22,-62,240,-67,245,22,-113,22,-68,]),'USE':([0,2,3,12,13,14,15,17,19,21,29,30,33,34,35,36,42,43,44,45,46,47,48,49,50,51,52,53,54,68,95,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,132,133,134,135,155,158,159,160,161,162,163,164,188,194,196,217,227,239,259,],[37,37,-3,-12,-13,-14,-15,-17,-19,-86,-59,-60,-82,-83,-84,-85,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,-18,-114,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,-77,-74,-75,-76,-114,-20,-61,-106,-107,-108,-109,-110,-73,-111,-112,-62,-67,-113,-68,]),'PRINTLN':([0,2,3,12,13,14,15,17,19,21,29,30,33,34,35,36,42,43,44,45,46,47,48,49,50,51,52,53,54,68,95,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,132,133,134,135,155,158,159,160,161,162,163,164,188,194,196,217,227,239,259,],[38,38,-3,-12,-13,-14,-15,-17,-19,-86,-59,-60,-82,-83,-84,-85,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,-18,-114,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,-77,-74,-75,-76,-114,-20,-61,-106,-107,-108,-109,-110,-73,-111,-112,-62,-67,-113,-68,]),'DECLARE':([0,2,3,12,13,14,15,17,19,21,29,30,33,34,35,36,42,43,44,45,46,47,48,49,50,51,52,53,54,68,95,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,132,133,134,135,155,158,159,160,161,162,163,164,188,194,196,217,227,239,259,],[39,39,-3,-12,-13,-14,-15,-17,-19,-86,-59,-60,-82,-83,-84,-85,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,-18,-114,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,-77,-74,-75,-76,-114,-20,-61,-106,-107,-108,-109,-110,-73,-111,-112,-62,-67,-113,-68,]),'RESTAR':([0,2,3,12,13,14,15,17,19,21,22,29,30,33,34,35,36,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,95,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,124,125,128,129,132,133,134,135,137,149,150,153,154,155,158,159,160,161,162,163,164,178,183,184,188,193,194,196,206,209,210,211,217,227,233,235,239,245,246,259,],[40,40,-3,-12,-13,-14,-15,56,-19,-86,40,-59,-60,-82,-83,-84,-85,40,40,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,40,40,40,40,40,40,40,40,40,40,40,40,40,-18,56,40,40,-99,-100,-95,-96,-97,-98,56,56,56,56,56,56,56,56,56,-87,40,40,40,40,-77,-74,56,-76,56,56,56,56,56,40,-20,-61,-106,-107,-108,-109,-110,40,40,40,-73,40,-111,-112,56,40,56,56,56,-67,56,40,-113,40,56,-68,]),'NEGACION':([0,2,3,12,13,14,15,17,19,21,22,29,30,33,34,35,36,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,95,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,124,125,128,129,132,133,134,135,155,158,159,160,161,162,163,164,178,183,184,188,193,194,196,209,217,227,235,239,245,259,],[41,41,-3,-12,-13,-14,-15,-17,-19,-86,41,-59,-60,-82,-83,-84,-85,41,41,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,41,41,41,41,41,41,41,41,41,41,41,41,41,-18,41,41,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,41,41,41,41,-77,-74,-75,-76,41,-20,-61,-106,-107,-108,-109,-110,41,41,41,-73,41,-111,-112,41,-62,-67,41,-113,41,-68,]),'ENTERO':([0,2,3,12,13,14,15,17,19,21,22,29,30,33,34,35,36,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,95,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,124,125,128,129,132,133,134,135,155,158,159,160,161,162,163,164,178,183,184,188,193,194,195,196,209,217,227,235,239,245,259,],[42,42,-3,-12,-13,-14,-15,-17,-19,-86,42,-59,-60,-82,-83,-84,-85,42,42,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,42,42,42,42,42,42,42,42,42,42,42,42,42,-18,42,42,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,42,42,42,42,-77,-74,-75,-76,42,-20,-61,-106,-107,-108,-109,-110,42,42,42,-73,42,-111,42,-112,42,-62,-67,42,-113,42,-68,]),'CADENA':([0,2,3,12,13,14,15,17,19,21,22,29,30,33,34,35,36,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,95,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,124,125,128,129,132,133,134,135,155,158,159,160,161,162,163,164,178,183,184,188,193,194,195,196,209,217,227,235,239,245,259,],[43,43,-3,-12,-13,-14,-15,-17,-19,-86,43,-59,-60,-82,-83,-84,-85,43,43,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,43,43,43,43,43,43,43,43,43,43,43,43,43,-18,43,43,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,43,43,43,43,-77,-74,-75,-76,43,-20,-61,-106,-107,-108,-109,-110,43,43,43,-73,43,-111,43,-112,43,-62,-67,43,-113,43,-68,]),'FLOAT':([0,2,3,12,13,14,15,17,19,21,22,29,30,33,34,35,36,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,95,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,124,125,128,129,132,133,134,135,155,158,159,160,161,162,163,164,178,183,184,188,193,194,195,196,209,217,227,235,239,245,259,],[44,44,-3,-12,-13,-14,-15,-17,-19,-86,44,-59,-60,-82,-83,-84,-85,44,44,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,44,44,44,44,44,44,44,44,44,44,44,44,44,-18,44,44,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,44,44,44,44,-77,-74,-75,-76,44,-20,-61,-106,-107,-108,-109,-110,44,44,44,-73,44,-111,44,-112,44,-62,-67,44,-113,44,-68,]),'$end':([1,2,3,12,13,14,15,17,19,21,29,30,33,34,35,36,42,43,44,45,46,47,48,49,50,51,52,53,54,68,95,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,132,133,134,135,155,158,159,160,161,162,163,164,188,194,196,217,227,239,259,],[0,-1,-3,-12,-13,-14,-15,-17,-19,-86,-59,-60,-82,-83,-84,-85,-103,-104,-105,-2,-4,-5,-6,-7,-8,-9,-10,-11,-16,-18,-114,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,-77,-74,-75,-76,-114,-20,-61,-106,-107,-108,-109,-110,-73,-111,-112,-62,-67,-113,-68,]),'PYC':([4,5,6,7,8,9,10,11,16,18,21,33,34,35,36,42,43,44,77,78,79,80,81,82,83,84,85,97,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,130,131,139,148,151,160,161,162,163,164,182,189,192,194,196,198,207,215,216,233,234,238,239,252,253,254,257,],[46,47,48,49,50,51,52,53,54,68,-86,-82,-83,-84,-85,-103,-104,-105,-27,-44,-45,-47,-48,-49,-50,-51,-52,-22,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,-28,-29,-21,-46,-55,-106,-107,-108,-109,-110,-26,-81,-79,-111,-112,-23,-25,-78,-80,-30,-53,-58,-113,-54,-56,-57,-24,]),'SUMAR':([17,21,33,34,35,36,42,43,44,73,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,134,137,149,150,153,154,206,210,211,217,233,246,],[55,-86,-82,-83,-84,-85,-103,-104,-105,55,-99,-100,-95,-96,-97,-98,55,55,55,55,55,55,55,55,55,-87,55,55,55,55,55,55,55,55,55,55,55,55,]),'MULT':([17,21,26,33,34,35,36,42,43,44,73,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,127,134,137,149,150,153,154,206,210,211,217,233,246,],[57,-86,86,-82,-83,-84,-85,-103,-104,-105,57,-99,-100,57,57,-97,-98,57,57,57,57,57,57,57,57,57,-87,152,57,57,57,57,57,57,57,57,57,57,57,57,]),'DIV':([17,21,33,34,35,36,42,43,44,73,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,134,137,149,150,153,154,206,210,211,217,233,246,],[58,-86,-82,-83,-84,-85,-103,-104,-105,58,-99,-100,58,58,-97,-98,58,58,58,58,58,58,58,58,58,-87,58,58,58,58,58,58,58,58,58,58,58,58,]),'IGUAL':([17,21,33,34,35,36,42,43,44,73,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,134,137,144,149,150,153,154,159,160,161,162,163,164,181,194,196,206,210,211,217,233,239,246,],[59,-86,-82,-83,-84,-85,-103,-104,-105,59,-99,-100,-95,-96,-97,-98,59,-89,-90,-91,-92,-93,-94,-101,-102,-87,59,59,178,59,59,59,59,193,-106,-107,-108,-109,-110,209,-111,-112,59,59,59,59,59,-113,59,]),'IGUALDAD':([17,21,33,34,35,36,42,43,44,73,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,134,137,149,150,153,154,206,210,211,217,233,246,],[60,-86,-82,-83,-84,-85,-103,-104,-105,60,-99,-100,-95,-96,-97,-98,60,-89,-90,-91,-92,-93,-94,60,60,-87,60,60,60,60,60,60,60,60,60,60,60,60,]),'DESIGUALDAD':([17,21,33,34,35,36,42,43,44,73,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,134,137,149,150,153,154,206,210,211,217,233,246,],[61,-86,-82,-83,-84,-85,-103,-104,-105,61,-99,-100,-95,-96,-97,-98,61,-89,-90,-91,-92,-93,-94,61,61,-87,61,61,61,61,61,61,61,61,61,61,61,61,]),'MENOR':([17,21,33,34,35,36,42,43,44,73,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,134,137,149,150,153,154,206,210,211,217,233,246,],[62,-86,-82,-83,-84,-85,-103,-104,-105,62,-99,-100,-95,-96,-97,-98,62,-89,-90,-91,-92,-93,-94,62,62,-87,62,62,62,62,62,62,62,62,62,62,62,62,]),'MAYOR':([17,21,33,34,35,36,42,43,44,73,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,134,137,149,150,153,154,206,210,211,217,233,246,],[63,-86,-82,-83,-84,-85,-103,-104,-105,63,-99,-100,-95,-96,-97,-98,63,-89,-90,-91,-92,-93,-94,63,63,-87,63,63,63,63,63,63,63,63,63,63,63,63,]),'MENOR_IGUAL':([17,21,33,34,35,36,42,43,44,73,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,134,137,149,150,153,154,206,210,211,217,233,246,],[64,-86,-82,-83,-84,-85,-103,-104,-105,64,-99,-100,-95,-96,-97,-98,64,-89,-90,-91,-92,-93,-94,64,64,-87,64,64,64,64,64,64,64,64,64,64,64,64,]),'MAYOR_IGUAL':([17,21,33,34,35,36,42,43,44,73,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,134,137,149,150,153,154,206,210,211,217,233,246,],[65,-86,-82,-83,-84,-85,-103,-104,-105,65,-99,-100,-95,-96,-97,-98,65,-89,-90,-91,-92,-93,-94,65,65,-87,65,65,65,65,65,65,65,65,65,65,65,65,]),'OR':([17,21,33,34,35,36,42,43,44,73,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,134,137,149,150,153,154,206,210,211,217,233,246,],[66,-86,-82,-83,-84,-85,-103,-104,-105,66,-99,-100,-95,-96,-97,-98,66,-89,-90,-91,-92,-93,-94,-101,-102,-87,66,66,66,66,66,66,66,66,66,66,66,66,]),'AND':([17,21,33,34,35,36,42,43,44,73,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,134,137,149,150,153,154,206,210,211,217,233,246,],[67,-86,-82,-83,-84,-85,-103,-104,-105,67,-99,-100,-95,-96,-97,-98,67,-89,-90,-91,-92,-93,-94,67,-102,-87,67,67,67,67,67,67,67,67,67,67,67,67,]),'DATA':([20,],[69,]),'TABLE':([20,27,28,32,],[70,93,94,96,]),'PROCEDURE':([20,],[71,]),'FUNCTION':([20,],[72,]),'PARC':([21,33,34,35,36,42,43,44,73,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,126,133,134,135,137,141,142,152,153,155,160,161,162,163,164,168,169,170,171,173,174,175,176,177,188,194,196,201,210,214,218,220,221,223,225,226,228,229,232,239,241,242,243,245,246,249,251,255,],[-86,-82,-83,-84,-85,-103,-104,-105,119,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,151,-74,-75,-76,158,-114,-114,185,186,-114,-106,-107,-108,-109,-110,198,-35,200,-70,-72,203,-33,204,-32,-73,-111,-112,-114,234,238,239,-36,-38,-40,-42,-34,-69,-71,-31,-113,-37,-39,-41,-114,252,255,257,-43,]),'COMA':([21,33,34,35,36,42,43,44,95,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,132,133,134,135,141,142,145,146,149,150,155,160,161,162,163,164,168,169,170,171,173,174,175,176,177,188,194,196,201,206,208,211,220,221,223,225,226,228,229,232,239,241,242,243,245,251,255,],[-86,-82,-83,-84,-85,-103,-104,-105,-114,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,155,-74,-75,-76,-114,-114,180,-65,183,184,-114,-106,-107,-108,-109,-110,199,-35,201,-70,-72,201,-33,205,-32,-73,-111,-112,-114,-66,-64,235,-36,-38,-40,-42,-34,-69,-71,-31,-113,-37,-39,-41,-114,155,-43,]),'AS':([21,33,34,35,36,42,43,44,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,154,160,161,162,163,164,194,196,200,239,244,],[-86,-82,-83,-84,-85,-103,-104,-105,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,187,-106,-107,-108,-109,-110,-111,-112,227,-113,250,]),'WHERE':([21,33,34,35,36,42,43,44,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,122,145,146,206,208,236,237,],[-86,-82,-83,-84,-85,-103,-104,-105,-99,-100,-95,-96,-97,-98,-88,-89,-90,-91,-92,-93,-94,-101,-102,-87,147,179,-65,-66,-64,247,248,]),'INTO':([23,],[74,]),'FROM':([25,86,185,186,],[76,123,212,213,]),'CONCATENAR':([26,],[87,]),'SUBSTRAER':([26,],[88,]),'HOY':([26,],[89,]),'CONTAR':([26,],[90,]),'SUMA':([26,],[91,]),'CAST':([26,],[92,]),'ARROBA':([39,141,142,201,],[99,172,172,172,]),'BASE':([69,],[115,]),'SET':([75,],[121,]),'ADD':([136,],[156,]),'INT':([138,167,187,189,190,202,216,230,],[160,160,160,-81,160,160,-80,160,]),'BIT':([138,167,187,189,190,202,216,230,],[161,161,161,-81,161,161,-80,161,]),'DECIMAL':([138,167,187,189,190,202,216,230,],[162,162,162,-81,162,162,-80,162,]),'DATE':([138,167,187,189,190,202,216,230,],[163,163,163,-81,163,163,-80,163,]),'DATETIME':([138,167,187,189,190,202,216,230,],[164,164,164,-81,164,164,-80,164,]),'NCHAR':([138,167,187,189,190,202,216,230,],[165,165,165,-81,165,165,-80,165,]),'NVARCHAR':([138,167,187,189,190,202,216,230,],[166,166,166,-81,166,166,-80,166,]),'COLUMN':([156,157,],[191,191,]),'NOT':([160,161,162,163,164,194,196,197,220,221,223,225,239,241,242,243,255,],[-106,-107,-108,-109,-110,-111,-112,222,222,-38,-40,-42,-113,-37,-39,-41,-43,]),'NULL':([160,161,162,163,164,194,196,197,220,221,222,223,225,239,241,242,243,255,],[-106,-107,-108,-109,-110,-111,-112,223,223,-38,242,-40,-42,-113,-37,-39,-41,-43,]),'PRIMARY':([160,161,162,163,164,194,196,197,220,221,223,225,239,241,242,243,255,],[-106,-107,-108,-109,-110,-111,-112,224,224,-38,-40,-42,-113,-37,-39,-41,-43,]),'REFERENCE':([160,161,162,163,164,194,196,197,220,221,223,225,239,241,242,243,255,],[-106,-107,-108,-109,-110,-111,-112,225,225,-38,-40,-42,-113,-37,-39,-41,-43,]),'RETURNS':([203,],[230,]),'VALUES':([204,],[231,]),'KEY':([224,],[243,]),'BEGIN':([250,],[256,]),'RETURN':([256,],[258,]),'END':([258,],[259,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ini':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,45,]),'crear_db':([0,2,],[4,4,]),'crear_tb':([0,2,],[5,5,]),'cmd_insert':([0,2,],[6,6,]),'cmd_update':([0,2,],[7,7,]),'cmd_delete':([0,2,],[8,8,]),'cmd_select':([0,2,],[9,9,]),'cmd_drop':([0,2,],[10,10,]),'cmd_truncate':([0,2,],[11,11,]),'declaracion_variable':([0,2,],[12,12,]),'crear_procedure':([0,2,],[13,13,]),'ejecutar_procedure':([0,2,],[14,14,]),'crear_funcion':([0,2,],[15,15,]),'cmd_alter':([0,2,],[16,16,]),'expresion':([0,2,22,40,41,55,56,57,58,59,60,61,62,63,64,65,66,67,95,98,124,125,128,129,155,178,183,184,193,209,235,245,],[17,17,73,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,134,137,149,150,153,154,134,206,210,211,217,233,246,134,]),'use_db':([0,2,],[18,18,]),'println':([0,2,],[19,19,]),'declaracion':([0,2,],[29,29,]),'declaracion_inicializada':([0,2,],[30,30,]),'aritmetica':([0,2,22,40,41,55,56,57,58,59,60,61,62,63,64,65,66,67,95,98,124,125,128,129,155,178,183,184,193,209,235,245,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'relacional':([0,2,22,40,41,55,56,57,58,59,60,61,62,63,64,65,66,67,95,98,124,125,128,129,155,178,183,184,193,209,235,245,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'logica':([0,2,22,40,41,55,56,57,58,59,60,61,62,63,64,65,66,67,95,98,124,125,128,129,155,178,183,184,193,209,235,245,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'literal':([0,2,22,40,41,55,56,57,58,59,60,61,62,63,64,65,66,67,95,98,124,125,128,129,155,178,183,184,193,195,209,235,245,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,218,36,36,36,]),'op_select':([26,],[77,]),'funcion_sistema':([26,],[78,]),'select_columnas':([26,],[79,]),'concatenar':([26,],[80,]),'substraer':([26,],[81,]),'hoy':([26,],[82,]),'contar':([26,],[83,]),'suma':([26,],[84,]),'cast':([26,],[85,]),'argumentos':([95,245,],[132,251,]),'argumento':([95,155,245,],[133,188,133,]),'empty':([95,141,142,155,201,245,],[135,173,173,135,173,135,]),'campos':([121,],[145,]),'campo':([121,180,],[146,208,]),'tipo':([138,167,187,190,202,230,],[159,197,214,215,229,244,]),'atributos':([140,],[168,]),'atributo':([140,199,],[169,226,]),'parametros':([141,142,],[170,174,]),'parametro':([141,142,201,],[171,171,228,]),'columnas':([143,],[176,]),'columna':([143,205,],[177,232,]),'condicion_where':([147,179,247,248,],[182,207,253,254,]),'cmd_alter_comp':([156,157,],[190,192,]),'comp_n':([165,166,],[194,196,]),'atributo_opciones':([197,],[220,]),'atributo_opcion':([197,220,],[221,241,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> ini","S'",1,None,None,None),
  ('ini -> instrucciones','ini',1,'p_inicio','parser.py',49),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones','parser.py',56),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','parser.py',64),
  ('instruccion -> crear_db PYC','instruccion',2,'p_instruccion','parser.py',70),
  ('instruccion -> crear_tb PYC','instruccion',2,'p_instruccion','parser.py',71),
  ('instruccion -> cmd_insert PYC','instruccion',2,'p_instruccion','parser.py',72),
  ('instruccion -> cmd_update PYC','instruccion',2,'p_instruccion','parser.py',73),
  ('instruccion -> cmd_delete PYC','instruccion',2,'p_instruccion','parser.py',74),
  ('instruccion -> cmd_select PYC','instruccion',2,'p_instruccion','parser.py',75),
  ('instruccion -> cmd_drop PYC','instruccion',2,'p_instruccion','parser.py',76),
  ('instruccion -> cmd_truncate PYC','instruccion',2,'p_instruccion','parser.py',77),
  ('instruccion -> declaracion_variable','instruccion',1,'p_instruccion','parser.py',78),
  ('instruccion -> crear_procedure','instruccion',1,'p_instruccion','parser.py',79),
  ('instruccion -> ejecutar_procedure','instruccion',1,'p_instruccion','parser.py',80),
  ('instruccion -> crear_funcion','instruccion',1,'p_instruccion','parser.py',81),
  ('instruccion -> cmd_alter PYC','instruccion',2,'p_instruccion','parser.py',82),
  ('instruccion -> expresion','instruccion',1,'p_instruccion','parser.py',83),
  ('instruccion -> use_db PYC','instruccion',2,'p_instruccion','parser.py',84),
  ('instruccion -> println','instruccion',1,'p_instruccion','parser.py',85),
  ('println -> PRINTLN PARA expresion PARC','println',4,'p_println','parser.py',91),
  ('crear_db -> CREATE DATA BASE ID','crear_db',4,'p_crear_db','parser.py',97),
  ('use_db -> USE ID','use_db',2,'p_use_db','parser.py',103),
  ('crear_tb -> CREATE TABLE ID PARA atributos PARC','crear_tb',6,'p_crear_tabla','parser.py',109),
  ('cmd_insert -> INSERT INTO ID PARA columnas PARC VALUES PARA argumentos PARC','cmd_insert',10,'p_cmd_insert','parser.py',116),
  ('cmd_update -> UPDATE ID SET campos WHERE condicion_where','cmd_update',6,'p_cmd_update','parser.py',123),
  ('cmd_delete -> DELETE FROM ID WHERE condicion_where','cmd_delete',5,'p_cmd_delete','parser.py',130),
  ('cmd_select -> SELECT op_select','cmd_select',2,'p_cmd_select','parser.py',137),
  ('cmd_drop -> DROP TABLE ID','cmd_drop',3,'p_cmd_drop','parser.py',144),
  ('cmd_truncate -> TRUNCATE TABLE ID','cmd_truncate',3,'p_cmd_truncate','parser.py',151),
  ('condicion_where -> ID IGUAL expresion','condicion_where',3,'p_condicion_where','parser.py',157),
  ('columnas -> columnas COMA columna','columnas',3,'p_columnas','parser.py',163),
  ('columnas -> columna','columnas',1,'p_columnas','parser.py',164),
  ('columna -> ID','columna',1,'p_columna','parser.py',174),
  ('atributos -> atributos COMA atributo','atributos',3,'p_atributos','parser.py',180),
  ('atributos -> atributo','atributos',1,'p_atributos','parser.py',181),
  ('atributo -> ID tipo atributo_opciones','atributo',3,'p_atributo','parser.py',192),
  ('atributo_opciones -> atributo_opciones atributo_opcion','atributo_opciones',2,'p_atributo_opciones','parser.py',199),
  ('atributo_opciones -> atributo_opcion','atributo_opciones',1,'p_atributo_opciones','parser.py',200),
  ('atributo_opcion -> NOT NULL','atributo_opcion',2,'p_atributo_opcion','parser.py',210),
  ('atributo_opcion -> NULL','atributo_opcion',1,'p_atributo_opcion_null','parser.py',216),
  ('atributo_opcion -> PRIMARY KEY','atributo_opcion',2,'p_atributo_opcion_primarykey','parser.py',222),
  ('atributo_opcion -> REFERENCE','atributo_opcion',1,'p_atributo_opcion_references','parser.py',228),
  ('atributo_opcion -> ID PARA ID PARC','atributo_opcion',4,'p_atributo_opcion_references_id','parser.py',234),
  ('op_select -> funcion_sistema','op_select',1,'p_op_select','parser.py',243),
  ('op_select -> select_columnas','op_select',1,'p_op_select','parser.py',244),
  ('select_columnas -> MULT FROM ID','select_columnas',3,'p_select_columnas','parser.py',250),
  ('funcion_sistema -> concatenar','funcion_sistema',1,'p_funcion_sistema','parser.py',257),
  ('funcion_sistema -> substraer','funcion_sistema',1,'p_funcion_sistema','parser.py',258),
  ('funcion_sistema -> hoy','funcion_sistema',1,'p_funcion_sistema','parser.py',259),
  ('funcion_sistema -> contar','funcion_sistema',1,'p_funcion_sistema','parser.py',260),
  ('funcion_sistema -> suma','funcion_sistema',1,'p_funcion_sistema','parser.py',261),
  ('funcion_sistema -> cast','funcion_sistema',1,'p_funcion_sistema','parser.py',262),
  ('concatenar -> CONCATENAR PARA expresion COMA expresion PARC','concatenar',6,'p_concatena','parser.py',268),
  ('substraer -> SUBSTRAER PARA expresion COMA expresion COMA expresion PARC','substraer',8,'p_substraer','parser.py',274),
  ('hoy -> HOY PARA PARC','hoy',3,'p_hoy','parser.py',280),
  ('contar -> CONTAR PARA MULT PARC FROM ID WHERE condicion_where','contar',8,'p_contar','parser.py',286),
  ('suma -> SUMA PARA expresion PARC FROM ID WHERE condicion_where','suma',8,'p_suma','parser.py',292),
  ('cast -> CAST PARA expresion AS tipo PARC','cast',6,'p_cast','parser.py',300),
  ('declaracion_variable -> declaracion','declaracion_variable',1,'p_declaracion_variable','parser.py',306),
  ('declaracion_variable -> declaracion_inicializada','declaracion_variable',1,'p_declaracion_variable','parser.py',307),
  ('declaracion -> DECLARE ARROBA ID tipo','declaracion',4,'p_declaracion','parser.py',312),
  ('declaracion_inicializada -> DECLARE ARROBA ID tipo IGUAL expresion','declaracion_inicializada',6,'p_declaracion_inicializada','parser.py',317),
  ('asignacion -> ARROBA ID IGUAL expresion','asignacion',4,'p_asignacion_variable','parser.py',322),
  ('campos -> campos COMA campo','campos',3,'p_asignaciones_columnas','parser.py',327),
  ('campos -> campo','campos',1,'p_asignaciones_columnas','parser.py',328),
  ('campo -> ID IGUAL expresion','campo',3,'p_asignacion_campo','parser.py',338),
  ('crear_procedure -> CREATE PROCEDURE ID PARA parametros PARC AS','crear_procedure',7,'p_crear_procedure','parser.py',344),
  ('crear_funcion -> CREATE FUNCTION ID PARA parametros PARC RETURNS tipo AS BEGIN RETURN END','crear_funcion',12,'p_crear_funcion','parser.py',349),
  ('parametros -> parametros COMA parametro','parametros',3,'p_parametros','parser.py',354),
  ('parametros -> parametro','parametros',1,'p_parametros','parser.py',355),
  ('parametro -> ARROBA ID tipo','parametro',3,'p_parametro','parser.py',360),
  ('parametro -> empty','parametro',1,'p_parametro','parser.py',361),
  ('argumentos -> argumentos COMA argumento','argumentos',3,'p_argumentos','parser.py',366),
  ('argumentos -> argumento','argumentos',1,'p_argumentos','parser.py',367),
  ('argumento -> expresion','argumento',1,'p_argumento','parser.py',377),
  ('argumento -> empty','argumento',1,'p_argumento','parser.py',378),
  ('ejecutar_procedure -> EXEC ID argumentos','ejecutar_procedure',3,'p_ejecutar_procedure','parser.py',384),
  ('cmd_alter -> ALTER TABLE ID ADD cmd_alter_comp tipo','cmd_alter',6,'p_cmd_alter','parser.py',390),
  ('cmd_alter -> ALTER TABLE ID DROP cmd_alter_comp','cmd_alter',5,'p_cmd_alter_drop','parser.py',396),
  ('cmd_alter_comp -> COLUMN ID','cmd_alter_comp',2,'p_cmd_alter_comp','parser.py',403),
  ('cmd_alter_comp -> ID','cmd_alter_comp',1,'p_cmd_alter_comp','parser.py',404),
  ('expresion -> aritmetica','expresion',1,'p_expresion','parser.py',422),
  ('expresion -> relacional','expresion',1,'p_expresion','parser.py',423),
  ('expresion -> logica','expresion',1,'p_expresion','parser.py',424),
  ('expresion -> literal','expresion',1,'p_expresion','parser.py',425),
  ('expresion -> ID','expresion',1,'p_expresion','parser.py',426),
  ('expresion -> PARA expresion PARC','expresion',3,'p_expresion_parentesis','parser.py',432),
  ('relacional -> expresion IGUAL expresion','relacional',3,'p_expresion_relacional','parser.py',438),
  ('relacional -> expresion IGUALDAD expresion','relacional',3,'p_expresion_relacional','parser.py',439),
  ('relacional -> expresion DESIGUALDAD expresion','relacional',3,'p_expresion_relacional','parser.py',440),
  ('relacional -> expresion MENOR expresion','relacional',3,'p_expresion_relacional','parser.py',441),
  ('relacional -> expresion MAYOR expresion','relacional',3,'p_expresion_relacional','parser.py',442),
  ('relacional -> expresion MENOR_IGUAL expresion','relacional',3,'p_expresion_relacional','parser.py',443),
  ('relacional -> expresion MAYOR_IGUAL expresion','relacional',3,'p_expresion_relacional','parser.py',444),
  ('aritmetica -> expresion SUMAR expresion','aritmetica',3,'p_expresion_aritmetica','parser.py',461),
  ('aritmetica -> expresion RESTAR expresion','aritmetica',3,'p_expresion_aritmetica','parser.py',462),
  ('aritmetica -> expresion MULT expresion','aritmetica',3,'p_expresion_aritmetica','parser.py',463),
  ('aritmetica -> expresion DIV expresion','aritmetica',3,'p_expresion_aritmetica','parser.py',464),
  ('aritmetica -> RESTAR expresion','aritmetica',2,'p_expresion_unaria','parser.py',477),
  ('logica -> NEGACION expresion','logica',2,'p_expresion_logica','parser.py',483),
  ('logica -> expresion OR expresion','logica',3,'p_expresion_logica','parser.py',484),
  ('logica -> expresion AND expresion','logica',3,'p_expresion_logica','parser.py',485),
  ('literal -> ENTERO','literal',1,'p_entero','parser.py',496),
  ('literal -> CADENA','literal',1,'p_cadena','parser.py',502),
  ('literal -> FLOAT','literal',1,'p_decimal','parser.py',508),
  ('tipo -> INT','tipo',1,'p_tipo','parser.py',514),
  ('tipo -> BIT','tipo',1,'p_tipo','parser.py',515),
  ('tipo -> DECIMAL','tipo',1,'p_tipo','parser.py',516),
  ('tipo -> DATE','tipo',1,'p_tipo','parser.py',517),
  ('tipo -> DATETIME','tipo',1,'p_tipo','parser.py',518),
  ('tipo -> NCHAR comp_n','tipo',2,'p_tipo','parser.py',519),
  ('tipo -> NVARCHAR comp_n','tipo',2,'p_tipo','parser.py',520),
  ('comp_n -> PARA literal PARC','comp_n',3,'p_comp_n','parser.py',539),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',545),
]
