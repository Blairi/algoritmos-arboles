import matplotlib.pyplot as plt
import random

from ArbolB import ArbolB

def prueba():

    BT = ArbolB(2)

    actual = BT.bTreeCreate()

    print("Se insertara B")
    BT.bTreeInsert(actual, ord("B"))

    print("Se insertara T")
    BT.bTreeInsert(actual, ord("T"))

    print("Se insertara H")
    BT.bTreeInsert(actual, ord("H"))

    print("Imprime raíz")
    BT.imprimeNodo(BT.raiz)

    print("Se insertara M")
    BT.bTreeInsert(actual, ord("M"))

    print(BT.raiz.llaves)
    print(BT.raiz.hijos[1].llaves)
    print(BT.raiz.hijos[2].llaves)

    print("Se insertara O")
    BT.bTreeInsert(actual, ord("O"))

    print("Se insertara C")
    BT.bTreeInsert(actual, ord("C"))

    print(BT.raiz.llaves)
    print(BT.raiz.hijos[1].llaves)
    print(BT.raiz.hijos[2].llaves)

    print("Se insertara Z")
    BT.bTreeInsert(actual, ord("Z"))

    print(BT.raiz.llaves)
    print(BT.raiz.hijos[1].llaves)
    print(BT.raiz.hijos[2].llaves)
    print(BT.raiz.hijos[3].llaves)

    print("\n===== Imprimiendo árbol =====")
    BT.imprimir_arbol()



def main():
    MAX = 1000

    # Caso promedio
    arbol_b = ArbolB(2)
    actual = arbol_b.bTreeCreate()
    elementos = list()
    times_lista = list()
    for i in range(MAX):
        times = arbol_b.times_bTreeInsert(actual, random.randint(0, 251))
        times_lista.append(times)
        elementos.append(i)
    
    # Construyendo gráfica...
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(100, 60))
    ax1, ax2, ax3 = axes.flatten()
    fig.subplots_adjust(hspace=0.5)

    ax1.grid(True)

    ax1.set_title("Insertando")

    ax1.plot(elementos, times_lista, label = '', marker = '*', color = 'b')

    # Labels de gráficas
    ax1.set_ylabel('Veces que entra')
    ax1.set_xlabel('Elementos')
    ax1.legend(loc=2)

    plt.show()

prueba()
main()

