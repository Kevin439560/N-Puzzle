from assets.node import Node
from assets.tab_move import tab_move
from assets.utility import utility

class Metodos:
    def __init__(self):
        pass
#BUSCA EM LARGURA
    def busca_em_largura(self,estado_inicial):
        #node = Node()
        #node = estado_inicial
        util = utility()
        move = tab_move(estado_inicial)       
        nova_matriz = move.mover_para_cima(estado_inicial)
        
        util.imprimir_matriz(nova_matriz)

    #BUSCA EM PROFUNDIDADE ITERATIVA
    def BPI(puzzle):
        return

    #Busca A* com heurística de quantidade de peças erradas
    def BAW(puzzle):
        return

    #Busca A* com heurística de distância de Manhattan
    def BAM(puzzle):
        return