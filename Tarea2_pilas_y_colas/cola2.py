class NodoCola:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cola:
    #constructor
    def __init__(self):
        self.frente = None
        self.final = None

    # esta vacia?
    def esta_vacia(self):
        return self.frente is None
    
    # metodo enqueue / insertar
    def encolar(self, elemento):
        nuevo_nodo = NodoCola(elemento)
        if self.esta_vacia():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

     # metodo dequeue / eliminar
    def desencolar(self):
        if not self.esta_vacia():
            valor_frente = self.frente.valor
            self.frente = self.frente.siguiente
            if self.frente is None:
                self.final = None
            return valor_frente
        else:
            return "La cola está vacía"
        
    #metodo mostrar elementos    
    def ver_cola(self):
        elementos = []
        actual = self.frente
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos


# Ejemplo de uso:
#creamos una cola
cola = Cola()
#insertar elementos a la cola
cola.encolar("platano")
cola.encolar("manzana")
cola.encolar("mango")
#accedemos a la cola
print("Frente de la cola:", cola.frente.valor)  
#ver elementos de la cola
print("Elementos en la cola:", cola.ver_cola())
#eliminar elementos de la cola 
print("Desencolando elementos:")
print(cola.desencolar())
print(cola.desencolar())  
print(cola.desencolar())  
print(cola.desencolar())  
