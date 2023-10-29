from Abstract.Abstract import Expression

class ImprimirLn(Expression):

        def __init__(self, texto, fila, columna):
            self.texto = texto
            super().__init__(fila, columna)

        def operar(self, arbol):
            pass

        def ejecutarT(self):
            texto_salto = '\n' + self.texto
            return texto_salto

        def getFila(self):
            return super().getFila()

        def getColumna(self):
            return super().getColumna()