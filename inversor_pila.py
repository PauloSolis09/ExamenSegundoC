#Yassly Diaz

def invertir_frase(frase):
    # Crear una pila vacía
    pila = []

    # Dividir la frase en palabras y apilarlas
    palabras = frase.strip().split()
    for palabra in palabras:
        pila.append(palabra)

    # Sacar las palabras de la pila en orden inverso
    frase_invertida = []
    while pila:
        frase_invertida.append(pila.pop())

    # Unir las palabras invertidas en una nueva frase
    return ' '.join(frase_invertida)


# Entrada del usuario
try:
    entrada = input("Ingrese una frase: ")
    resultado = invertir_frase(entrada)
    print("Frase invertida:", resultado)
except Exception as e:
    print("Ocurrió un error:", str(e))
