from collections import deque
from assets.node import node as bfs_node
from assets.tab_move import tab_move as tab

class busca_em_largura:
    def __init__(self):
        pass
    
    def solve(self, estado_inicial, estado_final):
        fronteira = deque([bfs_node(estado_inicial)])
        explorado = set()
        
        while fronteira:
            node = fronteira.popleft()
            estado_node = bfs_node()
            valor = bfs_node.valor
            
            if valor == estado_final:
                return self.construir_caminho(node)
            
            explorado.add(valor)
            
            for acao, estado_filho in self.caminhos_possiveis(estado):
                if estado_filho not in explorado:
                    no_filho = estado_node(estado_filho, node, acao)
                    fronteira.append(no_filho)
                    explorado.add(no_filho)
            
        return None
        
    def caminhos_possiveis(self, estado):
        tab_move = tab()
        possibilidades = []
        
        possibilidades = tab.caminhos_possiveis(estado)
        
        return possibilidades
    
    def construir_caminho(self):
        return