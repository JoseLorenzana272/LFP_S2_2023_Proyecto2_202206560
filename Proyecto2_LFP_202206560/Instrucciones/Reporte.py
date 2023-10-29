from Abstract.Abstract import Expression
import webbrowser

class Reporte(Expression):
    def __init__(self, titulo, fila, columna):
        self.titulo = titulo
        self.fila = fila
        self.columna = columna

    def obtenerTitulo(self):
        return self.titulo


    def operar(self):
        pass


    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()