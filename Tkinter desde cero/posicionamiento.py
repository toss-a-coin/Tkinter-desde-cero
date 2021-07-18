from tkinter import *

root = Tk()
root.title("Posicionar")
root.geometry("400x200")

# label = Label(root, text = "Etiqueta")
# #label.grid(row = 0, column = 0) Si usamos el metodo 'grid' no se necesitara usar el metodo 'pack'
# label.place(x = 30, y = 40)
#
# btn = Button(root, text = "Boton")
# btn.grid(row = 1, column = 0)

def saludo():
    print("Hola te saludo")

def minimizar():
    root.iconify()

label = Label(root, text = "Saluda desde aqui:")
label.place(x = 30, y = 50 )

label2 = Label(root, text = "Minimizar aqui")
label2.place(x = 30, y = 100 )

btn = Button(root, text = "Haz click aqui para saludar:", command = saludo)
btn.place(x = 200, y = 50)

btn2 = Button(root, text = "Haz click aqui para minimizar:", command = minimizar)
btn2.place(x = 200, y = 100)

root.mainloop()
