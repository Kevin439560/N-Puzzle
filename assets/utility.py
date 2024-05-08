import math
import numpy as np 
#from metodos import BL, BPI, BAW, BAM
from .tab import *
from .node import *

def gerar_matriz():
    print("Envie o tamanho das peças")
    N = input()
    verificacao = math.sqrt(int(N)+1)
    
    if verifica_zeros_apos_virgula(verificacao):
        tabuleiro = Board(int(N))
        imprimir_matriz(tabuleiro.matriz)
    else:
        print("O número não atende a restrição.")

def imprimir_matriz(matriz):
    print("Matriz de Nodes:")
    for linha in matriz:
        for node in linha:
            print(node, end=" ")
        print()

def verifica_zeros_apos_virgula(numero):
    partes = str(numero).split('.')
    if len(partes) == 2:  # Verifica se o número possui parte decimal
        parte_decimal = partes[1]
        if all(digito == '0' for digito in parte_decimal):
            return True
    return False