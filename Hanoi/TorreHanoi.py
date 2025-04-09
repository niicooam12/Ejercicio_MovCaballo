class TorreHanoi:
    def __init__(self, num_discos):
        """Inicializa las torres con el número de discos especificado."""
        self.num_discos = num_discos
        self.torres = [list(range(num_discos, 0, -1)), [], []]

    def mover_disco(self, origen, destino):
        """Mueve un disco de una torre a otra."""
        if self.torres[origen] and (not self.torres[destino] or self.torres[destino][-1] > self.torres[origen][-1]):
            disco = self.torres[origen].pop()
            self.torres[destino].append(disco)

    def resolver(self, n, origen, destino, auxiliar):
        """Resuelve el juego de las Torres de Hanoi recursivamente."""
        if n == 1:
            self.mover_disco(origen, destino)
        else:
            self.resolver(n - 1, origen, auxiliar, destino)
            self.mover_disco(origen, destino)
            self.resolver(n - 1, auxiliar, destino, origen)