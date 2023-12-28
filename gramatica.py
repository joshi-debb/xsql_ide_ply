ini : instrucciones

instrucciones : instrucciones instruccion
              | instruccion

instruccion : clausula PYC
            | declaracion_variable PYC
            | asignacion_variable PYC
            | crear_procedure PYC
            | ejecutar_procedure PYC
            | crear_funcion PYC
            | expresion PYC
            | sentencia_control PYC

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

declaracion_variable : declaracion

declaracion : DECLARE ARROBA ID tipo
            | DECLARE ARROBA ID AS tipo

asignacion_variable : SET ARROBA ID IGUAL expresion

crear_db : CREATE DATA BASE ID
use_db : USE ID
crear_tb : CREATE TABLE ID PARA atributos PARC
cmd_insert : INSERT INTO ID PARA columnas PARC VALUES PARA valores PARC
cmd_update : UPDATE ID SET campos WHERE condicion_where
cmd_delete : DELETE FROM ID WHERE condicion_where
cmd_drop : DROP TABLE ID
cmd_truncate : TRUNCATE TABLE ID
condicion_where : ID IGUAL expresion

cmd_alter : ALTER TABLE ID ADD COLUMN ID tipo
          | ALTER TABLE ID ADD ID tipo
          | ALTER TABLE ID DROP COLUMN ID
          | ALTER TABLE ID DROP ID

cmd_select : SELECT op_select
           | op_select

op_select : select_tabla
          | print

select_tabla : campos_select FROM nombre_tablas WHERE condicion_where_select
             | campos_select FROM nombre_tablas empty
             | MULT FROM nombre_tablas WHERE condicion_where_select
             | MULT FROM nombre_tablas

print : expresion

nombre_tablas : columnas

condicion_where_select : expresion
                       | ID BETWEEN expresion AND expresion

valores : valores COMA valor
        | valor

valor : expresion
      | empty

columnas : columnas COMA columna
         | columna

columna : ID
        | ID PUNTO ID

campos : campos COMA campo
       | campo

campo : ID IGUAL expresion

atributos : atributos COMA atributo
          | atributo

atributo : ID tipo atributo_opciones
         | ID tipo 

atributo_opciones : atributo_opciones atributo_opcion
                  | atributo_opcion

atributo_opcion : NOT NULL
                | NULL
                | PRIMARY KEY
                | REFERENCE
                | ID PARA ID PARC

funcion_sistema : concatenar
                | substraer
                | hoy
                | contar
                | suma
                | cas

concatenar : CONCATENAR PARA expresion COMA expresion PARC

substraer : SUBSTRAER PARA expresion COMA expresion COMA expresion PARC

hoy : HOY PARA PARC

contar : CONTAR PARA MULT PARC FROM nombre_tablas WHERE condicion_where_select

contar : CONTAR PARA MULT PARC FROM nombre_tablas

suma : SUMA PARA columnas PARC FROM nombre_tablas WHERE condicion_where_select
     | SUMA PARA columnas PARC FROM nombre_tablas
     | SUMA PARA MULT PARC FROM nombre_tablas WHERE condicion_where_select

cas : CAS PARA ARROBA ID AS tipo PARC

crear_funcion : CREATE FUNCTION ID PARA parametros PARC RETURN tipo AS BEGIN bloque END

crear_procedure : CREATE PROCEDURE ID PARA parametros PARC AS BEGIN bloque END

parametros : parametros COMA parametro
           | parametro

parametro : ARROBA ID tipo
          | ARROBA ID AS tipo
          | empty


ejecutar_procedure : EXEC ID argumentos
                   | EXEC ID PARA argumentos PARC

argumentos : argumentos COMA argumento
           | argumento

argumento : ARROBA ID IGUAL expresion
          | expresion
          | empty


sentencia_control : s_if
                  | s_while
                  | s_return

s_if : IF expresion BEGIN bloque END
     | IF expresion BEGIN bloque lista_else_if END
     | IF expresion BEGIN bloque lista_else_if ELSE BEGIN bloque END
     | IF expresion BEGIN bloque ELSE BEGIN bloque END

lista_else_if : lista_else_if ELSE IF expresion BEGIN bloque
              | ELSE IF expresion BEGIN bloque

s_while : WHILE expresion BEGIN bloque END

s_return : RETURN expresion

bloque : instrucciones

expresion : aritmetica
          | relacional
          | logica
          | literal
          | llamada_fnc
          | case
          | ternario
          | PARA expresion PARC
          | ARROBA ID
          | ID PUNTO ID

relacional : expresion IGUAL expresion
           | expresion IGUALDAD expresion
           | expresion DESIGUALDAD expresion
           | expresion MENOR expresion
           | expresion MAYOR expresion
           | expresion MENOR_IGUAL expresion
           | expresion MAYOR_IGUAL expresion

aritmetica : expresion SUMAR expresion
           | expresion RESTAR expresion
           | expresion MULT expresion
           | expresion DIV expresion
           | RESTAR expresion %prec UMENOS

logica : NEGACION expresion
       | expresion OR expresion
       | expresion AND expresion

literal : ENTERO
        | CADENA
        | FLOAT
        | ID
        | NULL

llamada_fnc : ID PARA argumentos PARC
            | funcion_sistema

case : CASE lista_when ELSE THEN bloque END comp_case
     | CASE lista_when END comp_case

comp_case : ID
          | empty

lista_when : lista_when c_when
           | c_when

c_when : WHEN expresion THEN bloque

ternario : IF PARA expresion COMA expresion COMA expresion PARC 

tipo : INT
     | BIT
     | DECIMAL
     | DATE
     | DATETIME
     | NCHAR
     | NVARCHAR
     | NCHAR PARA literal PARC
     | NVARCHAR PARA literal PARC

empty :
