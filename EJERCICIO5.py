class PilaDeSacos:
    def __init__(self):
        self.sacos = []

    def push(self, saco):
        self.sacos.append(saco)

    def pop(self):
        if len(self.sacos) == 0:
            return None
        return self.sacos.pop()

    def peek(self):
        if len(self.sacos) == 0:
            return None
        return self.sacos[-1]

def main():
    pila = PilaDeSacos()
    pila.push("Saco de arroz")
    pila.push("Saco de frijoles")
    pila.push("Saco de maíz")

    print("Saco encima:", pila.peek())

    descargado = pila.pop()
    print("Descargado:", descargado)

    print("Saco encima ahora:", pila.peek())

main()