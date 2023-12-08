from enum import Enum

class TipoDato(Enum):
    INT = 1
    BIT = 2
    DECIMAL = 3
    DATE = 4
    DATETIME = 5
    NCHAR = 6
    NVARCHAR = 7

class TipoAritmetica(Enum):
    SUMA = 1
    RESTA = 2
    MULTIPLICACION = 3
    DIVISION = 4

class TipoRelacional(Enum):
    IGUALDAD = 1
    DESIGUALDAD = 2
    MENOR_IGUAL = 3
    MAYOR_IGUAL = 4
    MENOR = 5
    MAYOR = 6

class TipoLogico(Enum):
    NOT = 1
    AND = 2
    OR = 3