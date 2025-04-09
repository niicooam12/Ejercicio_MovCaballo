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
        self.caballo_icon = None  # Referencia al único objeto gráfico del caballo
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
        """Inicia la animación del movimiento del caballo."""
        self.paso_actual = 0
        x, y = self.movimientos[0]  # Posición inicial del caballo
        self.caballo_icon = self.dibujar_caballo(x, y)  # Dibuja el caballo inicial
        self.mover_caballo()

    def mover_caballo(self):
        """Mueve el caballo y deja un rastro."""
        if self.paso_actual < len(self.movimientos) - 1:
            x1, y1 = self.movimientos[self.paso_actual]
            x2, y2 = self.movimientos[self.paso_actual + 1]

            # Cambiar la celda a gris para marcar que el caballo pasó por ella
            self.canvas.itemconfig(self.celdas[(x1, y1)], fill="gray")

            # Dibujar una línea desde la posición anterior a la nueva
            self.canvas.create_line(
                y1 * self.size + self.size // 2, x1 * self.size + self.size // 2,
                y2 * self.size + self.size // 2, x2 * self.size + self.size // 2,
                fill="blue", width=2
            )

            # Mover el caballo a la nueva posición
            self.canvas.coords(self.caballo_icon["cuerpo"],
                               y2 * self.size + self.size // 4, x2 * self.size + self.size // 3,
                               (y2 + 1) * self.size - self.size // 4, (x2 + 1) * self.size - self.size // 3)

            self.canvas.coords(self.caballo_icon["cabeza"],
                               y2 * self.size + self.size // 6, x2 * self.size + self.size // 6,
                               y2 * self.size + self.size // 3, x2 * self.size + self.size // 3)

            # Incrementar el paso y programar el siguiente movimiento
            self.paso_actual += 1
            self.root.after(500, self.mover_caballo)  # 500 ms entre movimientos

    def dibujar_caballo(self, fila, col):
        """Dibuja un caballo estilizado en la posición actual."""
        x1 = col * self.size
        y1 = fila * self.size
        x2 = (col + 1) * self.size
        y2 = (fila + 1) * self.size

        # Dibujar el cuerpo del caballo (rectángulo negro)
        cuerpo = self.canvas.create_rectangle(
            x1 + self.size // 4, y1 + self.size // 3,
            x2 - self.size // 4, y2 - self.size // 3,
            fill="black", outline="black"
        )

        # Dibujar la cabeza del caballo (círculo negro)
        cabeza = self.canvas.create_oval(
            x1 + self.size // 6, y1 + self.size // 6,
            x1 + self.size // 3, y1 + self.size // 3,
            fill="black", outline="black"
        )

        return {"cuerpo": cuerpo, "cabeza": cabeza}

    def iniciar(self):
        self.root.mainloop()


if __name__ == "__main__":
    gui = CaballoGUI(tam_tablero=8)
    gui.iniciar()