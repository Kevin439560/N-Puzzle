import math
import random
from .node import Node
import numpy as np 

class Board:
    def __init__(self, N):
        self.N = N
        self.linhas, self.colunas = self.calcular_dimensoes(N)
        self.matriz = self.criar_matriz()

    def calcular_dimensoes(self, N):
        dimensoes = 1
        while dimensoes * dimensoes < N:
            dimensoes += 1
        return dimensoes, dimensoes

    def criar_matriz(self):
        matriz = np.empty((self.linhas, self.colunas), dtype=object)
        valores_unicos = list(range(1, self.N + 1))
        random.shuffle(valores_unicos)
        valores_unicos.append('_')  # Adiciona o espaço vazio representado por um underline
        random.shuffle(valores_unicos)  # Embaralha novamente para garantir que o espaço vazio seja aleatório
        
        indice_valor = 0
        for i in range(self.linhas):
            for j in range(self.colunas):
                matriz[i, j] = Node(valores_unicos[indice_valor], valores_unicos[indice_valor])
                indice_valor += 1
        
        return matriz