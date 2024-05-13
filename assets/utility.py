import math
import numpy as np 
from .tab import *
from .node import *

class utility:
    def __init__(self):
        pass
    
    def imprimir_matriz(self, matriz):
        print("Matriz de Nodes:")
        for linha in matriz:
            for node in linha:
                print(node, end=" ")
            print()

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
            tabuleiro = Board(int(N))
            matriz = tabuleiro.criar_matriz()
            self.imprimir_matriz(matriz)
            return tabuleiro.matriz
    
        return "O número não atende a restrição"
