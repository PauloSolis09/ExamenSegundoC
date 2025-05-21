class PilaDeTareas:
    def __init__(self):
        self.pila = []

    def push(self, tarea):
        self.pila.append(tarea)

    def pop(self):
        if self.esta_vacia():
            return "No hay tareas para revisar"
        return self.pila.pop()

    def peek(self):
        if self.esta_vacia():
            return "No hay tareas para revisar"
        return self.pila[-1]

    def esta_vacia(self):
        return len(self.pila) == 0

pila = PilaDeTareas()
continuar = True
while continuar:
    print("1. Agregar tarea")
    print("2. Revisar tarea")
    print("3. Ver siguiente tarea")
    print("4. Salir")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        tarea = input("Ingrese la descripcion de la tarea: ")
        pila.push(tarea)
        print("Tarea agregada")
    elif opcion == "2":
        print("Tarea revisada:", pila.pop())
    elif opcion == "3":
        print("Siguiente tarea a revisar:", pila.peek())
    elif opcion == "4":
        continuar = False
    else:
        print("Opcion no valida")