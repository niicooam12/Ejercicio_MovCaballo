class NReinas:
    def __init__(self, n):
        self.n = n
        self.tablero = [[0] * n for _ in range(n)]

    def es_seguro(self, fila, col):
        # Verificar la fila a la izquierda
        for i in range(col):
            if self.tablero[fila][i] == 1:
                return False

        # Verificar la diagonal superior izquierda
        for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
            if self.tablero[i][j] == 1:
                return False

        # Verificar la diagonal inferior izquierda
        for i, j in zip(range(fila, self.n), range(col, -1, -1)):
            if self.tablero[i][j] == 1:
                return False

        return True

    def resolver_reinas(self, col=0):
        if col >= self.n:
            return True

        for i in range(self.n):
            if self.es_seguro(i, col):
                self.tablero[i][col] = 1
                if self.resolver_reinas(col + 1):
                    return True
                self.tablero[i][col] = 0  # Backtracking

        return False

    def resolver(self):
        return self.resolver_reinas()

    def obtener_tablero(self):
        return self.tablero