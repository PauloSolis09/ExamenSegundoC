#Elaborado por Erick Bernardo Guido Tellez

def infix_to_postfix(expression):
    precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    stack = []
    output = []
    
    for char in expression:
        if char.isalnum():  # Si es un operando (número o letra)
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Eliminar '(' de la pila
        else:  # Es un operador
            while (stack and stack[-1] != '(' and
                   precedence[char] <= precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(char)
    
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)

def evaluate_postfix(expression):
    stack = []
    
    for char in expression:
        if char.isdigit():  # Si es un operando
            stack.append(int(char))
        else:  # Es un operador
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 / operand2)
            elif char == '^':
                stack.append(operand1 ** operand2)
    
    return stack.pop()


def main():
    # Lista de expresiones infijas
    infix_expressions = [
        "6 + 4 * ( 9 + 5 * 2 - 3 )",
        "5 * 4 + ( 9 / 3 + 8 * 2 )",
        "7 + 3 * ( 9 + 5 * 2 ^ 3 - 8 )",
        "4 * ( 2 + 3 - 2 ) * ( 4 + 8 - 5 )",
        "8 + 4 + (( 5 ^ 2 + 6 ) * 4 )",
        "6 * 2 + 8 - 3 * 2 / 2"
    ]
    
    for infix_expression in infix_expressions:
        # Convertir a postfijo
        postfix_expression = infix_to_postfix(infix_expression.replace(" ", ""))
        print(f"Expresión en postfijo: {postfix_expression}")
        
        # Evaluar la expresión en postfijo
        result = evaluate_postfix(postfix_expression)
        print(f"Resultado de la evaluación: {result}\n")

if __name__ == "__main__":
    main()
