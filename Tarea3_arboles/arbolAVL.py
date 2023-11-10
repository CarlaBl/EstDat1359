class nodoArbol:
    def __init__(self):
        self.dato = None
        self.izq = None
        self.der = None

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def arbol_vacio(self):
        return self.raiz == None
    def reiniciar (self):
        self.raiz= None
    
    def imprimir(self,opcion):
        cadena = ""
        if opcion == 0:
            cadena = self.preorden(self.raiz)
        elif opcion ==1:
            cadena = self.postorden(self.raiz)
        elif opcion ==2:
            cadena = self.inorden(self.raiz)
        return cadena
    
    def preorden(self, sub_arbol):
        cadena = ""
        if sub_arbol is not None:
            cadena += sub_arbol.dato + "\n" + self.preorden(sub_arbol.izq) + self.preorden(sub_arbol.der)
        return cadena
    def postorden(self, sub_arbol):
        cadena = ""
        if sub_arbol != None:
            cadena += self.postorden(sub_arbol.izq) + self.postorden(sub_arbol.der) + sub_arbol.dato + "\n"
        return cadena
    def inorden (self, sub_arbol):
        cadena = ""
        if sub_arbol != None:
            cadena += self.inorden(sub_arbol.izq) + sub_arbol.dato + "\n" + self.inorden(sub_arbol.der)
        return cadena
    
    def insertar (self, dato):
        self.raiz = self.__insertar_nodo__(self.raiz, dato)
    def __insertar_nodo__(self, sub_arbol, dato):
        if sub_arbol== None: 
            nodo = nodoArbol()
            nodo.dato = dato
            sub_arbol = nodo
        else:
            if dato< sub_arbol.dato:
                sub_arbol.izq = self.__insertar_nodo__(sub_arbol.izq, dato)
            elif dato> sub_arbol.dato:
                sub_arbol.der = self.__insertar_nodo__(sub_arbol.der,dato)
        return sub_arbol
    
    def __buscar_nodo__(self, dato):
        actual = None
        if not self.arbol_vacio():
            actual = self.raiz
            while actual != None and dato != actual.dato:
                if dato < actual.dato:
                    actual = actual.izq
                elif dato > actual.dato:
                    actual = actual.der
        return actual
    
    def buscar(self,dato):
        return self.__buscar_nodo__(dato) != None
    
    def quitar (self, dato):
        elemento = "No se encuentra el dato"
        posicion = self.__buscar_nodo__(dato)
        if posicion != None:
            elemento = posicion.dato
            self.raiz = self.__eliminar_nodo__(self.raiz, dato)
        return elemento
    
    def __eliminar_nodo__(self, sub_arbol,dato):
        if sub_arbol == None:
            return None
        elif dato< sub_arbol.dato:
            sub_arbol.izq =self.__eliminar_nodo__(sub_arbol.izq,dato)
        elif dato> sub_arbol.dato:
            sub_arbol.der = self.__eliminar_nodo__(sub_arbol.der,dato)
        else:
            nodo_eliminar = sub_arbol
            if nodo_eliminar.der == None:
                sub_arbol= nodo_eliminar.izq
            elif nodo_eliminar.izq == None:
                sub_arbol = nodo_eliminar.der
            else:
                nodo_eliminar= self.__cambiar__(nodo_eliminar)
                nodo_eliminar = None
        return sub_arbol
        
    def __cambiar__(self, aux):
        cambio = aux
        otro = aux.izq
        while otro.der != None:
            cambio = otro
            otro = otro.der
        aux.dato = otro.dato
        if cambio == aux:
            cambio.izq = otro.izq
        else:
            cambio.der = otro.izq
        return otro
    
        






