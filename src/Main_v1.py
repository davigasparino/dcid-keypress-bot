import tkinter as tk
import time

class Cronometro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro")

        self.tempo_inicial = 0
        self.tempo_atual = 0
        self.executando = False

        self.label_tempo = tk.Label(root, font=("Helvetica", 24))
        self.label_tempo.pack()

    def iniciar_cronometro(self):
        if not self.executando:
            self.tempo_inicial = time.time()
            self.executando = True
            self.atualizar_cronometro()

    def parar_cronometro(self):
        if self.executando:
            self.tempo_atual += time.time() - self.tempo_inicial
            self.executando = False

    def atualizar_cronometro(self):
        if self.executando:
            self.tempo_atual = time.time() - self.tempo_inicial

        minutos, segundos = divmod(int(self.tempo_atual), 60)
        horas, minutos = divmod(minutos, 60)
        self.label_tempo.config(text=f"{horas:02}:{minutos:02}:{segundos:02}")

        self.root.after(1000, self.atualizar_cronometro)

def iniciar_cronometro():
    cronometro.iniciar_cronometro()

def parar_cronometro():
    cronometro.parar_cronometro()

if __name__ == "__main__":
    root = tk.Tk()
    cronometro = Cronometro(root)

    botao_play = tk.Button(root, text="Play", command=iniciar_cronometro)
    botao_play.pack()

    botao_stop = tk.Button(root, text="Stop", command=parar_cronometro)
    botao_stop.pack()

    root.mainloop()
