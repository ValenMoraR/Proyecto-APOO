from cod import Reproductor,Cancion

def main ():
    reproducir = Reproductor()

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
