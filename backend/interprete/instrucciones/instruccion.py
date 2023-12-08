
class Instruccion:
    def __init__(self, linea: int, columna: int) -> None:
        self.linea: int = linea;
        self.columna: int = columna;

    def ejecutar(self):
        pass