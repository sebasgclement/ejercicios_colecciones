numeros = [10, 20, 30, 20, 40, 10, 50, 30]

# Crear una lista vacía para almacenar los elementos únicos
numeros_sin_duplicados = []

# Iterar sobre los números de la lista original
for numero in numeros:
    # Verificar si el número no está en la lista de números sin duplicados
    if numero not in numeros_sin_duplicados:
        # Agregar el número a la lista de números sin duplicados
        numeros_sin_duplicados.append(numero)

# Imprimir la lista sin duplicados
print(numeros_sin_duplicados)
