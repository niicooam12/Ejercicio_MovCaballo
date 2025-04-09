import tkinter as tk
from MovsCaballo import MovsCaballo

class CaballoGUI:
    def __init__(self, tam_tablero=8):
        self.tam_tablero = tam_tablero
        self.size = 600 // tam_tablero  # Tamaño de cada celda
        self.root = tk.Tk()
        self.root.title("Recorrido del Caballo")
        self.canvas = tk.Canvas(self.root, width=600, height=600)
        self.canvas.pack()
        self.caballo = MovsCaballo(tam_tablero)
        self.movimientos = self.caballo.resolver()
        self.celdas = {}  # Diccionario para almacenar las celdas del tablero
        self.dibujar_tablero()
        self.caballo_icon = None
        self.animar_movimientos()

    def dibujar_tablero(self):
        """Dibuja el tablero de ajedrez."""
        for i in range(self.tam_tablero):
            for j in range(self.tam_tablero):
                rect = self.canvas.create_rectangle(
                    j * self.size, i * self.size,
                    (j + 1) * self.size, (i + 1) * self.size,
                    fill="white", outline="black"
                )
                self.celdas[(i, j)] = rect

    def animar_movimientos(self):
        """Anima los movimientos del caballo."""
        for paso in range(len(self.movimientos) - 1):
            x1, y1 = self.movimientos[paso]
            x2, y2 = self.movimientos[paso + 1]
            self.root.after(paso * 500, self.mover_caballo, x1, y1, x2, y2)  # 500 ms entre movimientos

    def mover_caballo(self, x1, y1, x2, y2):
        """Mueve el caballo y deja un rastro."""
        # Cambiar la celda a gris para marcar que el caballo pasó por ella
        self.canvas.itemconfig(self.celdas[(x1, y1)], fill="gray")

        # Dibujar una línea desde la posición anterior a la nueva
        self.canvas.create_line(
            y1 * self.size + self.size // 2, x1 * self.size + self.size // 2,
            y2 * self.size + self.size // 2, x2 * self.size + self.size // 2,
            fill="blue", width=2
        )

        # Dibujar el caballo en la nueva posición
        if self.caballo_icon:
            self.canvas.delete(self.caballo_icon)  # Elimina el caballo anterior
        self.caballo_icon = self.canvas.create_oval(
            y2 * self.size + self.size // 4, x2 * self.size + self.size // 4,
            (y2 + 1) * self.size - self.size // 4, (x2 + 1) * self.size - self.size // 4,
            fill="black"
        )

    def iniciar(self):
        self.root.mainloop()


