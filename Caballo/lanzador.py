import random
import tkinter as tk
from models import Movimiento, Session

class MovsCaballo:
    def __init__(self, tam_tablero=8):
        self.tam_tablero = tam_tablero
        self.origen = self.generar_posicion()
        self.tablero = [[-1 for _ in range(self.tam_tablero)] for _ in range(self.tam_tablero)]
        self.movimientos_x = [2, 1, -1, -2, -2, -1, 1, 2]
        self.movimientos_y = [1, 2, 2, 1, -1, -2, -2, -1]
        self.pasos = 0  # Variable para contar los pasos realizados
        self.session = Session()  # Crear una sesión de base de datos
        self.movimientos = []  # Lista para almacenar los movimientos realizados

    def generar_posicion(self):
        return (random.randint(0, self.tam_tablero - 1), random.randint(0, self.tam_tablero - 1))

    def es_valido(self, x, y):
        return 0 <= x < self.tam_tablero and 0 <= y < self.tam_tablero and self.tablero[x][y] == -1

    def registrar_movimiento(self, paso, x, y):
        """Registra un movimiento en la base de datos."""
        movimiento = Movimiento(paso=paso, x=x, y=y)
        self.session.add(movimiento)
        self.session.commit()
        self.movimientos.append((x, y))  # Agregar el movimiento a la lista

    def resolver(self):
        # Comienza en la posición aleatoria
        x, y = self.origen
        self.tablero[x][y] = self.pasos
        self.registrar_movimiento(self.pasos, x, y)  # Registrar el primer movimiento
        self.pasos += 1

        # Intentamos recorrer todo el tablero
        if self.coordenadas(x, y):
            return self.movimientos
        else:
            return "No se pudo encontrar un recorrido completo."

    def coordenadas(self, x, y):
        if self.pasos == self.tam_tablero * self.tam_tablero:
            return True  # Si ya hemos recorrido todas las casillas, terminamos

        # Ordenar los movimientos según el heurístico de Warnsdorff
        movimientos = []
        for i in range(8):
            sig_x = x + self.movimientos_x[i]
            sig_y = y + self.movimientos_y[i]
            if self.es_valido(sig_x, sig_y):
                movimientos.append((self.contar_movimientos_validos(sig_x, sig_y), sig_x, sig_y))

        # Ordenar por el número de movimientos válidos (menor a mayor)
        movimientos.sort()

        for _, sig_x, sig_y in movimientos:
            self.tablero[sig_x][sig_y] = self.pasos
            self.registrar_movimiento(self.pasos, sig_x, sig_y)  # Registrar el movimiento
            self.pasos += 1
            if self.coordenadas(sig_x, sig_y):
                return True
            # Retroceder si no es posible continuar
            self.tablero[sig_x][sig_y] = -1
            self.pasos -= 1

        return False

    def contar_movimientos_validos(self, x, y):
        """Cuenta cuántos movimientos válidos tiene una casilla."""
        count = 0
        for i in range(8):
            sig_x = x + self.movimientos_x[i]
            sig_y = y + self.movimientos_y[i]
            if self.es_valido(sig_x, sig_y):
                count += 1
        return count


# Interfaz gráfica con Tkinter
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
        self.lineas = []  # Lista para almacenar las líneas del rastro
        for paso in range(len(self.movimientos) - 1):
            x1, y1 = self.movimientos[paso]
            x2, y2 = self.movimientos[paso + 1]
            self.root.after(paso * 500, self.mover_caballo, x1, y1, x2, y2)  # 500 ms entre movimientos

    def mover_caballo(self, x1, y1, x2, y2):
        """Mueve el caballo y deja un rastro."""
        # Cambiar la celda a gris para marcar que el caballo pasó por ella
        self.canvas.itemconfig(self.celdas[(x1, y1)], fill="gray")

        # Dibujar una línea desde la posición anterior a la nueva
        self.lineas.append(self.canvas.create_line(
            y1 * self.size + self.size // 2, x1 * self.size + self.size // 2,
            y2 * self.size + self.size // 2, x2 * self.size + self.size // 2,
            fill="blue", width=2
        ))

        # Dibujar el punto negro en la nueva posición
        self.canvas.delete("caballo")  # Elimina el punto anterior
        self.canvas.create_oval(
            y2 * self.size + self.size // 4, x2 * self.size + self.size // 4,
            (y2 + 1) * self.size - self.size // 4, (x2 + 1) * self.size - self.size // 4,
            fill="black", tags="caballo"
        )

    def iniciar(self):
        self.root.mainloop()


if __name__ == "__main__":
    gui = CaballoGUI(tam_tablero=8)
    gui.iniciar()