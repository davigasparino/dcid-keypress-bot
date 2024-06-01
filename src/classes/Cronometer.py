import tkinter as tk
import time

class Cronometer:
    def __init__(self):
        self.tempo_inicial = 0
        self.tempo_atual = 0
        self.executando = False

    def iniciar(self):
        if not self.executando:
            self.tempo_inicial = time.time()
            self.executando = True
            print('-------> Iniciado')

    def parar(self):
        if self.executando:
            self.tempo_atual += time.time() - self.tempo_inicial
            self.executando = False
            print('-------> Finalizado')

    def obter_tempo_formatado(self):
        minutos, segundos = divmod(int(self.tempo_atual), 60)
        horas, minutos = divmod(minutos, 60)
        return f"{horas:02}:{minutos:02}:{segundos:02}"