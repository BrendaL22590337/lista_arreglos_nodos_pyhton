class Nodo:
    def __init__(self, nombre, calificacion):
        # Arreglo con dos datos: nombre y calificación
        self.datos = [nombre, calificacion]
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, nombre, calificacion):
        nuevo = Nodo(nombre, calificacion)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def mostrar_lista(self):
        if self.cabeza is None:
            print("\nLa lista está vacía.")
        else:
            print("\nContenido de la lista:\n")
            actual = self.cabeza
            while actual:
                print(f"Nombre: {actual.datos[0]} | Calificación: {actual.datos[1]}")
                actual = actual.siguiente


# Programa principal
if __name__ == "__main__":
    lista = ListaEnlazada()

    print("=== LISTA DE ESTUDIANTES ===")
    while True:
        nombre = input("Ingresa el nombre del estudiante (o 'salir' para terminar): ")
        if nombre.lower() == "salir":
            break
        calificacion = input(f"Ingrese la calificación de {nombre}: ")

        # Insertar el nodo
        lista.insertar_inicio(nombre, calificacion)

    # Mostrar resultado final
    lista.mostrar_lista()

