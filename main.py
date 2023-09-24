class Cancion:
    def __init__(self, nombre, artista):
        self.nombre = nombre
        self.artista = artista

class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_canciones= []

    def agregar_cancion_lista(self,cancion):
        self.lista_canciones.append(cancion)

        

    def eliminar_cancion_lista(self,nombre):
        for cancion in self.lista_canciones:
            if cancion.nombre ==nombre:
                self.lista_canciones.remove(cancion)
                return True
        return False
    
    def mostrar_cancion(self):
        for i, cancion in enumerate(self.lista_canciones):
            print (f"{i + 1}.{cancion.nombre} - {cancion.artista}")

    def mostrar_canciones_lista(self):
        print (f"Canciones de la lista {self.nombre}: ")
        for i, cancion in enumerate(self.lista_canciones):
            print (f"{i + 1}.{cancion.nombre} - {cancion.artista}")

class Reproduccion:
    def __init__(self):
        self.lista_reproducciones= {}
        
    def crear_lista_reproducciones(self):
        nombre_lista =input("Ingrese el nombre de la lista de producciones: ")
        if nombre_lista in self.lista_reproducciones:
            print ("Ya existe una lista con ese nombre")
        else:
            self.lista_reproducciones[nombre_lista] = ListaReproduccion(nombre_lista)


    def mostrar_listas(self):
        print ("Listas de reproducción creadas")
        for lista_nombre in self.lista_reproducciones:
            print (lista_nombre)

def main ():
    reproducir = Reproduccion()

    while True:
        print ( "\n Ménu")
        print ("1. Crear una lista de reproducción")
        print ("2. Mostar listas creadas")
        print ("3. Mostar canciones de una lista")
        print ("4. Agregar una canción de una lista")
        print ("5. Eliminar una canción de una lista")
        print ("6. salir")

        opcion = input("Seleccione una de las siguientes funciones: ")

        if opcion == "1":
            reproducir.crear_lista_reproducciones()
        elif opcion == "2":
            reproducir.mostrar_listas()
        elif opcion == "3":
            nombres_listas =input ("Ingrese el nombre de la lista, para visualizar sus canciones: ")
            if nombres_listas in reproducir.lista_reproducciones:
                reproducir.lista_reproducciones[nombres_listas].mostrar_cancion()
        elif opcion == "4":
            nombres_listas= input("Ingrese el nombre de la lista a la cual desea agreagar la canción: ")
            if nombres_listas in reproducir.lista_reproducciones:
                nombre = input("Ingrese el nombre de la canción: ")
                artista = input("Ingrese el artista de la canción: ")
                cancion= Cancion(nombre, artista)
                reproducir.lista_reproducciones[nombres_listas].agregar_cancion_lista(cancion)
            else:
                print("La lista no ha sido creada")
        elif opcion == "5":
            nombres_listas = input("Ingrese el nombre de la lista a la cual desea eliminarle la canción: ")
            if nombres_listas in reproducir.lista_reproducciones:
                 nombre = input("Ingrese el nombre de la canción que va ha eliminar: ")
                 if reproducir.lista_reproducciones[nombres_listas].eliminar_cancion_lista(nombre):
                     print(f"La canción {nombre}, ha sido eliminada")

            else:
                print("La lista no ha sido creada")
        elif opcion == "6":
            break

if __name__ == "__main__":
    main()
