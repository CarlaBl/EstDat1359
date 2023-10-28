"""Comenzando con un arreglo indexado en 1 de ceros y una lista de operaciones,
para cada operación, se agrega un valor a cada elemento del arreglo entre dos índices dados.
Una vez que se hayan realizado todas las operaciones, se devuelve el valor máximo en el arreglo."""

class calculadoraValorMaximo:
    #constructor
    # Inicializar un arreglo de ceros de longitud n
    def __init__(self, n):
        self.n = n
        self.arr = [0] * (n + 1)
   # Metodo que realiza las operaciones en el arreglo
    def agregar_operacion(self, a, b, k):
        self.arr[a] += k
        if b + 1 <= self.n:
            self.arr[b + 1] -= k
   # Metodo que encuentra el valor maximo
    def encontrar_valor_maximo(self):
        valor_maximo = 0
        valor_actual = 0
        for i in range(1, self.n + 1):
            valor_actual += self.arr[i]
            if valor_actual > valor_maximo:
                valor_maximo = valor_actual

        return valor_maximo

# Ejemplo de uso
n = 10
operaciones = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]

calculator = calculadoraValorMaximo(n)

for operacion in operaciones:
    a, b, k = operacion
    calculator.agregar_operacion(a, b, k)

resultado = calculator.encontrar_valor_maximo()
print(resultado)  # Imprimir 10 
