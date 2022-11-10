import matplotlib.pyplot as plt
import random
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

    MAX = 1000

    times_prefijo = []
    nodos_prefijo = []
    arbol_prefijo = Arbol()
    for i in range(1, MAX):
        arbol_prefijo.agregar( random.randint(0, MAX) )
        nodos_prefijo.append( i )
        times_prefijo.append( arbol_prefijo.times_recorrer_prefijo() )

    times_sufijo = []
    nodos_sufijo = []
    arbol_sufijo = Arbol()
    for i in range(1, MAX):
        arbol_sufijo.agregar( random.randint(0, MAX) )
        nodos_sufijo.append( i )
        times_sufijo.append( arbol_sufijo.times_recorrer_sufijo() )

    times_infijo = []
    nodos_infijo = []
    arbol_infijo = Arbol()
    for i in range(1, MAX):
        arbol_infijo.agregar( random.randint(0, MAX) )
        nodos_infijo.append( i )
        times_infijo.append( arbol_infijo.times_recorrer_infijo() )

    # Construyendo gráfica...
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(100, 60))
    ax1, ax2, ax3 = axes.flatten()
    fig.subplots_adjust(hspace=0.5)

    ax1.grid(True)
    ax2.grid(True)
    ax3.grid(True)

    ax1.set_title("Recorrido prefijo")
    ax2.set_title("Recorrido sufijo")
    ax3.set_title("Recorrido infijo")


    ax1.plot(nodos_prefijo, times_prefijo, label = '', marker = '*', color = 'b')
    ax2.plot(nodos_sufijo, times_sufijo, label = '', marker = '*', color = 'g')
    ax3.plot(nodos_infijo, times_infijo, label = '', marker = '*', color = 'r')

    # Labels de gráficas
    ax1.set_ylabel('Veces que entra')
    ax1.set_xlabel('Elementos')
    ax1.legend(loc=2)

    ax2.set_ylabel('Veces que entra')
    ax2.set_xlabel('Elementos')
    ax2.legend(loc=2)

    ax3.set_ylabel('Veces que entra')
    ax3.set_xlabel('Elementos')
    ax3.legend(loc=2)

    plt.show()


main()