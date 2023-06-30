# Ejemplo de lista con elementos duplicados
lista_original = [1, 2, 3, 4, 2, 3, 5, 1, 6, 4]

# Crear una lista vacía para almacenar los elementos únicos
lista_sin_duplicados = []

# Iterar sobre la lista original
for elemento in lista_original:
    # Verificar si el elemento ya existe en la lista sin duplicados
    if elemento not in lista_sin_duplicados:
        # Agregar el elemento a la lista sin duplicados
        lista_sin_duplicados.append(elemento)

# Imprimir la lista sin duplicados
print(lista_sin_duplicados)
