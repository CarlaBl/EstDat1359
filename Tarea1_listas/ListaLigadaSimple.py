# Caracteristicas 
class NodoSencillo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaLigadaSimple:
    def __init__(self):
        self.primero = None
# Metodos 
    def insert(self, valor):
        nuevo_nodo = NodoSencillo(valor)
        nuevo_nodo.siguiente = self.primero
        self.primero = nuevo_nodo

    def append(self, valor):
        nuevo_nodo = NodoSencillo(valor)
        if not self.primero:
            self.primero = nuevo_nodo
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def remove(self, valor):
        if not self.primero:
            return
        if self.primero.valor == valor:
            self.primero = self.primero.siguiente
            return
        actual = self.primero
        while actual.siguiente:
            if actual.siguiente.valor == valor:
                actual.siguiente = actual.siguiente.siguiente
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
    
    ## Definimos un display para mostrar los valores de la lista        
    def display(self):
        valores = []
        actual = self.primero
        while actual:
            valores.append(actual.valor)
            actual = actual.siguiente
        print(valores)
   
# mandamos a llamar a la clase ListaLigadaSimple
lista = ListaLigadaSimple()
# insertamos valores 
lista.insert('mango')
lista.insert('manzana')
lista.insert('uvas')
# imprimimos la lista
lista.display()
# usamos append para insertar un valor al final de la lista
lista.append('naranja')
lista.display()
# eliminamos el elemento 'uvas'
lista.remove('uvas')
lista.display()
# buscamos un elemento en la lista
print(lista.search(1))
print(lista.search(2))