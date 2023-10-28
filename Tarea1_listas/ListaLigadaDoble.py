# caracteristicas 
class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaLigadaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
# metodos 
    def insert(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if not self.primero:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo

    def append(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if not self.primero:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def remove(self, valor):
        if not self.primero:
            return
        if self.primero.valor == valor:
            self.primero = self.primero.siguiente
            if self.primero:
                self.primero.anterior = None
            else:
                self.ultimo = None
            return
        actual = self.primero
        while actual.siguiente:
            if actual.siguiente.valor == valor:
                actual.siguiente = actual.siguiente.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual
                else:
                    self.ultimo = actual
                return
            actual = actual.siguiente

    def search(self, index):
        if index < 0:
            return None
        actual = self.primero
        i = 0
        while actual and i < index:
            actual = actual.siguiente
            i += 1
        if actual:
            return actual.valor
        return None

    def display(self):
        valores = []
        actual = self.primero
        while actual:
            valores.append(actual.valor)
            actual = actual.siguiente
        print(valores)

# creamos una lista ligada doble instanciando la clase ListaLigadaDoble
lista = ListaLigadaDoble()
# insertamos valores 
lista.insert('mango')
lista.insert('manzana')
lista.insert('uvas')
# imprimimos la lista
lista.display()
# usamos append para insertar un valor al final de la lista
lista.append('naranja')
lista.append('platano')
lista.display()
# eliminamos el elemento 'mango'
lista.remove('mango')
lista.display()
# buscamos un elemento en la lista
print(lista.search(1))
print(lista.search(2))

