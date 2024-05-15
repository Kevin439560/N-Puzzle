import math
import numpy as np 
from .tab import *
from .node import *

class utility:
    def __init__(self):
        pass
    
    def imprimir_matriz(self, matriz):
        print("Matriz:")
        for linha in matriz:
            print(" ".join(str(node) for node in linha))

    def verifica_zeros_apos_virgula(self, numero):
        partes = str(numero).split('.')
        if len(partes) == 2:  # Verifica se o número possui parte decimal
            parte_decimal = partes[1]
            if all(digito == '0' for digito in parte_decimal):
                return True
        return False
        
    def gerar_matriz(self):
        print("Envie o tamanho das peças")
        N = input()
        verificacao = math.sqrt(int(N)+1)
    
        if self.verifica_zeros_apos_virgula(verificacao):
            tabuleiro = board(int(N))
            matriz = tabuleiro.criar_matriz()
            matriz = np.array(matriz, dtype=str)  # Converter matriz para string
            self.imprimir_matriz(matriz)
            return matriz  # Retorna a matriz diretamente
    
        return "O número não atende a restrição"
    
    def embaralhar_matriz(self, matriz):
        linhas, colunas = matriz.shape
        
        valores_matriz = matriz.flatten().tolist()
        random.shuffle(valores_matriz)
        
        matriz_embaralhada = np.array(valores_matriz, dtype=str).reshape((linhas, colunas))
        
        self.imprimir_matriz(matriz_embaralhada)
        
        return matriz_embaralhada
