numeros = [10, 20, 30, 20, 40, 10, 50, 30]

# Crear un diccionario para almacenar la frecuencia de cada elemento
frecuencia = {}

# Iterar sobre los números de la lista
for numero in numeros:
    # Verificar si el número ya está en el diccionario
    if numero in frecuencia:
        # Incrementar la frecuencia del número existente
        frecuencia[numero] += 1
    else:
        # Agregar el número al diccionario con una frecuencia inicial de 1
        frecuencia[numero] = 1

# Imprimir los resultados
for numero, contador in frecuencia.items():
    print("El número", numero, "aparece", contador, "veces.")
