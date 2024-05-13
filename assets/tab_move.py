class tab_move:
    def __init__(self, matriz):
        self.matriz = matriz
     
    def encontrar_vazio(self, matriz):
        for i in range(self.linhas):
            for j in range(self.colunas):
                if self.matriz[i, j].valor == '_':
                    return i, j
   
    def mover_para_cima(self, matriz):
        i, j = self.encontrar_vazio()
        if i > 0:
            self.matriz[i, j], self.matriz[i - 1, j] = self.matriz[i - 1, j], self.matriz[i, j]
        return self.matriz

    def mover_para_baixo(self, matriz):
        i, j = self.encontrar_vazio()
        if i < self.linhas - 1:
            self.matriz[i, j], self.matriz[i + 1, j] = self.matriz[i + 1, j], self.matriz[i, j]
        return self.matriz
    
    def mover_para_esquerda(self, matriz):
        i, j = self.encontrar_vazio()
        if j > 0:
            self.matriz[i, j], self.matriz[i, j - 1] = self.matriz[i, j - 1], self.matriz[i, j]
        return self.matriz
    
    def mover_para_direita(self, matriz):
        i, j = self.encontrar_vazio()
        if j < self.colunas - 1:
            self.matriz[i, j], self.matriz[i, j + 1] = self.matriz[i, j + 1], self.matriz[i, j]
        return self.matriz