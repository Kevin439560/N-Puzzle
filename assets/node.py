class node:
    def __init__(self, valor, pai=None, acao=None, profundidade = 0, g=0, f=0):
        self.valor = valor
        self.pai = pai
        self.acao = acao
        self.profundidade = profundidade
        self.g = g  # custo do caminho do estado inicial até este nó
        self.f = f # custo estimado total (g + h)

    def __lt__(self, other):
        return self.f < other.f
