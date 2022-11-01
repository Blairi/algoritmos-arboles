from Nodo import Nodo


class Arbol:

    def __init__(self) -> None:
        self.raiz = None


    def obtenerRaiz(self):
        return self.raiz


    def agregar(self, val):
        if self.raiz == None:
            self.raiz = Nodo(val)
        else:
            self.agregarNodo( val, self.raiz )

    
    def agregarNodo(self, val, nodo):
        if val < nodo.valor:
            if nodo.hijoIzq != None:
                self.agregarNodo( val, nodo.hijoIzq )
            else:
                nodo.hijoIzq = Nodo( val )
        else:
            if nodo.hijoDer != None:
                self.agregarNodo( val, nodo.hijoDer )
            else:
                nodo.hijoDer = Nodo( val )


    def busqueda(self, nodo, valor):

        if nodo == None or valor == nodo.valor:
            return nodo

        if valor < nodo.valor:
            return self.busqueda(nodo.hijoIzq, valor)
        else:
            return self.busqueda(nodo.hijoDer, valor)
    
    def buscarValor(self, valor):
        if self.raiz != None:
            return self.busqueda( self.raiz, valor )


    def prefijo(self, nodo):
        if nodo != None:
            print( str(nodo.valor) )
            if nodo.hijoIzq != None:
                self.prefijo(nodo.hijoIzq)

            if nodo.hijoDer != None:
                self.prefijo(nodo.hijoDer)


    def imprimirPrefijo(self):
        if self.raiz != None:
            self.prefijo( self.raiz )


    def sufijo(self, nodo):
        if nodo != None:
            if nodo.hijoIzq != None:
                self.sufijo(nodo.hijoIzq)

            if nodo.hijoDer != None:
                self.sufijo(nodo.hijoDer)

            print( str(nodo.valor) )

    def imprimirSufijo(self):
        if self.raiz != None:
            self.sufijo( self.raiz )


    def infijo(self, nodo):
        if nodo != None:
            if nodo.hijoIzq != None:
                self.infijo(nodo.hijoIzq)

            print( str(nodo.valor) )

            if nodo.hijoDer != None:
                self.infijo(nodo.hijoDer)


    def imprimirInfijo(self):
        if self.raiz != None:
            self.infijo( self.raiz )

