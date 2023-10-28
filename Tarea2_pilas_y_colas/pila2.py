class NodoPila:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    #constructor
    def __init__(self):
        self.tope = None

    # esta vacia?
    def esta_vacia(self):
        return self.tope is None
    
    # metodo push / insertar
    def apilar(self, elemento):
        nuevo_nodo = NodoPila(elemento)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo

    # metodo pop / eliminacion
    def desapilar(self):
        if not self.esta_vacia():
            valor_tope = self.tope.valor
            self.tope = self.tope.siguiente
            return valor_tope
        else:
            return "La pila está vacía"
        
    #metodo peek / acceso
    def ver_tope(self):
        if not self.esta_vacia():
            return self.tope.valor
        else:
            return "La pila está vacía"
        
    #metodo mostrar elementos 
    def ver_pila(self):
        elementos = []
        actual = self.tope
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos

# Ejemplo de uso:
#creamos una pila
pila = Pila()
#insertar elementos a la pila
pila.apilar("mango")
pila.apilar("uva")
pila.apilar("fresa")
#acceder a la pila
print("Tope de la pila:", pila.ver_tope())
#ver elementos de la pila
print("Elementos en la pila:", pila.ver_pila())
#eliminar elementos de la pila 
print("Desapilando elementos:")
print(pila.desapilar())  
print(pila.desapilar())  
print(pila.desapilar())  
print(pila.desapilar())  
