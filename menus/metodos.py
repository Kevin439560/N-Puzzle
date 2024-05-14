from assets.node import node
from assets.tab_move import tab_move
from assets.utility import utility
from algorithms.busca_em_largura import busca_em_largura as BFS

class metodos:
    def __init__(self):
        pass
    
    def busca_em_largura(self,estado_inicial, estado_final):
        caminho = []
        solver = BFS()
        caminho = solver.solve(estado_inicial, estado_final)
        
        if caminho is not None:
            print("Caminho da resolução: " + caminho)    
        else:
            print("Não foi encontrada solução")
    
    def BPI(puzzle):
        return
    def BAW(puzzle):
        return
    def BAM(puzzle):
        return