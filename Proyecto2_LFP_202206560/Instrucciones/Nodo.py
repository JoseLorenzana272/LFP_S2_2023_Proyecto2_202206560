from graphviz import Digraph

class Nodo:
    def __init__(self, etiqueta):
        self.etiqueta = etiqueta
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)