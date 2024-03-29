from Nodo import Nodo

class ArbolB:

    def __init__(self, gradoMinimo) -> None:
        self.t = gradoMinimo
        self.raiz = None
    
    
    def bTreeCreate(self):
        if self.raiz == None:
            self.raiz = Nodo( self.t )
        return self.raiz
    

    def bTreeSplitShild(self, x, i):
        z = Nodo(self.t)
        y = x.hijos[i]
        z.hoja = y.hoja
        z.n = self.t - 1

        for j in range(1, self.t):
            z.llaves[j] = y.llaves[j + self.t]
            y.llaves[j + self.t] = None
        
        if y.hoja == 0:
            for j in range(1, self.t + 1):
                z.hijos[j] = y.hijos[j + self.t]
                y.hijos[j + self.t] = None
        
        y.n = self.t - 1

        for j in range(x.n + 1, i, -1):
            x.hijos[j + 1] = x.hijos[j]
        
        x.hijos[i + 1] = z
        
        for j in range(x.n, i - 1, -1):
            x.llaves[j + 1] = x.llaves[j]
        
        x.llaves[i] = y.llaves[self.t]
        y.llaves[self.t] = None
        x.n = x.n + 1
    

    def times_bTreeSplitShild(self, x, i):
        times = 0

        z = Nodo(self.t)
        y = x.hijos[i]
        z.hoja = y.hoja
        z.n = self.t - 1

        for j in range(1, self.t):
            times += 1

            z.llaves[j] = y.llaves[j + self.t]
            y.llaves[j + self.t] = None
        
        if y.hoja == 0:
            for j in range(1, self.t + 1):
                times += 1

                z.hijos[j] = y.hijos[j + self.t]
                y.hijos[j + self.t] = None
        
        y.n = self.t - 1

        for j in range(x.n + 1, i, -1):
            times += 1

            x.hijos[j + 1] = x.hijos[j]
        
        x.hijos[i + 1] = z
        
        for j in range(x.n, i - 1, -1):
            times += 1

            x.llaves[j + 1] = x.llaves[j]
        
        x.llaves[i] = y.llaves[self.t]
        y.llaves[self.t] = None
        x.n = x.n + 1

        return times

    def bTreeInsertNonFull(self, x, k):

        i = x.n

        if x.hoja == 1:

            while i >= 1 and k < x.llaves[i]:
                x.llaves[i + 1] = x.llaves[i]
                i = i - 1

            x.llaves[i + 1] = k
            x.n = x.n + 1

        else:

            while i >= 1 and k < x.llaves[i]:
                i = i - 1

            i = i + 1

            if x.hijos[i].n == 2 * self.t - 1:
                self.bTreeSplitShild(x, i)
                if k > x.llaves[i]:
                    i = i + 1

            self.bTreeInsertNonFull(x.hijos[i], k)
    

    def times_bTreeInsertNonFull(self, x, k):
        times = 0

        i = x.n

        if x.hoja == 1:

            while i >= 1 and k < x.llaves[i]:
                times += 1

                x.llaves[i + 1] = x.llaves[i]
                i = i - 1

            x.llaves[i + 1] = k
            x.n = x.n + 1

        else:

            while i >= 1 and k < x.llaves[i]:
                times += 1

                i = i - 1

            i = i + 1

            if x.hijos[i].n == 2 * self.t - 1:
                self.bTreeSplitShild(x, i)
                if k > x.llaves[i]:
                    i = i + 1

            times += self.times_bTreeInsertNonFull(x.hijos[i], k)
        
        return times
    

    def bTreeInsert(self, nodo, k):

        r = self.raiz

        if r.n == 2 * self.t - 1:
            s = Nodo(self.t)
            self.raiz = s
            s.hoja = 0
            s.n = 0
            s.hijos[1] = r
            self.bTreeSplitShild(s, 1)
            self.bTreeInsertNonFull(s, k)
        else:
            self.bTreeInsertNonFull(r, k)
    

    def times_bTreeInsert(self, nodo, k):
        times = 0

        r = self.raiz

        if r.n == 2 * self.t - 1:
            s = Nodo(self.t)
            self.raiz = s
            s.hoja = 0
            s.n = 0
            s.hijos[1] = r
            times += self.times_bTreeSplitShild(s, 1)
            times += self.times_bTreeInsertNonFull(s, k)
        else:
            times += self.times_bTreeInsertNonFull(r, k)
        
        return times

    
    def imprimir_arbol(self):

        for llave in self.raiz.llaves:
            if not isinstance(llave, list):
                print(chr(llave) + " ", end="")
        print()

        for hijo in self.raiz.hijos:
            if not isinstance(hijo, list):
                self.imprimir_hijos(hijo)
        
        print()


    def imprimir_hijos(self, nodo):
        for llave in nodo.llaves:
            if not isinstance(llave, list) and llave != None:
                print(chr(llave) + " ", end="")

    def imprimeNodo(self, nodo):
        for i in range(1, 2 + self.t, 1):
            if nodo.llaves[i] != None:
                print( nodo.llaves[i] )