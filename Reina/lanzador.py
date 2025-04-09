import tkinter as tk
from tkinter import messagebox
from NReinas import NReinas

class NReinasGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("N Reinas")
        
        self.label = tk.Label(master, text="Ingrese el número de reinas:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        self.start_button = tk.Button(master, text="Iniciar", command=self.iniciar_juego)
        self.start_button.pack(pady=10)

        self.canvas = None  # Se inicializa más tarde cuando se crea el tablero

    def iniciar_juego(self):
        try:
            n = self.entry.get()
            if not n.isdigit() or int(n) <= 0:
                messagebox.showerror("Entrada inválida", "El número de reinas debe ser un entero mayor a 0.")
                return
            n = int(n)
            
            # Crear el tablero y resolver el problema
            self.n = n
            self.size = 600 // n  # Tamaño de cada celda
            self.reinas = NReinas(n)
            solucion = self.reinas.resolver()
            if not solucion:
                messagebox.showinfo("Sin solución", "No hay solución para el número de reinas ingresado.")
                return
            self.tablero = self.reinas.obtener_tablero()

            # Crear el canvas para dibujar el tablero
            if self.canvas:
                self.canvas.destroy()  # Elimina el canvas anterior si existe
            self.canvas = tk.Canvas(self.master, width=600, height=600)
            self.canvas.pack(pady=10)

            self.dibujar_tablero()
        except ValueError as e:
            messagebox.showerror("Entrada inválida", str(e))

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

        # Dibujar el círculo negro de fondo
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", outline="white")

        # Dibujar la base de la corona (rectángulo)
        self.canvas.create_rectangle(
            x1 + self.size // 4, y2 - self.size // 4,
            x2 - self.size // 4, y2 - self.size // 6,
            fill="gold", outline="black"
        )

        # Dibujar la parte superior de la corona (triángulo)
        self.canvas.create_polygon(
            x1 + self.size // 4, y2 - self.size // 4,
            x1 + self.size // 2, y1 + self.size // 4,
            x2 - self.size // 4, y2 - self.size // 4,
            fill="gold", outline="black"
        )

        # Dibujar las joyas de la corona (pequeños círculos)
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

        self.canvas.create_oval(x1, y1, x2, y2, fill="black", outline="white")

if __name__ == "__main__":
    root = tk.Tk()
    app = NReinasGUI(root)
    root.mainloop()