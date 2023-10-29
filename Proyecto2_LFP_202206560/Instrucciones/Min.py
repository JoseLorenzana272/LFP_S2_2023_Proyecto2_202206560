from Abstract.Abstract import Expression

class Min(Expression):
    def __init__(self, clave, fila, columna):
        self.clave = clave
        super().__init__(fila, columna)

    def operar(self):
        pass

    def ejecutarT(self, registros_dict):
        if self.clave not in registros_dict[1]:  # Verifica que la clave esté en al menos un registro
            raise Exception(f"La clave '{self.clave}' no se encuentra en ningún registro.")

        valores_clave = [registro[self.clave] for registro in registros_dict.values()]
        maximo = min(valores_clave)
        return maximo


    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()