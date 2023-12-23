from subprocess import check_call
from interprete.extra.consola import Consola

class Nodo:
    # id -> Identificador del dodo
    # valor -> Contenido del nodo
    # hijos -> Arreglo de 'n' hijos
    def __init__(self, id, valor:str, hijos):
        self.id = id
        self.valor = valor
        self.hijos = hijos
    
    def addHijo(self, nodoHijo):
        self.hijos.append(nodoHijo)
    
    def getId(self):
        return self.id
    
    def getValor(self):
        return self.valor
    
    def getHijos(self):
        return self.hijos

class AST:
    id:int = 0
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones
    
    def getAST(self):
        declaraciones = ''
        conexiones = ''
        raiz = Nodo(id=0, valor='INSTRUCCIONES', hijos=[])

        for instruccion in self.instrucciones:
            instruccion.recorrerArbol(raiz)
        declaraciones = f'\t{raiz.getId()} [label = "{raiz.getValor()}"];\n'
        declaraciones, conexiones = self.graficarArbol(raiz, declaraciones, conexiones)
        dot = 'digraph {\n' + declaraciones + conexiones + '}\n'
        
        filename = "backend/AST.dot"

        archivo = open(filename, "w")
        archivo.write(dot)
        archivo.close()
        
        check_call(['dot','-Tpng',filename,'-o', "backend/AST.png"])
        Consola.addConsola('AST generado con éxito.')
        return {'dot': dot}

    def graficarArbol(self, raiz:Nodo, declaraciones:str, conexiones:str):
        for hijo in raiz.getHijos():
            declaraciones += f'\t{hijo.getId()} [label = "{hijo.getValor()}"];\n'
            conexiones += f'\t{raiz.getId()} -> {hijo.getId()};\n'
            declaraciones, conexiones = self.graficarArbol(hijo, declaraciones, conexiones)
        return declaraciones, conexiones

    @classmethod
    def generarId(cls):
        cls.id += 1
        return cls.id
    