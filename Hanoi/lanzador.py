import tkinter as tk
from tkinter import messagebox
from TorreHanoi import TorreHanoi

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
                raise ValueError("El número de discos debe ser positivo.")
            self.juego = TorreHanoi(num_discos)
            self.dibujar_torres()
        except ValueError as e:
            messagebox.showerror("Entrada inválida", str(e))

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

if __name__ == "__main__":
    root = tk.Tk()
    app = Lanzador(root)
    root.mainloop()