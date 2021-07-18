from tkinter import *
from gi.repository import Notify

root = Tk()
root.title("Entrada")
root.geometry("400x300")
Notify.init("MyProgram")
n = Notify.Notification.new("Default Title","Default Body")
#StringVar son las variables que usamos para almacenar los datos de nuestras entradas.
name = StringVar()
surname = StringVar()

#La funcion set es como un placeholder pero la diferencia, es que se tiene que borrar para poder ingresar datos.
# name.set("Escribe aqui tu nombre:")
# surname.set("Escribe aqui tu apellido:")

def saludar():
    print("Hola " + name.get() + " " + surname.get())
    n.update("Hola", name.get() + " " + surname.get())
    n.show()

#Etiqueta Nombre
label = Label(root, text = "Escribe tu nombre:")
label.place(x = 10, y = 10)

#Entrada de Nombre
entry = Entry(root, textvariable = name)
entry.place(x = 170, y = 10)

#Etiqueta apellido
label2 = Label(root, text = "Escribe tu apellido:")
label2.place(x = 10, y = 40)

#Entrada de Apellido
entry2 = Entry(root, textvariable = surname)
entry2.place(x = 170, y = 40)

#Boton
btn = Button(root, text = "Saludar ahora", command = saludar)
btn.place(x = 10, y = 100)


root.mainloop()
