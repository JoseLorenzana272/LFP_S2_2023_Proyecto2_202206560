from Abstract.Abstract import Expression
from tabulate import tabulate

class Datos(Expression):
    def __init__(self, fila, columna):
        super().__init__(fila, columna)

    def operar(self, arbol):
        pass

    def ejecutarT(self, registros_dict):

        data = [list(registro.values()) for registro in registros_dict.values()]

        keys = list(registros_dict[1].keys())

        return tabulate(data, headers=keys, tablefmt="simple")

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()