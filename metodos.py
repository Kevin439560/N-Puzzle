from assets.node import node
from assets.tab_move import tab_move
from assets.utility import utility
from algorithms.busca_em_largura import busca_em_largura as BFS

class metodos:
    def __init__(self):
        pass
#BUSCA EM LARGURA
    def busca_em_largura(self,estado_inicial, estado_final):
        solver = BFS()
        solver.solve(estado_inicial, estado_final)
    #BUSCA EM PROFUNDIDADE ITERATIVA
    def BPI(puzzle):
        return

    #Busca A* com heurística de quantidade de peças erradas
    def BAW(puzzle):
        return

    #Busca A* com heurística de distância de Manhattan
    def BAM(puzzle):
        return