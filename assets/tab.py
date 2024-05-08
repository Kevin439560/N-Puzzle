import math
import random
from .node import Node
import numpy as np 

class Board:
    def __init__(self, N):
        self.N = N
        self.linhas = int(math.sqrt(N + 1))
        self.colunas = int(math.sqrt(N + 1))
        self.matriz = self.criar_matriz()

    def criar_matriz(self):
        matriz = np.empty((self.linhas, self.colunas), dtype=object)
        valor = 1
        
        for i in range(self.linhas):
            for j in range(self.colunas):
                matriz[i, j] = Node(valor, random.randint(2, 100))  # Exemplo de valor aleatório
                valor += 1
        
        # Adicionar vizinhos
        for i in range(self.linhas):
            for j in range(self.colunas):
                if i > 0:
                    matriz[i, j].adicionar_vizinho(matriz[i - 1, j])  # Vizinho acima
                if i < self.linhas - 1:
                    matriz[i, j].adicionar_vizinho(matriz[i + 1, j])  # Vizinho abaixo
                if j > 0:
                    matriz[i, j].adicionar_vizinho(matriz[i, j - 1])  # Vizinho à esquerda
                if j < self.colunas - 1:
                    matriz[i, j].adicionar_vizinho(matriz[i, j + 1])  # Vizinho à direita
        
        return matriz