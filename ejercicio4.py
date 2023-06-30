# Ejemplo de lista
lista_original = [1, 2, 3, 4, 5]

# Crear una lista vacía para almacenar los elementos en orden inverso
lista_inversa = []

# Iterar sobre la lista original en orden inverso
for i in range(len(lista_original)-1, -1, -1):
    # Agregar el elemento actual a la lista inversa
    lista_inversa.append(lista_original[i])

# Imprimir la lista inversa
print(lista_inversa)
