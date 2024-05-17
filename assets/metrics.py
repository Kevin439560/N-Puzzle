import time

class Metrics:
    def __init__(self):
        self.max_memoria = 0
        self.nos_expandidos = 0
        self.total_filhos = 0
        self.start_time = None
        self.end_time = None

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        self.end_time = time.time()

    def update_max_memoria(self, fronteira_len, explorado_len):
        self.max_memoria = max(self.max_memoria, fronteira_len + explorado_len)

    def increment_nos_expandidos(self):
        self.nos_expandidos += 1

    def add_filhos(self, num_filhos):
        self.total_filhos += num_filhos

    def fator_ramificacao_media(self):
        if self.nos_expandidos > 0:
            return self.total_filhos / self.nos_expandidos
        return 0

    def tempo_gasto(self):
        if self.start_time is not None and self.end_time is not None:
            return self.end_time - self.start_time
        return 0

    def print_metrics(self):
        print(f"Nós expandidos: {self.nos_expandidos}")
        print(f"Memória máxima usada: {self.max_memoria}")
        print(f"Fator de ramificação média: {self.fator_ramificacao_media()}")
        print(f"Tempo gasto: {self.tempo_gasto():.4f} segundos")
