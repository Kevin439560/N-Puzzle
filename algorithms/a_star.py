import numpy as np
from collections import deque
from assets.node import node as bfs_node
from assets.utility import utility as heuristicas
from assets.tab_move import tab_move as tab
import heapq

class a_star:
    def __init__(self, heuristica):
        self.heuristica = heuristica
    
    def solve(self, estado_inicial, estado_final):
        estado_inicial_node = bfs_node(valor=np.array(estado_inicial, dtype=str))
        estado_inicial_node.f = self.heuristica
        fronteira = []
        heapq.heappush(fronteira, estado_inicial_node)
        explorado = set()
        
        estado_inicial_str = self.estado_to_str(estado_inicial)
        g_score = {estado_inicial_str: 0}
        f_score = {estado_inicial_str: self.heuristica}
        
        total_filhos = 0
        while fronteira:
            atual_node = heapq.heappop(fronteira)
            valor = atual_node.valor
            
            print("Atual")
            print(valor)
            
            if np.array_equal(valor, estado_final):
                return self.construir_caminho(atual_node)
            
            explorado.add(tuple(map(tuple, valor)))
            
            filhos = list(self.caminhos_possiveis(valor))
            
            total_filhos += len(filhos)
            
            for acao, estado_filho in filhos:
                estado_filho_tupla = tuple(map(tuple, estado_filho))
                tentativa_g_score = g_score[str(valor.tolist())] + 1

                if estado_filho_tupla not in explorado or tentativa_g_score < g_score.get(str(estado_filho.tolist()), float('inf')):
                    g_score[str(estado_filho.tolist())] = tentativa_g_score
                    f_score[str(estado_filho.tolist())] = tentativa_g_score + self.heuristica
                    no_filho = bfs_node(valor=estado_filho, pai=atual_node, acao=acao, g=tentativa_g_score, f=f_score[str(estado_filho.tolist())])
                    heapq.heappush(fronteira, no_filho)
                    explorado.add(estado_filho_tupla)
                    
        return None
        
    def estado_to_str(self, estado):
        return str(estado.tolist())
    
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
        