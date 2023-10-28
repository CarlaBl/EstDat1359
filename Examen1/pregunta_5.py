"""Para optimizar el algoritmo,
en lugar de realizar operaciones en todo el rango entre los índices dados, 
podemos realizar las operaciones en los índices de inicio y final de cada operación
"""
def valor_maximo_despues_de_operaciones(n, operaciones):
    # Inicializar un arreglo de ceros de longitud n+1 para manejar los índices indexados en 1
    arr = [0] * (n + 1)                                               # O(1)

    # Realizar las operaciones en el arreglo
    for operacion in operaciones:                                     # O(n)
        a, b, k = operacion                                           # O(1)
        arr[a] += k         #agregamos k al índice a del arreglo      # O(1)
        if b + 1 <= n:      #si b + 1 está dentro del rango           # O(1)
            arr[b + 1] -= k #restamos k al índice b + 1 del arreglo   # O(1)

    #calculamos el valor máximo
    valor_maximo = 0                                                  # O(1)   
    valor_actual = 0                                                  # O(1)
    for i in range(1, n + 1):                                         # O(n)
        valor_actual += arr[i]                                        # O(1)
        if valor_actual > valor_maximo:                               # O(1)
            valor_maximo = valor_actual                               # O(1)
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
