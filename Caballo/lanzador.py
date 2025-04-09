import random
import gradio as gr
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

    def generar_posicion(self):
        return (random.randint(0, self.tam_tablero - 1), random.randint(0, self.tam_tablero - 1))

    def es_valido(self, x, y):
        return 0 <= x < self.tam_tablero and 0 <= y < self.tam_tablero and self.tablero[x][y] == -1

    def registrar_movimiento(self, paso, x, y):
        """Registra un movimiento en la base de datos."""
        movimiento = Movimiento(paso=paso, x=x, y=y)
        self.session.add(movimiento)
        self.session.commit()

    def resolver(self):
        # Comienza en la posición aleatoria
        x, y = self.origen
        self.tablero[x][y] = self.pasos
        self.registrar_movimiento(self.pasos, x, y)  # Registrar el primer movimiento
        self.pasos += 1

        # Intentamos recorrer todo el tablero
        if self.coordenadas(x, y):
            return self.tablero
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

    def mostrar_tablero(self):
        """Devuelve el tablero como una lista de listas para Gradio."""
        return self.tablero


# Función para Gradio
def ejecutar_movimientos(tam_tablero):
    caballo = MovsCaballo(tam_tablero=tam_tablero)
    tablero = caballo.resolver()
    return tablero


# Crear la interfaz de Gradio
if __name__ == "__main__":
    interfaz = gr.Interface(
        fn=ejecutar_movimientos,
        inputs=gr.Number(label="Tamaño del tablero (por defecto: 8)", value=8),
        outputs=gr.Dataframe(label="Tablero de movimientos del caballo"),
        title="Recorrido del Caballo",
        description="Introduce el tamaño del tablero y observa cómo el caballo llena el tablero con su recorrido."
    )
    interfaz.launch()