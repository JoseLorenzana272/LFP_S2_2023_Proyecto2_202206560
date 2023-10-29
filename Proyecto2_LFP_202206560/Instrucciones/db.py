class Db_claves:
    def __init__(self):
        self.claves = {}

    def agregar_clave(self, clave):
        self.claves[clave] = []

    def agregar_valor(self, pos, valor):
        clave = list(self.claves.keys())[pos]
