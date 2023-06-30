numeros = [10, 5, 25, 30, 15]

# Inicializar la variable para almacenar el número más grande
numero_mas_grande = numeros[0]

# Iterar sobre los números de la lista
for numero in numeros:
    # Verificar si el número actual es más grande que el número almacenado
    if numero > numero_mas_grande:
        numero_mas_grande = numero

# Imprimir el número más grande
print("El número más grande es:", numero_mas_grande)
