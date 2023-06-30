# Ejemplo de lista con elementos duplicados
lista_original = [1, 2, 3, 4, 2, 3, 5, 1, 6, 4]

# Convertir la lista en un conjunto para eliminar los elementos duplicados
conjunto = set(lista_original)

# Convertir el conjunto nuevamente en una lista
lista_sin_duplicados = list(conjunto)

# Imprimir la lista sin duplicados
print(lista_sin_duplicados)
