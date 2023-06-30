from random import randint

# Generar una lista de números al azar
lista_numeros = [randint(1, 100) for _ in range(10)]  # Genera 10 números aleatorios entre 1 y 100

# Crear una lista vacía para almacenar los números impares
numeros_impares = []

# Iterar sobre cada número en la lista original
for numero in lista_numeros:
    # Verificar si el número es impar
    if numero % 2 != 0:
        # Agregar el número impar a la lista de números impares
        numeros_impares.append(numero)

# Imprimir la lista de números impares
print(numeros_impares)
