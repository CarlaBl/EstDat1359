
"""Comenzando con un arreglo indexado en 1 de ceros y una lista de operaciones,
para cada operación, se agrega un valor a cada elemento del arreglo entre dos índices dados.
Una vez que se hayan realizado todas las operaciones, se devuelve el valor máximo en el arreglo."""

def valor_maximo_despues_de_operaciones(n, operaciones):
    # Inicializar un arreglo de ceros de longitud n
    arr = [0] * n                                                      #O(1)

    # Realizar las operaciones en el arreglo
    for operacion in operaciones:                                      #O(n)
        a, b, k = operacion                                            #O(1)
        arr[a - 1] += k  # Restamos 1 a 'a' para ajustar al índice 0   #O(1)
        if b < n:                                                      #O(1)
            arr[b] -= k  # Restamos 'k' al elemento siguiente a 'b'    #O(1)

    # Calcular el valor máximo en el arreglo
    valor_maximo = 0                                                   #O(1)
    valor_actual = 0                                                   #O(1)
    for num in arr:                                                    #O(n)
        valor_actual += num                                            #O(1)
        if valor_actual > valor_maximo:                                #O(1)
            valor_maximo = valor_actual                                #O(1)
    return valor_maximo

# Ejemplo de uso
n = 10
operaciones = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
resultado = valor_maximo_despues_de_operaciones(n, operaciones)
print(f'el valor maximo es: {resultado}')  # imprime 10

""" ANALISIS
    1+n(1+1+1(1))+1+1+n(1+1(1))
    1+n(1+1+1)+1+1+n(1+1)
    1+n(3)+1+1+n(2)
    1+3n+1+1+2n
    5n+3
    identificar termino dominante '5n'
    eliminar terminos menores      'n'
    por lo tanto es igual a       O(n)
"""
