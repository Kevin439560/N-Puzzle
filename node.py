class Node:
    def __init__(self, identificador, valor):
        self.identificador = identificador
        self.valor = valor
        self.vizinhos = []

    def adicionar_vizinho(self, no_vizinho):
        self.vizinhos.append(no_vizinho) 
        
    def __repr__(self):
        return str(self.identificador)