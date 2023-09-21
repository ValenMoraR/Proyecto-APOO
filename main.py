class Cancion:
    def __init__(self, nombre, album, artista):
        self.nombre = nombre
        self.album = album
        self.artista = artista

class ListaReproduccion:
    def __init__(self,nombre):
        self.nombre= nombre
        self.lista_canciones= [Cancion]

    def crear_lista(self):
        print(f"{self.nombre} ha sido creada")

    def agregar_cancion_lista(self,lista,cancion):
        lista = input("¿A cuál lista desea agregar el tema?")
        self.cancion.append()


    # def eliminar_lista(self):
    #     pass

   





    
# c1= Cancion("Quiero repetir","Odisea","Ozuna")
# print(c1.nombre)
# c2= Cancion("Ferxxo 30","Mor no le temas a las oscuridad","Feid")
# print(c2.nombre)

# l1= ListaReproduccion("perreito")
# l1.crear_lista()
# l1.crear_lista("perreito")

