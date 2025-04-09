import tkinter as tk
import subprocess
import os
import sys

class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Seleccionar Juego")
        self.master.geometry("400x300")  # Tamaño de la ventana

        self.label = tk.Label(master, text="Seleccione un juego:", font=("Arial", 14))
        self.label.pack(pady=20)

        self.caballo_button = tk.Button(master, text="Movimiento del Caballo", font=("Arial", 12), command=self.abrir_caballo)
        self.caballo_button.pack(pady=10)

        self.reina_button = tk.Button(master, text="N Reinas", font=("Arial", 12), command=self.abrir_reina)
        self.reina_button.pack(pady=10)

        self.hanoi_button = tk.Button(master, text="Torres de Hanoi", font=("Arial", 12), command=self.abrir_hanoi)
        self.hanoi_button.pack(pady=10)

        self.salir_button = tk.Button(master, text="Salir", font=("Arial", 12), command=self.salir)
        self.salir_button.pack(pady=20)

    def abrir_caballo(self):
        ruta = os.path.join(os.path.dirname(__file__), "Caballo", "lanzador.py")
        subprocess.Popen([sys.executable, ruta])

    def abrir_reina(self):
        ruta = os.path.join(os.path.dirname(__file__), "Reina", "lanzador.py")
        subprocess.Popen([sys.executable, ruta])

    def abrir_hanoi(self):
        ruta = os.path.join(os.path.dirname(__file__), "Hanoi", "lanzador.py")
        subprocess.Popen([sys.executable, ruta])

    def salir(self):
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()