class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None
 
def insertar(raiz,nodo):
        if raiz is None:
           raiz = nodo
        else:
            if raiz.dato < nodo.dato:
                if raiz.der is None:
                    raiz.der = nodo
                else: 
                    insertar(raiz.der, nodo)
            else:
                if raiz.izq is None:
                    raiz.izq = nodo 
                else:
                    insertar(raiz.izq, nodo)
def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izq)
        print(raiz.dato)
        inorden(raiz.der)
def preorden(raiz):
    if raiz is not None:
        print(raiz.dato)
        preorden(raiz.izq)
        preorden(raiz.der)
def postorden(raiz):
    if raiz is not None:
        postorden(raiz.izq)
        postorden(raiz.der)
        print(raiz.dato)

#ejemplo
raiz = Nodo(21)
insertar(raiz, Nodo(13))
insertar(raiz, Nodo(10))
insertar(raiz, Nodo(33))
insertar(raiz, Nodo(18))
insertar(raiz, Nodo(25))

print("inorden")
inorden(raiz)
print("preorden")
preorden(raiz)


    



