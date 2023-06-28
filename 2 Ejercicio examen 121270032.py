import tkinter as tk
import queue

cola = queue.Queue()
arreglo = []

def agregarDatos():
    dato = ingresar.get() # Guardar el valor del numero ingresado
    if dato != '0':
        arreglo.append(dato) # Agregar el valor al arreglo
        cola.put(dato) # Agregar el valor a la cola
        ingresar.delete(0, tk.END) # Limpiar el espacio para ingresar
        print(arreglo)
        print("El tamaño de la cola es: ", cola.qsize())
    else:
        ingresar.config(state=tk.DISABLED)
        agregar.config(state=tk.DISABLED)

def descolar():
    if not cola.empty():
        print("La cola no esta vacia")
        dato = cola.get()
        print("El valor ",dato," Fue descolado")
        print("La cola disminuye a ", cola.qsize())
    else:
        "La cola esta llena"


ventana = tk.Tk()
ventana.title("2. Ejercicio | Examen | 121270032")
ventana.geometry("500x300")              


label1 = tk.Label(text="Ingrese los valores del arreglo")
label1.pack()

ingresar = tk.Entry()
ingresar.pack()

agregar = tk.Button(text="Agregar a la cola", command=agregarDatos)
agregar.pack()

label2 = tk.Label(text="Descolar un elemento")
label2.pack()


borrar = tk.Button(text="Descolar y verificar", command=descolar)
borrar.pack()

ventana.mainloop()
