from Abstract.Abstract import Expression

class Contar(Expression):
    def __init__(self, fila, columna):
        super().__init__(fila, columna)

    def operar(self, arbol):
        pass

    def ejecutarT(self, registros_dict):
        total_registros = sum(len(diccionario) for diccionario in registros_dict.values())
        return total_registros

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()
