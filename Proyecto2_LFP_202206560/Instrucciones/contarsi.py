from Abstract.Abstract import Expression

class ContarSi(Expression):
    def __init__(self, clave, numero, fila, columna):
        self.clave = clave
        self.numero = numero
        super().__init__(fila, columna)

    def operar(self):
        pass

    def contar(self, registros_dict):
        if self.clave not in registros_dict[1]:  # Verifica que la clave esté en al menos un registro
            raise Exception(f"La clave '{self.clave}' no se encuentra en ningún registro.")

        count = 0
        for registro in registros_dict.values():
            if self.clave in registro:
                if registro[self.clave] == self.numero:
                    count += 1
                    print(count)
        return count

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()