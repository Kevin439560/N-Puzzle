class node:
    def __init__(self, valor, pai = None, acao = None, profundidade = 0):
        self.valor = valor
        self.pai = pai
        self.acao = acao
        self.profundidade = profundidade