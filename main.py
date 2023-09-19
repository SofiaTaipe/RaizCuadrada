from logica.RaizCuadrada import RaizCuadrada

if __name__ == '__main__':
    numeroA = float(input("Dame el valor del  numero: "))
    x = 1.0
    k = int
    raizCuadrada = RaizCuadrada(numeroA, x, k)
    raizCuadrada.calcular()
    raizCuadrada.imprimirRpta()


