class tab_move:
    def __init__(self, matriz):
        self.atualizar_dimensoes(matriz)
        self.matriz = matriz
        
    def atualizar_dimensoes(self, matriz):
        self.linhas, self.colunas = matriz.shape
        
    def encontrar_vazio(self, matriz):
        for i in range(self.linhas):
            for j in range(self.colunas):
                if matriz[i, j] == '_':
                    return i, j
   
    def mover_para_cima(self, matriz):
        i, j = self.encontrar_vazio(matriz)
        if i > 0:
            matriz[i, j], matriz[i - 1, j] = matriz[i - 1, j], matriz[i, j]
        return matriz

    def mover_para_baixo(self, matriz):
        i, j = self.encontrar_vazio(matriz)
        if i < self.linhas - 1:
            matriz[i, j], matriz[i + 1, j] = matriz[i + 1, j], matriz[i, j]
        return matriz
    
    def mover_para_esquerda(self, matriz):
        i, j = self.encontrar_vazio(matriz)
        if j > 0:
            matriz[i, j], matriz[i, j - 1] = matriz[i, j - 1], matriz[i, j]
        return matriz
    
    def mover_para_direita(self, matriz):
        i, j = self.encontrar_vazio(matriz)
        if j < self.colunas - 1:
            matriz[i, j], matriz[i, j + 1] = matriz[i, j + 1], matriz[i, j]
        return matriz
    
    def caminhos_possiveis(self, matriz):
        possibilidades = []
        
        possibilidade = matriz.copy()
        if self.mover_para_cima(possibilidade) != matriz:
            possibilidades.append(self.mover_para_cima(possibilidade))

        possibilidade = matriz.copy()
        if self.mover_para_baixo(possibilidade) != matriz:
            possibilidades.append(self.mover_para_baixo(possibilidade))
            
        possibilidade = matriz.copy()
        if self.mover_para_esquerda(possibilidade) != matriz:
            possibilidades.append(self.mover_para_esquerda(possibilidade))
        
        possibilidade = matriz.copy()
        if self.mover_para_direita(possibilidade) != matriz:
            possibilidades.append(self.mover_para_direita(possibilidade))
            
        return possibilidades