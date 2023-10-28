
# caracteristicas 
class NodoCircular:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaLigadaCircular:
    def __init__(self):
        self.primero = None
# metodos
    def insert(self, valor):
        nuevo_nodo = NodoCircular(valor)
        if not self.primero:
            self.primero = nuevo_nodo
            nuevo_nodo.siguiente = self.primero
        else:
            nuevo_nodo.siguiente = self.primero
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            self.primero = nuevo_nodo

    def append(self, valor):
        nuevo_nodo = NodoCircular(valor)
        if not self.primero:
            self.primero = nuevo_nodo
            nuevo_nodo.siguiente = self.primero
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.primero

    def remove(self, valor):
        if not self.primero:
            return
        if self.primero.valor == valor:
            if self.primero.siguiente == self.primero:
                self.primero = None
                return
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = self.primero.siguiente
            self.primero = self.primero.siguiente
            return
        actual = self.primero
        previo = None
        while actual.siguiente != self.primero:
            previo = actual
            actual = actual.siguiente
            if actual.valor == valor:
                previo.siguiente = actual.siguiente
                return

    def search(self, index):
        if index < 0:
            return None
        actual = self.primero
        i = 0
        while actual and i < index:
            actual = actual.siguiente
            if actual == self.primero:
                return None
            i += 1
        return actual.valor
    
    # Definimos un display para mostrar los valores de la lista ligada circular
    def display(self):
        valores = []
        actual = self.primero
        while actual:
            valores.append(actual.valor)
            actual = actual.siguiente
            if actual == self.primero:
                break
        print(valores)

# creamos una lista ligada circular instanciando la clase ListaLigadaCircular
lista_circular = ListaLigadaCircular()
# insertamos valores en la lista ligada circular
lista_circular.insert('mango')
lista_circular.insert('manzana')
lista_circular.insert('uvas')
# imprimimos la lista
lista_circular.display()
# usamos append para insertar un valor al final de la lista
lista_circular.append('naranja')
lista_circular.append('platano')
lista_circular.display()
# eliminamos el elemento 'mango'
lista_circular.remove('mango')
lista_circular.display()
# buscamos un elemento en la lista
print(lista_circular.search(0))
print(lista_circular.search(1))
print(lista_circular.search(3))