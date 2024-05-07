from metodos import BL, BPI, BAW, BAM
from tab import board

print("Digite o tamanho da matriz: ")
N = input()
node_mat = []

node_mat = board(int(N))
# Imprimir a matriz
print("Matriz de Nodes:")
for linha in node_mat:
    for node in linha:
        print(node, end=" ")
    print()
print("N-Puzzle")