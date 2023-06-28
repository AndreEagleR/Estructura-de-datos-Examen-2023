import tkinter as tk

arreglo = []

def valoresArreglo():
    dato = entrada.get()
    if dato != '0':
        arreglo.append(int(dato))
        entrada.delete(0, tk.END)
        print(arreglo)
    else:
        print('Se ha terminado de llenar el arreglo')
        agregar.config(state=tk.DISABLED)

def seleccion():
    n = len(arreglo)
    for i in range(n):
        # Encuentra el valor máximo en la parte no ordenada del arreglo
        max_idx = i
        for j in range(i+1, n):
            if arreglo[j] > arreglo[max_idx]:
                max_idx = j

        # Intercambia el valor máximo encontrado con el elemento actual
        arreglo[i], arreglo[max_idx] = arreglo[max_idx], arreglo[i]

    print("Arreglo ordenado de mayor a menor:", arreglo)

    # Tamaño del arreglo
    size = len(arreglo)
    print("Tamaño del arreglo:", size)

    # Promedio de los valores
    promedio = sum(arreglo) / size
    print("Promedio de los valores:", promedio)

    # Suma de los elementos del arreglo
    sumaelementos = sum(arreglo)
    print("Suma de los elementos del arreglo:", sumaelementos)


ventana = tk.Tk()
ventana.title("3 Ejercicio | Examen | 121270032")
ventana.geometry("500x300")

label1 = tk.Label(text="Ingrese los valores al arreglo")
label1.pack()

label0 = tk.Label(text="Ingrese 0 para dejar de ingresar datos")
label0.pack()

entrada = tk.Entry()
entrada.pack()

agregar = tk.Button(text="Agregar", command=valoresArreglo)
agregar.pack()

evaluar = tk.Button(text="Evaluar arreglo", command=seleccion)
evaluar.pack()

ventana.mainloop()

