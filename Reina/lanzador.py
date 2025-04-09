import tkinter as tk
from reina import NReinas

class NReinasGUI:
    def __init__(self, n):
        self.n = n
        self.size = 600 // n  # Tamaño de cada celda
        self.root = tk.Tk()
        self.root.title(f"{n} Reinas")
        self.canvas = tk.Canvas(self.root, width=600, height=600)
        self.canvas.pack()
        self.reinas = NReinas(n)
        self.tablero = self.reinas.obtener_tablero()
        self.dibujar_tablero()

    def dibujar_tablero(self):
        """Dibuja el tablero y coloca las reinas."""
        for i in range(self.n):
            for j in range(self.n):
                color = "white" if (i + j) % 2 == 0 else "gray"
                self.canvas.create_rectangle(
                    j * self.size, i * self.size,
                    (j + 1) * self.size, (i + 1) * self.size,
                    fill=color
                )
                if self.tablero[i][j] == 1:
                    self.dibujar_reina(i, j)

    def dibujar_reina(self, fila, col):
        """Dibuja una corona en la posición (fila, col)."""
        x1 = col * self.size
        y1 = fila * self.size
        x2 = (col + 1) * self.size
        y2 = (fila + 1) * self.size

        self.canvas.create_rectangle(
            x1 + self.size // 4, y2 - self.size // 4,
            x2 - self.size // 4, y2 - self.size // 6,
            fill="gold", outline="black"
        )

        self.canvas.create_polygon(
            x1 + self.size // 4, y2 - self.size // 4,
            x1 + self.size // 2, y1 + self.size // 4,
            x2 - self.size // 4, y2 - self.size // 4,
            fill="gold", outline="black"
        )

        self.canvas.create_oval(
            x1 + self.size // 3 - 5, y1 + self.size // 4 - 5,
            x1 + self.size // 3 + 5, y1 + self.size // 4 + 5,
            fill="red", outline="black"
        )
        self.canvas.create_oval(
            x1 + self.size // 2 - 5, y1 + self.size // 4 - 5,
            x1 + self.size // 2 + 5, y1 + self.size // 4 + 5,
            fill="blue", outline="black"
        )
        self.canvas.create_oval(
            x2 - self.size // 3 - 5, y1 + self.size // 4 - 5,
            x2 - self.size // 3 + 5, y1 + self.size // 4 + 5,
            fill="green", outline="black"
        )

    def iniciar(self):
        self.root.mainloop()


if __name__ == "__main__":
    n = input("Introduce el número de reinas: ")
    if n.isdigit() and int(n) > 0:
        n = int(n)
        gui = NReinasGUI(n)
        gui.iniciar()
    else:
        print("Por favor, introduce un número válido mayor o igual a 1.")
