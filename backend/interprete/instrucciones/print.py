from interprete.extra.ast import *
from interprete.extra.tipos import TipoDato
from .instruccion import Instruccion
from interprete.extra.enviroment import Enviroment
from interprete.extra.consola import Consola
from interprete.extra.retorno import Retorno3d
from interprete.extra.generador import Generador

class Print(Instruccion):
    def __init__(self, text_val:str, argumento, linea, columna):
        super().__init__(text_val, linea, columna)
        self.text_val = text_val
        self.argumento = argumento
    
    def ejecutar(self, env:Enviroment):
        exp = self.argumento.ejecutar(env)

        # Validar que no haya un error en la expresion
        if exp.tipo == TipoDato.ERROR:
            print("Semántico", f'Error en la expresión de la funcion print()', self.linea, self.columna)
            return self

        Consola.addConsola(exp.valor)
    
    def recorrerArbol(self, raiz:Nodo):
        id = AST.generarId()
        hijo = Nodo(id=id, valor='SELECT', hijos=[])
        raiz.addHijo(hijo)                                    
        self.argumento.recorrerArbol(hijo)
    
    
    
    # para el c3d
    
    def ejecutar3d(self, env:Enviroment, generador:Generador):
        codigo = '/* PRINT */\n'
        valor_exp:Retorno3d = self.argumento.ejecutar3d(env, generador)
        if valor_exp.tipo == TipoDato.INT or valor_exp.tipo == TipoDato.BIT:
            codigo += f'printf("%d", (int) {valor_exp.temporal});\n'
        
        elif valor_exp.tipo == TipoDato.DECIMAL:
            codigo += f'printf("%f",(float) {valor_exp.temporal});\n'
        elif valor_exp.tipo == TipoDato.NVARCHAR or valor_exp.tipo == TipoDato.NCHAR or valor_exp.tipo == TipoDato.DATE or valor_exp.tipo == TipoDato.DATETIME:
            etqCiclo = generador.obtenerEtiqueta()
            etqSalida = generador.obtenerEtiqueta()

            caracter = generador.obtenerTemporal()    # Temp para llevar guardar caracter
            tmp = generador.obtenerTemporal()
            codigo += f'{tmp} = {valor_exp.temporal};\n' # tmp = direccion_heap_cadena
            codigo += f'{etqCiclo}:\n' # Ln:
            codigo += f'{caracter} = heap[(int) {tmp}];\n'
            codigo += f'if ({caracter} == 0) goto {etqSalida};\n'
            codigo += f'printf("%c", (char) {caracter});\n'
            codigo += f'{tmp} = {tmp} + 1;\n'
            codigo += f'goto {etqCiclo};\n'
            codigo += f'{etqSalida}:\n'
        codigo += f'printf("\\n");\n'

        generador.agregarInstruccion(codigo)

        return codigo