from metodos import metodos as metodos_module
from assets.utility import utility

class menu:
    def __init__(self):
        self.cases = {
            1: self.caseBL,
            2: self.caseBPI,
            3: self.caseBAW,
            4: self.caseBAM
        }
    
    def switch(self, case):
        if case in self.cases:
            # Se a chave estiver presente, chama a função associada à chave
            self.cases[case]()
        else:
            # Se a chave não estiver presente, imprime 'Caso inválido'
            print("Caso inválido")
    
    def caseBL(self):
        metodos = metodos_module()      
        util = utility() 
        matriz_gerada = util.gerar_matriz()
        matriz_embaralhada = util.embaralhar_matriz()
        metodos.busca_em_largura(matriz_gerada, matriz_embaralhada)
        
        print("BL")
    
    def caseBPI():
        print("BPI")
    
    def caseBAW():
        print("BAW")
    
    def caseBAM():
        print("BAM")