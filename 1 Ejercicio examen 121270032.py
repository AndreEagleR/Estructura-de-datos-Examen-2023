# Importar la libreria tkinter
import tkinter as tk

# Crear la funcion de busqueda lineal
def buscar_elemento():
    elemento = int(entry_buscar.get())
    if elemento in arreglo:
        resultado.set(f"El elemento {elemento} se encuentra en el arreglo.")  # Se utilizo  f-string para evaluar y reemplazar los valores dentro del {}
    else:
        resultado.set(f"El elemento {elemento} no se encuentra en el arreglo.")

def mostrar_arreglo():
    resultado.set(f"Arreglo: {arreglo}")

# Funcion para agregar elementos en la ventana de tkinter
def agregar_elemento():
    elemento = int(entry_elemento.get())
    if elemento != 0:
        arreglo.append(elemento)
        entry_elemento.delete(0, tk.END)
    else:
        entry_elemento.config(state=tk.DISABLED)  # Deshabilitar el campo de entrada cuando se ingrese 0

arreglo = []

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("1. Ejercicio | Examen | 121270032")
ventana.geometry("500x300")

# Etiqueta y campo de entrada para agregar elementos al arreglo
label_elemento = tk.Label(ventana, text="Ingresar elemento:")
label_elemento.pack()
entry_elemento = tk.Entry(ventana)
entry_elemento.pack()

# Botón para agregar elementos al arreglo
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)
boton_agregar.pack()

# Etiqueta y campo de entrada para buscar un elemento en el arreglo
label_buscar = tk.Label(ventana, text="Buscar elemento:")
label_buscar.pack()
entry_buscar = tk.Entry(ventana)
entry_buscar.pack()

# Botón para buscar un elemento en el arreglo
boton_buscar = tk.Button(ventana, text="Buscar", command=buscar_elemento)
boton_buscar.pack()

# Botón para mostrar los valores del arreglo
boton_mostrar = tk.Button(ventana, text="Mostrar arreglo", command=mostrar_arreglo)
boton_mostrar.pack()

# Variable para mostrar el resultado de la búsqueda o los valores del arreglo
resultado = tk.StringVar()
label_resultado = tk.Label(ventana, textvariable=resultado)
label_resultado.pack()

# Crear la ejecucion de la ventana tkinter
ventana.mainloop()
