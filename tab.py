import math
import random
from assets.node import Node
import numpy as np 

def board(N):
    lines = 1
    col = 1
  
    linhas = int(math.sqrt(N + 1))
    colunas = int(math.sqrt(N + 1))
    
    matriz = np.empty((linhas, colunas), dtype=object)
    identificador = 0
    
    for i in range(linhas):
        for j in range(colunas):
            matriz[i, j] = Node(identificador, random.randint(1, 100))  # Exemplo de valor aleatório
            identificador += 1
    
    # Adicionar vizinhos
    for i in range(linhas):
        for j in range(colunas):
            if i > 0:
                matriz[i, j].adicionar_vizinho(matriz[i - 1, j])  # Vizinho acima
            if i < linhas - 1:
                matriz[i, j].adicionar_vizinho(matriz[i + 1, j])  # Vizinho abaixo
            if j > 0:
                matriz[i, j].adicionar_vizinho(matriz[i, j - 1])  # Vizinho à esquerda
            if j < colunas - 1:
                matriz[i, j].adicionar_vizinho(matriz[i, j + 1])  # Vizinho à direita
    
    return matriz