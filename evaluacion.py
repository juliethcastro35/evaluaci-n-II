def invertir_array():
    # Solicitar la cantidad de elementos
    n = int(input("Ingrese la cantidad de elementos: "))

    # Crear el array solicitando los valores
    elementos = []
    for i in range(n):
        valor = input(f"Ingrese el elemento {i + 1}: ")
        elementos.append(valor)

    # Mostrar el array original
    print("Array original:", " ".join(elementos))

    # Invertir y mostrar el array
    elementos_invertidos = elementos[::-1]
    print("Array invertido:", " ".join(elementos_invertidos))

# Ejecutar la función
invertir_array()