numeros = [10, 20, 30, 20, 40, 10, 50, 30]

# Convertir la lista en un conjunto para eliminar los elementos duplicados
conjunto_numeros = set(numeros)

# Convertir el conjunto nuevamente en una lista
numeros_sin_duplicados = list(conjunto_numeros)

#Ordenar la lista en forma ascendente
numeros_sin_duplicados.sort()

# Imprimir la lista sin duplicados
print(numeros_sin_duplicados)
