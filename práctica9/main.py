from ArbolB import ArbolB

def main():

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
    print(BT.raiz.llaves[1].llaves)
    print(BT.raiz.llaves[2].llaves)

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

main()
