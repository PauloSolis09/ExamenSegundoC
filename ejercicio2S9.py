#paulo solis 
def parentesis_balanceados(cadena):
    pila = []

    for caracter in cadena:
        if caracter == '(' or caracter == '{' or caracter == '[':
            pila.append(caracter)
        elif caracter == ')' or caracter == '}' or caracter == ']':
            if not pila:
                return False
            ultimo = pila.pop()
            if caracter == ')' and ultimo != '(':
                return False
            if caracter == '}' and ultimo != '{':
                return False
            if caracter == ']' and ultimo != '[':
                return False

    return len(pila) == 0


# Código principal
frase = input("Ingrese una cadena con paréntesis: ")
if parentesis_balanceados(frase):
    print("Los paréntesis están balanceados.")
else:
    print("Los paréntesis NO están balanceados.")
