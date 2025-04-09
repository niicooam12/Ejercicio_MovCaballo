class NReinas:
    def __init__(self, n):
        self.n = n
        self.tablero = [[0 for _ in range(n)] for _ in range(n)]

    def es_seguro(self, fila, col):
        """Verifica si es seguro colocar una reina en la posición (fila, col)."""
        for i in range(fila):
            if self.tablero[i][col] == 1:
                return False

        for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
            if self.tablero[i][j] == 1:
                return False

        for i, j in zip(range(fila, -1, -1), range(col, self.n)):
            if self.tablero[i][j] == 1:
                return False

        return True

    def resolver_n_reinas(self, fila=0):
        """Resuelve el problema de las N reinas utilizando backtracking."""
        if fila == self.n:
            return True

        for col in range(self.n):
            if self.es_seguro(fila, col):
                self.tablero[fila][col] = 1
                if self.resolver_n_reinas(fila + 1):
                    return True
                self.tablero[fila][col] = 0

        return False

    def obtener_tablero(self):
        """Devuelve el tablero resuelto."""
        if self.resolver_n_reinas():
            return self.tablero
        else:
            return None