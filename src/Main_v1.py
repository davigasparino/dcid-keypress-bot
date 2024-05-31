import tkinter as tk
import threading

def iniciar_loop():
    # Função que será executada em loop infinito
    while True:
        print("Loop infinito...")

def parar_loop():
    # Função para interromper o loop
    global loop_thread
    loop_thread.join()  # Aguarda até que o loop termine
    print("Loop interrompido!")

root = tk.Tk()

# Botão "Play"
play_button = tk.Button(root, text="Play", command=lambda: iniciar_loop_thread())
play_button.pack()

# Botão "Stop"
stop_button = tk.Button(root, text="Stop", command=parar_loop)
stop_button.pack()

def iniciar_loop_thread():
    global loop_thread
    loop_thread = threading.Thread(target=iniciar_loop)
    loop_thread.start()

root.mainloop()
