#Elaborado por Erick Bernardo Guido Tellez

def infija_a_postfija(expresion):
    precedencia = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    pila = []
    salida = []
    
    for caracter in expresion:
        if caracter.isalnum():  # Si es un operando (número o letra)
            salida.append(caracter)
        elif caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop()  # Eliminar '(' de la pila
        else:  # Es un operador
            while (pila and pila[-1] != '(' and
                   precedencia[caracter] <= precedencia[pila[-1]]):
                salida.append(pila.pop())
            pila.append(caracter)
    
    while pila:
        salida.append(pila.pop())
    
    return ''.join(salida)

def evaluar_postfija(expresion):
    pila = []
    
    for simbolo in expresion:
        if simbolo.isdigit():  # Si es un operando
            pila.append(int(simbolo))
        else:  # Es un operador
            operando2 = pila.pop()  # Sacar el segundo operando
            operando1 = pila.pop()  # Sacar el primer operando
            
            # Realizar la operación según el operador leído
            if simbolo == '+':
                valor = operando1 + operando2
            elif simbolo == '-':
                valor = operando1 - operando2
            elif simbolo == '*':
                valor = operando1 * operando2
            elif simbolo == '/':
                valor = operando1 / operando2
            elif simbolo == '^':
                valor = operando1 ** operando2
            
            pila.append(valor)  # Empujar el resultado a la pila
    
    return pila.pop()  # El resultado final es el único elemento en la pila

def main():
    # Lista de expresiones infijas
    expresiones_infijas = [
        "6 + 4 * ( 9 + 5 * 2 - 3 )",
        "5 * 4 + ( 9 / 3 + 8 * 2 )",
        "7 + 3 * ( 9 + 5 * 2 ^ 3 - 8 )",
        "4 * ( 2 + 3 - 2 ) * ( 4 + 8 - 5 )",
        "8 + 4 + (( 5 ^ 2 + 6 ) * 4 )",
        "6 * 2 + 8 - 3 * 2 / 2"
    ]
    
    for expresion_infija in expresiones_infijas:
        # Convertir a postfijo
        expresion_postfija = infija_a_postfija(expresion_infija.replace(" ", ""))
        print(f"Expresión en postfijo: {expresion_postfija}")
        
        # Evaluar la expresión en postfijo
        resultado = evaluar_postfija(expresion_postfija)
        print(f"Resultado de la evaluación: {resultado}\n")

if __name__ == "__main__":
    main()
