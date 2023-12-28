
class Generador:
    def __init__(self) -> None:
        self.temporales = 0
        self.etiquetas = 0
        self.codigo = ''
        self.main = ''
        self.funciones = ''
        
    
    def obtenerTemporal(self) -> str:
        temporal = 't' + str(self.temporales)
        self.temporales += 1
        return temporal
    
    def obtenerEtiqueta(self) -> str:
        etiqueta = 'L' + str(self.etiquetas)
        self.etiquetas += 1
        return etiqueta
    
    def agregarInstruccion(self, instruccion: str) -> None:
        self.main += instruccion + '\n'
        
    def generate_main(self) -> str:
        codigo = self.generarEncabezado()
        codigo += self.codigo + "\n"
        codigo += 'int main() {\n' + f'{self.main}\n' + f'return 0;' + "\n}"
        return codigo
    
    def agregarFuncion(self, codigo_fnc):
        self.funciones += codigo_fnc + '\n'
    
    def reiniciarGenerador(self):
        self.temporales = 0
        self.etiquetas = 0
        self.codigo = ''
        self.main = ''
        
    def generarEncabezado(self) -> str:
        encabezado = ""
        
        encabezado += '\n'
        encabezado += '#include <stdio.h>\n'
        encabezado += 'float stack[10000];\n'
        encabezado += 'float heap[10000];\n'
        encabezado += 'int SP = 0;\n'
        encabezado += 'int HP = 0;\n'
        

        if self.temporales > 0:
            encabezado += 'float '
        # imprimir temporales:
        for i in range(0, self.temporales):
            encabezado += f't{i}'
            if i < self.temporales-1:
                encabezado += ", "
        encabezado += ';\n\n'

        return encabezado