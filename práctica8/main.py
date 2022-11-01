from Arbol import Arbol


def main():
    arbol = Arbol()
    arbol.agregar(8)
    arbol.agregar(3)
    arbol.agregar(10)
    arbol.agregar(14)
    arbol.agregar(13)
    arbol.agregar(1)
    arbol.agregar(6)
    arbol.agregar(4)
    arbol.agregar(7)

    print("Recorrido prefijo")
    arbol.imprimirPrefijo()

    print("Recorrido sufijo")
    arbol.imprimirSufijo()

    print("Recorrido infijo")
    arbol.imprimirInfijo()


main()