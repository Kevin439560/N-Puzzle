import numpy as np
from assets.utility import utility
from collections import deque
from assets.node import node as bfs_node
from assets.tab_move import tab_move as tab

class busca_em_largura:
    def __init__(self):
        pass
    
    def solve(self, estado_inicial, estado_final):
        fronteira = deque([bfs_node(estado_inicial)])
        print("Estao inicial")
        print(estado_inicial)
        explorado = set()
        util = utility()
        print(fronteira)
        while fronteira:
            node = fronteira.popleft()
            valor = node.valor
            #print("Nó atual:", util.imprimir_matriz(valor))
            print(valor)
            if np.array_equal(valor, estado_final):
                print("Entrou no primeiro condicional")
                return self.construir_caminho(node)
            
            explorado.add(tuple(map(tuple, valor)))
            
            for acao, estado_filho in self.caminhos_possiveis(valor):
                estado_filho_tupla = tuple(map(tuple, estado_filho))
                
                if estado_filho_tupla not in explorado:
                    print("Entrou no segundo condicional")
                    no_filho = bfs_node(estado_filho, node, acao)
                    fronteira.append(no_filho)
                    explorado.add(estado_filho_tupla)
            
        return None
        
    def caminhos_possiveis(self, estado):
        tab_move = tab(estado)
        return tab_move.caminhos_possiveis(estado)
    
    def construir_caminho(self, node):
        caminho = []
        
        while node.pai:
            caminho.append((node.acao, node.valor))
            node = node.pai
            
        caminho.reverse()
        return caminho
