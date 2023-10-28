class Pila:
    #constructor
    def __init__(self):
        self.elementos = []

    # metodo push / insertar
    def push (self, dato):
        self.elementos.append(dato)

    # esta vacia?
    def vacia (self):
        return len(self.elementos) == 0
    
    # metodo pop / eliminacion 
    def pop (self):
        if self.vacia():
            print('la pila esta vacia')
            return None
        else:
            return self.elementos.pop()
    
    #metodo peek / acceso
    def peek (self):
        if self.vacia():
            print('la pila esta vacia')
            return None
        else:
            return print(f'cabecera: {self.elementos [-1]}')
    
    #metodo mostrar elementos
    def mostrar (self):
        print(f'los elementos de la pila son: {self.elementos}')
    

#prueba
#creamos una pila
pila1 = Pila()
pila1.mostrar()
#insertar elementos a la pila
pila1.push("mango")
pila1.push("uva")
pila1.push("pera")
pila1.push("fresa")
pila1.push("manzana")
pila1.mostrar()
pila1.peek()
#eliminar elementos de la pila 
pila1.pop()
pila1.mostrar()
pila1.peek()
pila1.pop()
pila1.mostrar()






    

