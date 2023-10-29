from Abstract.Abstract import Expression

#HICE ESTOOOOOOOOOOOOOOOOO
class DeclaracionRegistros(Expression):

    def __init__(self, nombre, registros, fila, columna):
        self.nombre = nombre
        self.registros = registros
        super().__init__(fila, columna)

    def operar(self, arbol):
        pass

    def ejecutarT(self):
        return self.registros

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()