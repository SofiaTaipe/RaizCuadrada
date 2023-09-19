class RaizCuadrada():
    def __init__(self, numero, x, k):
        self.numero = numero
        self.x =x
        self.k = k

    def calcular(self):
        valoresK = 10
        self.x = 1.0
        for self.k in range(valoresK):
            self.x = (self.x + self.numero/self.x) / 2

    def imprimirRpta(self):
        print(f"La raiz despues de {self.k} interasiones es {self.x}")

