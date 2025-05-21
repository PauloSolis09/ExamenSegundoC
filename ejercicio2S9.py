#paulo solis 
def parentesis_balanceados(cadena):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}

    for caracter in cadena:
        if caracter in '({[':
            pila.append(caracter)
        elif caracter in ')}]':
            if not pila or pila[-1] != pares[caracter]:
                return False
            pila.pop()
    
    return not pila

# Ejemplos de uso con texto entre paréntesis
texto1 = "{[()()]}"                      # Balanceado
texto2 = "{[(Hola)(mundo)]}"            # Balanceado
texto3 = "{[Texto](sin)[orden}}"        # No balanceado (corchetes no cierran)
texto4 = "Función ejemplo() { return [1, 2, 3]; }"  # Balanceado

print(f"'{texto1}' está balanceado: {parentesis_balanceados(texto1)}")
print(f"'{texto2}' está balanceado: {parentesis_balanceados(texto2)}")
print(f"'{texto3}' está balanceado: {parentesis_balanceados(texto3)}")
print(f"'{texto4}' está balanceado: {parentesis_balanceados(texto4)}")
