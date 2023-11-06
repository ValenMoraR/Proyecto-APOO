import tkinter as tk
from tkinter import messagebox 
from tkinter import simpledialog
import pygame
from pygame import mixer
import random
import threading 
import json
import os

pygame.init()
mixer.init()

class Cancion:
    def __init__(self, nombre, archivo):
        self.nombre = nombre
        self.archivo = archivo
        self.es_favorita = False

class Reproductor:
    def __init__(self, ventana):
        self.ventana = ventana
        self.canciones = []  # Lista de canciones
        self.playlist_frame = None
        self.cancion_actual = None  # Canción actual
        self.lista_activa = None
        self.listas_de_reproduccion = {
            "Temas de Feid": [Cancion("Chorrito Pa Las Ánimas - Feid", "canciones/ChorritoPaLasAnimas.mp3"), Cancion("Normal - Feid", "canciones/Normal.mp3"), Cancion("Feliz Cummpleaños FERXXO - Feid", "canciones/FelizCumpleañosFerxxo.mp3"), Cancion("FERXXO 100 - Feid", "canciones/Ferxxo100.mp3"), Cancion("FUMETEO - Feid, Mora, Eladio Carrion", "canciones/Fumeteo.mp3"), Cancion("PERRO NEGRO - Bad Bunny, Feid", "PerroNegro.mp3")],
            "Temas de Eladio Carrion": [Cancion("Haciendo Dinero - Eladio Carrion", "canciones/HaciendoDinero.mp3"), Cancion("Mala Mía Otra Vez - Eladio Carrion", "canciones/MalaMiaOtraVez.mp3"), Cancion("FUMETEO - Feid, Mora, Eladio Carrion", "canciones/Fumeteo.mp3"), Cancion("THUNDER Y LIGHTNING - Bad Bunny, Eladio Carrion", "canciones/ThunderYLightning.mp3")],
            "Temas en Inglés": [Cancion("Thriller (Shortened Version) - Michael Jackson", "canciones/Thriller.mp3"), Cancion("It Was A Good Day - Ice Cube", "canciones/ItwasAgoodDay.mp3"), Cancion("God's Plan - Drake", "canciones/GodsPlan.mp3"), Cancion("Calm Down - Rema", "canciones/CalmDown.mp3")],
            "NSLQVAPM Bad Bunny": [Cancion("MONACO - Bad Bunny", "canciones/Monaco.mp3"), Cancion("PERRO NEGRO - Bad Bunny, Feid", "PerroNegro.mp3"), Cancion("THUNDER Y LIGHTNING - Bad Bunny, Eladio Carrion", "canciones/ThunderYLightning.mp3")],
            "Favoritos": []  # Lista de reproducción "Favoritos"
        }
        self.cargar_favoritos()

        # Crear elementos de la interfaz gráfica
        self.ventana.title("Reproductor de Audio")
        self.icono = tk.PhotoImage(file="icono.png")  # Reemplaza "icono.png" con tu icono
        self.ventana.tk.call('wm', 'iconphoto', self.ventana._w, self.icono)

        # Sección para añadir listas de reproducción (background morado)
        self.playlist_frame = tk.Frame(self.ventana, bg="purple", height=250)
        self.playlist_frame.pack(fill="x")

        # Agregar botones para las listas de reproducción
        self.crear_botones_listas()

        # Sección para controlar el audio (background gris oscuro)
        controls_frame = tk.Frame(self.ventana, bg="darkgray")
        controls_frame.pack(fill="both", expand=True)

        # Botones para controlar el audio (organizados horizontalmente)
        self.pause_button = tk.Button(controls_frame, text="Pause", command=self.pausar)
        self.pause_button.pack(side="left")

        self.next_button = tk.Button(controls_frame, text="Siguiente", command=self.siguiente_cancion)
        self.next_button.pack(side="left")

        self.favorite_button = tk.Button(controls_frame, text="Favorito", command=self.agregar_a_favoritos)
        self.favorite_button.pack(side="left")

        self.create_playlist_button = tk.Button(controls_frame, text="Crear Lista", command=self.crear_lista_personalizada)
        self.create_playlist_button.pack(side="left")

        self.add_to_playlist_button = tk.Button(controls_frame, text="Añadir a Lista", command=self.agregar_cancion_a_lista)
        self.add_to_playlist_button.pack(side="left")

    def mostrar_lista(self, nombre_lista):
        lista_canciones = self.listas_de_reproduccion.get(nombre_lista, [])
        nueva_ventana = tk.Toplevel(self.ventana)  # Crea una nueva ventana
        nueva_ventana.title(nombre_lista)

        # Botón "Regresar" en la parte superior izquierda
        regresar_button = tk.Button(nueva_ventana, text="Regresar", command=nueva_ventana.destroy)
        regresar_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Botones de canciones en la nueva ventana
        for i, cancion in enumerate(lista_canciones):
            cancion_button = tk.Button(nueva_ventana, text=cancion.nombre, command=lambda c=cancion: self.reproducir_cancion(c))
            cancion_button.grid(row=i + 1, column=0, padx=10, pady=5, sticky="w")

        # Botón "Reproducir" para todas las canciones en orden aleatorio
        reproducir_button = tk.Button(nueva_ventana, text="Reproducir esta Playlist", command=lambda lc=lista_canciones: self.reproducir_aleatoriamente(lc))
        reproducir_button.grid(row=len(lista_canciones) + 1, column=0, padx=10, pady=10, sticky="w")

         # Actualizar la lista activa al mostrar una lista de reproducción
        self.lista_activa = self.listas_de_reproduccion.get(nombre_lista, [])

    # Métodos de Reproductor
    def reproducir_cancion(self, cancion):
        # Lógica para reproducir una canción
        if cancion:
            self.cancion_actual = cancion
            mixer.music.load(cancion.archivo)
            mixer.music.play()
            print(self.cancion_actual.nombre)

    def pausar(self):
        # Lógica para pausar la canción
        if mixer.music.get_busy():
            mixer.music.pause()
            print("Canción Pausada")
        else:
            mixer.music.unpause()
            print("Canción renaudada")

    def mostrar_favoritos(self):
        # Actualizar la lista "Favoritos" en el diccionario
        if self.cancion_actual in self.listas_de_reproduccion["Favoritos"]:
            self.listas_de_reproduccion["Favoritos"].remove(self.cancion_actual)
            print(f"{self.cancion_actual.nombre} Removida")
        else:
            self.listas_de_reproduccion["Favoritos"].append(self.cancion_actual)
            print(f"{self.cancion_actual.nombre} Agregada")

    def agregar_a_favoritos(self):
        if self.cancion_actual:
            # Marcar o desmarcar la canción como favorita
            self.cancion_actual.es_favorita = not self.cancion_actual.es_favorita
            self.mostrar_favoritos()
            self.guardar_favoritos()

    def reproducir_aleatoriamente(self, lista_canciones):
        if lista_canciones:
            # Detener la canción actual si se está reproduciendo
            pygame.mixer.music.stop()

            # Reproducir las canciones en un orden aleatorio en un hilo separado
            def reproducir_hilo():
                canciones_aleatorias = lista_canciones.copy()
                random.shuffle(canciones_aleatorias)

                for cancion in canciones_aleatorias:
                    mixer.music.load(cancion.archivo)
                    mixer.music.play()
                    print(cancion.nombre)
                    self.cancion_actual = cancion
                    while mixer.music.get_busy():
                        pygame.time.Clock().tick(10)  # Evitar bloquear la GUI

            # Crea un hilo para reproducir la música
            hilo = threading.Thread(target=reproducir_hilo)
            hilo.start()

    def siguiente_cancion(self):
        if self.lista_activa:
            # Detener la canción actual si se está reproduciendo
            mixer.music.stop()

            # Obtener una canción aleatoria de la lista activa
            cancion_aleatoria = random.choice(self.lista_activa)

            # Reproducir la canción aleatoria
            mixer.music.load(cancion_aleatoria.archivo)
            mixer.music.play()
            self.cancion_actual = cancion_aleatoria
            print("Canción omitida")
            print(self.cancion_actual.nombre)

    def cargar_favoritos(self):
        if os.path.exists("favoritos.json"):
            with open("favoritos.json", "r") as archivo:
                try:
                    datos_favoritos = json.load(archivo)
                    self.listas_de_reproduccion["Favoritos"] = [Cancion(cancion["nombre"], cancion["archivo"]) for cancion in datos_favoritos]
                except json.JSONDecodeError:
                    print("Error al decodificar el archivo JSON 'favoritos.json'. El archivo puede estar vacío o tener un formato incorrecto.")
        else:
            # Si el archivo no existe, crea una lista vacía de favoritos
            self.listas_de_reproduccion["Favoritos"] = []

    def guardar_favoritos(self):
        with open("favoritos.json", "w") as archivo:
            datos_favoritos = [{"nombre": cancion.nombre, "archivo": cancion.archivo} for cancion in self.listas_de_reproduccion["Favoritos"]]
            json.dump(datos_favoritos, archivo)

    def crear_botones_listas(self):
        # Borra los botones existentes de listas de reproducción
        for widget in self.playlist_frame.winfo_children():
            widget.destroy()

        # Crea los nuevos botones para todas las listas de reproducción
        for lista in self.listas_de_reproduccion:
            lista_button = tk.Button(self.playlist_frame, text=lista, command=lambda l=lista: self.mostrar_lista(l))
            lista_button.pack(side="left", padx=10, pady=10)

    def crear_lista_personalizada(self):
        nombre_lista = simpledialog.askstring("Crear Lista", "Ingresa el nombre de la nueva lista de reproducción:")
        if nombre_lista:
            self.listas_de_reproduccion[nombre_lista] = []
            self.crear_botones_listas()  # Actualizar los botones de las listas

            self.guardar_listas_de_reproduccion()

    def agregar_cancion_a_lista(self):
        if self.cancion_actual:
            # Crear una nueva ventana emergente para seleccionar la lista
            ventana_lista = tk.Toplevel(self.ventana)
            ventana_lista.title("Seleccionar Lista")

            # Crear una variable de control para la selección
            lista_seleccionada = tk.StringVar()

            # Crear una etiqueta y una lista desplegable para mostrar las listas
            tk.Label(ventana_lista, text="Selecciona una lista:").pack()
            listas_dropdown = tk.OptionMenu(ventana_lista, lista_seleccionada, *self.listas_de_reproduccion.keys())
            listas_dropdown.pack()

            # Botón para agregar la canción a la lista seleccionada
            agregar_button = tk.Button(ventana_lista, text="Agregar a Lista", command=lambda: self.agregar_cancion_seleccionada(lista_seleccionada.get()))
            agregar_button.pack()

            self.guardar_listas_de_reproduccion()

    def agregar_cancion_seleccionada(self, lista_seleccionada):
        if self.cancion_actual and lista_seleccionada:
            lista = self.listas_de_reproduccion.get(lista_seleccionada)
            if lista:
                lista.append(self.cancion_actual)
                print(f"{self.cancion_actual.nombre} agregada a la lista '{lista_seleccionada}'")
                self.guardar_listas_de_reproduccion()

    def guardar_listas_de_reproduccion(self):
        # Guardar las listas de reproducción en un archivo JSON
        with open("listas_de_reproduccion.json", "w") as archivo:
            json.dump(self.listas_de_reproduccion, archivo)


if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.geometry("700x100")

    reproductor = Reproductor(ventana)
    reproductor.cargar_favoritos()
    ventana.mainloop()
