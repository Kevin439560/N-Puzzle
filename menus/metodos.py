from assets.node import node
from assets.tab_move import tab_move
from assets.utility import utility
from algorithms.busca_em_largura import busca_em_largura as BFS
from algorithms.busca_em_profundidade import busca_em_profundidade as DFS
import time

class metodos:
    def __init__(self):
        pass
    
    def busca_em_largura(self, estado_inicial, estado_final):
        caminho = []
        solver = BFS()

        start_time = time.time()
        caminho = solver.solve(estado_inicial, estado_final)
        end_time = time.time()

        tempo_gasto = end_time - start_time
        
        if caminho is not None:
            caminho_str = " -> ".join([acao for acao, estado in caminho])
            print("Caminho da resolução: " + caminho_str)
        else:
            print("Não foi encontrada solução")

        print(f"Tempo gasto: {tempo_gasto:.4f} segundos")
    
    def busca_em_profundidade(self, estado_inicial, estado_final):
        caminho = []
        solver = DFS()

        start_time = time.time()
        caminho = solver.solve(estado_inicial, estado_final)
        end_time = time.time()

        tempo_gasto = end_time - start_time
        
        if caminho is not None:
            caminho_str = " -> ".join([acao for acao, estado in caminho])
            print("Caminho da resolução: " + caminho_str)
        else:
            print("Não foi encontrada solução")

        print(f"Tempo gasto: {tempo_gasto:.4f} segundos")
    
    def BAW(self, puzzle):
        return
    
    def BAM(self, puzzle):
        return