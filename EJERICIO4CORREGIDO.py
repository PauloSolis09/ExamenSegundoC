import heapq

class Elemento:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

    def __lt__(self, otro):
        return self.prioridad < otro.prioridad

class ColaDePrioridad:
    def __init__(self):
        self.cola = []

    def encolar(self, nombre, prioridad):
        heapq.heappush(self.cola, Elemento(nombre, prioridad))

    def desencolar(self):
        if self.cola:
            return heapq.heappop(self.cola).nombre
        return None

    def esta_vacia(self):
        return len(self.cola) == 0

cola = ColaDePrioridad()
cola.encolar("Tarea urgente", 1)
cola.encolar("Tarea normal", 3)
cola.encolar("Tarea importante", 2)

while not cola.esta_vacia():
    print("Atendiendo:", cola.desencolar())
