import tkinter as tk

arreglo = []

def valorArreglo():
    dato = agregar.get()
    if dato != '0':
        arreglo.append(int(dato))  # Convertir dato a entero y agregar al arreglo
        print("Valor", dato, "agregado al arreglo")
        print(arreglo)
    else:
        agregarBtn.config(state=tk.DISABLED)

def evaluacion():
    n = len(arreglo)
    # Ordenamiento burbuja
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
    print("Número mayor:", arreglo[-1])
    print("Número menor:", arreglo[0])
    print("Tamaño del arreglo:", len(arreglo))

ventana = tk.Tk()
ventana.title("4 Ejercicio | Examen | 121270032")
ventana.geometry("500x300")

label1 = tk.Label(text="Ingresar datos al arreglo")
label1.pack()

agregar = tk.Entry()
agregar.pack()

agregarBtn = tk.Button(text="Agregar", command=valorArreglo)
agregarBtn.pack()

evaluar = tk.Button(text="Valor mayor y menor", command=evaluacion)
evaluar.pack()

ventana.mainloop()

