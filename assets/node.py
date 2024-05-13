class Node:
    def __init__(self):
        self.identificador = None
        self.valor = None
        self.vizinhos = []

    def adicionar_vizinho(self, no_vizinho):
        self.vizinhos.append(no_vizinho) 
    
    
    def __repr__(self):
        return str(self.identificador)