from arbolAVL import ArbolAVL

arbol = ArbolAVL()
#insertar elementos
arbol.insertar("21")
arbol.insertar("13")
arbol.insertar("10")
arbol.insertar("33")
arbol.insertar("18")
arbol.insertar("25")
#imprimir recorridos
print('preorden')
print(arbol.imprimir(0))
print('postorden')
print(arbol.imprimir(1))
print('inorden')
print(arbol.imprimir(2))
#buscar datos
print("Esta el dato 10: ", arbol.buscar("10"))
print("Esta el dato 52: ", arbol.buscar("52"))
#borrar datos
print("Borrando el dato: ", arbol.quitar("10"))
print('preorden')
print(arbol.imprimir(0))
print('inorden')
print(arbol.imprimir(2))
