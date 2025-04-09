import tkinter as tk
from tkinter import messagebox
from TorreHanoi import TorreHanoi
import time

class Lanzador:
    def __init__(self, master):
        self.master = master
        self.master.title("Torres de Hanoi")
        
        self.label = tk.Label(master, text="Ingrese el número de discos:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.start_button = tk.Button(master, text="Iniciar", command=self.iniciar_juego)
        self.start_button.pack()

        self.torre_frame = tk.Frame(master)
        self.torre_frame.pack()

        self.torres = [tk.Canvas(self.torre_frame, width=200, height=300, bg='white') for _ in range(3)]
        for i, torre in enumerate(self.torres):
            torre.grid(row=0, column=i, padx=10)

    def iniciar_juego(self):
        try:
            num_discos = int(self.entry.get())
            if num_discos <= 0:
                messagebox.showerror("Entrada inválida", "El número de discos debe ser positivo.")
                return
            self.juego = TorreHanoi(num_discos)
            self.dibujar_torres()
            self.master.after(500, self.resolver_hanoi, num_discos, 0, 1, 2)  # Llama a la resolución automática
        except ValueError:
            messagebox.showerror("Entrada inválida", "Por favor, ingrese un número válido.")

    def dibujar_torres(self):
        for torre in self.torres:
            torre.delete("all")
        for i, torre in enumerate(self.juego.torres):
            for j, disco in enumerate(torre):
                ancho = disco * 20
                x1 = 100 - ancho // 2
                x2 = 100 + ancho // 2
                y1 = 300 - (j + 1) * 20
                y2 = 300 - j * 20
                self.torres[i].create_rectangle(x1, y1, x2, y2, fill="blue")

    def resolver_hanoi(self, n, origen, auxiliar, destino):
        if n == 1:
            self.juego.mover_disco(origen, destino)
            self.dibujar_torres()
            self.master.update()
            time.sleep(0.5)  # Pausa para visualizar el movimiento
        else:
            self.resolver_hanoi(n - 1, origen, destino, auxiliar)
            self.juego.mover_disco(origen, destino)
            self.dibujar_torres()
            self.master.update()
            time.sleep(0.5)  # Pausa para visualizar el movimiento
            self.resolver_hanoi(n - 1, auxiliar, origen, destino)

if __name__ == "__main__":
    root = tk.Tk()
    app = Lanzador(root)
    root.mainloop()