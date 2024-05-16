import numpy as np
from collections import deque
from assets.node import node as bfs_node
from assets.tab_move import tab_move as tab

class busca_em_largura:
    def __init__(self):
        pass
    
    def solve(self, estado_inicial, estado_final):
        estado_final = np.array(estado_final, dtype=str)
        fronteira = deque([bfs_node(np.array(estado_inicial, dtype=str))])
        explorado = set()
        max_memoria = 0  # Para rastrear a memória máxima
        nos_expandidos = 0  # Para rastrear o número de nós expandidos
        total_filhos = 0  # Para rastrear o total de filhos gerados

        while fronteira:
            max_memoria = max(max_memoria, len(fronteira) + len(explorado))
            node = fronteira.popleft()
            valor = node.valor

            print("Estado atual (valor):")
            print(np.array(valor))
            print("Estado final:")
            print(np.array(estado_final))

            if np.array_equal(valor, estado_final):
                print("Solução encontrada")
                print(f"Nós expandidos: {nos_expandidos}")
                print(f"Memória máxima usada: {max_memoria}")
                if nos_expandidos > 0:
                    fator_ramificacao_media = total_filhos / nos_expandidos
                else:
                    fator_ramificacao_media = 0
                print(f"Fator de ramificação média: {fator_ramificacao_media}")
                return self.construir_caminho(node)
            
            explorado.add(tuple(map(tuple, valor)))
            nos_expandidos += 1  # Incrementa o contador de nós expandidos

            filhos = list(self.caminhos_possiveis(valor))
            total_filhos += len(filhos)  # Incrementa o total de filhos gerados

            for acao, estado_filho in filhos:
                estado_filho_tupla = tuple(map(tuple, estado_filho))
                
                if estado_filho_tupla not in explorado:
                    no_filho = bfs_node(estado_filho, node, acao)
                    fronteira.append(no_filho)
                    explorado.add(estado_filho_tupla)
            
        print(f"Nós expandidos: {nos_expandidos}")
        print(f"Memória máxima usada: {max_memoria}")
        if nos_expandidos > 0:
            fator_ramificacao_media = total_filhos / nos_expandidos
        else:
            fator_ramificacao_media = 0
        print(f"Fator de ramificação média: {fator_ramificacao_media}")
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
