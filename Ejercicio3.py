class Cancion:
    def __init__(self, titulo):
        self.titulo = titulo
        self.anterior = None
        self.siguiente = None

class ListaReproduccion:
    def __init__(self):
        self.primera = None
        self.actual = None

    def agregar_cancion(self, titulo):
        nueva = Cancion(titulo)
        if not self.primera:
            self.primera = nueva
            self.actual = nueva
        else:
            temp = self.primera
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nueva
            nueva.anterior = temp
        print(f'Canción "{titulo}" agregada.\n')

    def eliminar_cancion(self, titulo):
        temp = self.primera
        while temp:
            if temp.titulo == titulo:
                if temp.anterior:
                    temp.anterior.siguiente = temp.siguiente
                else:
                    self.primera = temp.siguiente
                if temp.siguiente:
                    temp.siguiente.anterior = temp.anterior
                if self.actual == temp:
                    self.actual = temp.siguiente or temp.anterior
                print(f'Canción "{titulo}" eliminada.\n')
                return
            temp = temp.siguiente
        print(f'Canción "{titulo}" no encontrada.\n')

    def reproducir_actual(self):
        if self.actual:
            print(f'Reproduciendo: {self.actual.titulo}\n')
        else:
            print("La lista está vacía.\n")

    def siguiente_cancion(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            self.reproducir_actual()
        else:
            print("No hay siguiente canción.\n")

    def anterior_cancion(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            self.reproducir_actual()
        else:
            print("No hay canción anterior.\n")

    def mostrar_lista(self):
        temp = self.primera
        if not temp:
            print("Lista de reproducción vacía.\n")
            return
        print("Lista de reproducción:")
        while temp:
            actual_flag = " <-- Actual" if temp == self.actual else ""
            print(f'- {temp.titulo}{actual_flag}')
            temp = temp.siguiente
        print()

# Programa interactivo
def menu():
    lista = ListaReproduccion()
    while True:
        print("Menú:")
        print("1. Agregar canción")
        print("2. Eliminar canción")
        print("3. Reproducir canción actual")
        print("4. Reproducir siguiente canción")
        print("5. Reproducir canción anterior")
        print("6. Mostrar lista de reproducción")
        print("7. Salir")
        opcion = input("Elige una opción (1-7): ")

        if opcion == "1":
            titulo = input("Título de la canción: ")
            lista.agregar_cancion(titulo)
        elif opcion == "2":
            titulo = input("Título de la canción a eliminar: ")
            lista.eliminar_cancion(titulo)
        elif opcion == "3":
            lista.reproducir_actual()
        elif opcion == "4":
            lista.siguiente_cancion()
        elif opcion == "5":
            lista.anterior_cancion()
        elif opcion == "6":
            lista.mostrar_lista()
        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.\n")

menu()
