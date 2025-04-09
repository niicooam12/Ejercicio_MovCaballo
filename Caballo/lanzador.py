import random
import random

class MovsCaballo:
    def __init__(self, tam_tablero=8):
        self.tam_tablero = tam_tablero
        self.origen = self.generar_posicion()
        self.tablero = [[-1 for _ in range(self.tam_tablero)] for _ in range(self.tam_tablero)]
        self.movimientos_x = [2, 1, -1, -2, -2, -1, 1, 2]
        self.movimientos_y = [1, 2, 2, 1, -1, -2, -2, -1]
        self.pasos = 0  # Variable para contar los pasos realizados

    def generar_posicion(self):
        return (random.randint(0, self.tam_tablero - 1), random.randint(0, self.tam_tablero - 1))

    def es_valido(self, x, y):
        return 0 <= x < self.tam_tablero and 0 <= y < self.tam_tablero and self.tablero[x][y] == -1

    def contar_movimientos_validos(self, x, y):
        """Cuenta cuántos movimientos válidos tiene una casilla."""
        count = 0
        for i in range(8):
            sig_x = x + self.movimientos_x[i]
            sig_y = y + self.movimientos_y[i]
            if self.es_valido(sig_x, sig_y):
                count += 1
        return count

    def resolver(self):
        # Comienza en la posición aleatoria
        x, y = self.origen
        self.tablero[x][y] = self.pasos
        self.pasos += 1

        # Intentamos recorrer todo el tablero
        if self.coordenadas(x, y):
            self.mostrar_camino()
        else:
            print("No se pudo encontrar un recorrido completo.")

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
            self.pasos += 1
            if self.coordenadas(sig_x, sig_y):
                return True
            # Retroceder si no es posible continuar
            self.tablero[sig_x][sig_y] = -1
            self.pasos -= 1

        return False

    def mostrar_camino(self):
        print(f"Recorrido completo desde {self.origen}:\n")
        for i in range(self.tam_tablero):
            for j in range(self.tam_tablero):
                print(f"{self.tablero[i][j]:2}", end=" ")
            print()


if __name__ == "__main__":
    caballo = MovsCaballo()
    caballo.resolver()