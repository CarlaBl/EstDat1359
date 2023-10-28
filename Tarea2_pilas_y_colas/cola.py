class Cola:
    #constructor
    def __init__(self):
        self.elementos = []
   
    # metodo enqueue / insertar
    def enqueue (self, dato):
        self.elementos.append(dato)
    
    # esta vacia?
    def vacia (self):
        return len(self.elementos) == 0
   
    # metodo dequeue / eliminar
    def dequeue (self):
        if self.vacia():
            print('la cola esta vacia')
            return None
        else:
            return self.elementos.pop(0)
    #metodo peek / acceso
    def peek (self):
        if self.vacia():
            print('la cola esta vacia')
            return None
        else:
            return print(f'primero en la cola:{self.elementos[0]} ,ultimo en la cola:{self.elementos[-1]}')
    #metodo mostrar elementos
    def mostrar (self):
        print(f'los elementos de la cola son: {self.elementos}')
        
#prueba
#creamos una cola
cola1 = Cola()
cola1.mostrar()
#insertar elementos a la cola
cola1.enqueue("mango")
cola1.enqueue("uva")
cola1.enqueue("pera")
cola1.enqueue("fresa")
cola1.enqueue("manzana")
cola1.mostrar()
cola1.peek()
#eliminar elementos de la cola 
cola1.dequeue()
cola1.mostrar()
cola1.peek()
cola1.dequeue()
cola1.mostrar()

        