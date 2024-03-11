import tkinter as tk
from tkinter import filedialog, messagebox

class Cancion:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion

class Album:
    def __init__(self, nombre, año, imagen):
        self.nombre = nombre
        self.año = año
        self.imagen = imagen
        self.canciones = []

    def add_cancion(self, cancion):
        self.canciones.append(cancion)

def agregar_album():
    nombre = nombre_entry.get()
    año = año_entry.get()
    imagen = imagen_path
    album = Album(nombre, año, imagen)
    for i in range(12):
        cancion_nombre = canciones_nombre_entry[i].get()
        cancion_duracion = canciones_duracion_entry[i].get()
        if cancion_nombre and cancion_duracion:
            album.add_cancion(Cancion(cancion_nombre, cancion_duracion))
    albums.append(album)
    messagebox.showinfo("Éxito", "Álbum agregado correctamente")
    limpiar_campos()
    
def cargar_imagen():
    global imagen_path
    imagen_path = filedialog.askopenfilename()
    if imagen_path:
        # Cargar la imagen seleccionada y mostrarla en la interfaz
        imagen_preview.image = tk.PhotoImage(file=imagen_path)
        imagen_preview.config(image=imagen_preview.image)
    
def limpiar_campos():
    nombre_entry.delete(0, tk.END)
    año_entry.delete(0, tk.END)
    for entry_nombre in canciones_nombre_entry:
        entry_nombre.delete(0, tk.END)
    for entry_duracion in canciones_duracion_entry:
        entry_duracion.delete(0, tk.END)
    # Limpiar también la vista previa de la imagen
    imagen_preview.config(file="")

        
def mostrar_albums():
    for album in albums:
        print("Álbum:", album.nombre)
        print("Año:", album.año)
        print("Imagen:", album.imagen)
        print("Canciones:")
        for cancion in album.canciones:
            print("- Nombre:", cancion.nombre)
            print("  Duración:", cancion.duracion)
        print()


def mostrar_albums_gui():
    for album in albums:
        frame = tk.Frame(cards_frame, relief=tk.RAISED, borderwidth=2)
        frame.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(frame, text=f"Álbum: {album.nombre}")
        label.pack()

        label = tk.Label(frame, text=f"Año: {album.año}")
        label.pack()

        label = tk.Label(frame, text="Canciones:")
        label.pack()

        for cancion in album.canciones:
            label = tk.Label(frame, text=f"- Nombre: {cancion.nombre}, Duración: {cancion.duracion}")
            label.pack()

        # Agregar imagen (puedes cargarla desde el archivo imagen en el disco)
        #image = tk.PhotoImage(file=album.imagen)
        #label = tk.Label(frame, image=image)
        #label.pack()

albums = []

root = tk.Tk()
root.title("Sistema de Stock de Disquería")




# Pantalla principal
main_frame = tk.Frame(root)
main_frame.pack(pady=20, fill="both", expand="1")

def cargar_formulario():
    main_frame.pack_forget()
    form_frame.pack()

def ver_albums():
    main_frame.pack_forget()
    cards_frame.pack()
    mostrar_albums_gui()

def salir():
    root.quit()
    
    
# Botones de la pantalla principal
btn_cargar = tk.Button(main_frame, text="Cargar Nuevo Disco", command=cargar_formulario)
btn_cargar.pack(pady=10)

btn_ver = tk.Button(main_frame, text="Ver Discos", command=ver_albums)
btn_ver.pack(pady=10)

btn_salir = tk.Button(main_frame, text="Salir", command=salir)
btn_salir.pack(pady=10)

# Formulario para cargar un nuevo disco
form_frame = tk.Frame(root)

# Vista previa de la imagen
imagen_preview = tk.Label(form_frame)
imagen_preview.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Campo para seleccionar la imagen
imagen_button = tk.Button(form_frame, text="Cargar Imagen", command=cargar_imagen)
imagen_button.grid(row=1, column=0, padx=5, pady=5)



# Otros campos del formulario
nombre_label = tk.Label(form_frame, text="Nombre del Álbum:")
nombre_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
nombre_entry = tk.Entry(form_frame)
nombre_entry.grid(row=2, column=1, padx=5, pady=5)

año_label = tk.Label(form_frame, text="Año del Álbum:")
año_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
año_entry = tk.Entry(form_frame)
año_entry.grid(row=3, column=1, padx=5, pady=5)

# Entradas para las canciones
canciones_nombre_label = tk.Label(form_frame, text="Nombre de la Canción:")
canciones_nombre_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
canciones_nombre_entry = []
for i in range(12):
    entry = tk.Entry(form_frame)
    entry.grid(row=5+i, column=0, padx=5, pady=5, sticky="w")
    canciones_nombre_entry.append(entry)

canciones_duracion_label = tk.Label(form_frame, text="Duración de la Canción:")
canciones_duracion_label.grid(row=4, column=1, padx=5, pady=5, sticky="w")
canciones_duracion_entry = []
for i in range(12):
    entry = tk.Entry(form_frame)
    entry.grid(row=5+i, column=1, padx=5, pady=5, sticky="w")
    canciones_duracion_entry.append(entry)

# Botón para agregar álbum
btn_agregar = tk.Button(form_frame, text="Agregar", command=agregar_album)
btn_agregar.grid(row=18, column=0, columnspan=2, padx=5, pady=5)

btn_volver = tk.Button(form_frame, text="Volver", command=lambda:[form_frame.pack_forget(), main_frame.pack()])
btn_volver.grid(row=18, column=1, columnspan=4, padx=5, pady=5)

# Frame para mostrar los discos
cards_frame = tk.Frame(root)

root.mainloop()