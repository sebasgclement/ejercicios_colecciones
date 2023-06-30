# Ejemplo de lista de números
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Crear una lista vacía para almacenar los números pares
numeros_pares = []

# Iterar sobre cada número en la lista original
for numero in lista_numeros:
    # Verificar si el número es par
    if numero % 2 == 0:
        # Agregar el número par a la lista de números pares
        numeros_pares.append(numero)

# Imprimir la lista de números pares
print(numeros_pares)
