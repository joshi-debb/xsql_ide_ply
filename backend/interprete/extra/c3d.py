

class Traduccion:
    def __init__(self):
        self.tmp:int = 0
        self.label:int = 0
        self.list_tmp:[str] = []
        self.list_main:[str] = [] # Esta lista almacena el entorno main
        self.index_stack:int = 0 # Este indice lleva el control de la pila de stack
        self.list_funcs:[str] = [] # Esta lista almacena el entorndo de las funciones
        self.is_main:bool = True
        self.list_c3d:[str] = [] # Esta lista almacena el codigo 3d
    
    def get_new_tmp(self):
        temporal = 't' + str(self.tmp)
        self.tmp += 1
        self.list_tmp.append(temporal)
        return temporal
        
    def get_index_stack(self):
        new_stack = self.index_stack
        self.index_stack += 1
        return new_stack
    
    def set_stack(self, index, temporal, esdeclaracion):
        if self.is_main:
            if esdeclaracion:
                self.list_main.append('stack[' + str(index) + '] = ' + temporal + ';\n')
            else:
                self.list_main.append('stack[' + str(index) + ']' + ';\n')
        else:
            if esdeclaracion:
                self.list_funcs.append('stack[' + str(index) + '] = ' + temporal + ';\n')
            else:
                self.list_funcs.append('stack[' + str(index) + ']' + ';\n')
            
            
    def get_stack(self, index, temporal):
        if self.is_main:
            self.list_main.append(temporal + ' = stack[' + str(index) + '];\n')
        else:
            self.list_funcs.append(temporal + ' = stack[' + str(index) + '];\n')
        
    def Print(self, temporal, tipo):
        if self.is_main:
            self.list_main.append('printf("%' + tipo + '", ' + temporal + ');\n')
            self.list_main.append('printf("%' + 'c' + '", ' + '10' + ');\n')
        else:
            self.list_funcs.append('printf("%' + tipo + '", ' + temporal + ');\n')
            self.list_funcs.append('printf("%' + 'c' + '", ' + '10' + ');\n')

    def generate_render(self) -> [str]:
        
        encabezado = '#include <stdio.h>\n'
        encabezado += 'float P, H;\n'
        encabezado += 'float stack[100000];\n'
        encabezado += 'float heap[100000];\n'
        
        lista = []
        lista.append(encabezado)
        if len(self.list_tmp) != 0:
            temporal = 'float ' + ", ".join(self.list_tmp) + ';\n'
            lista.append(temporal)
            
        if len(self.list_funcs) != 0:
            for i in self.list_funcs:
                lista.append(i)
                
        lista.append('int main(){\n')
        
        if len(self.list_main) != 0:
            for i in self.list_main:
                lista.append(i)      

        lista.append('return 0;\n')
        lista.append('}')
                
        return lista

            