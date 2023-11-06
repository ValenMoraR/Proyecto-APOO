from code_1 import tk, Reproductor

ventana = tk.Tk()
ventana.geometry("620x300")
ventana.resizable(width=0, height=0)

reproductor = Reproductor(ventana)
reproductor.cargar_favoritos()
if __name__ == "__main__": 
    ventana.mainloop()