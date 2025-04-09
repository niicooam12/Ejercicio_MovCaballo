class Caballos:
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino

    def movimiento(self):
        return f"El caballo se ha movido desde {self.origen} hasta {self.destino}."