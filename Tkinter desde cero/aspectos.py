from tkinter import *
from gi.repository import Notify

root = Tk()
root.title("Entrada")
root.geometry("400x300")
Notify.init("MyProgram")
root.resizable(0,0)  #Este metodo sirve para que el geomertry que nosotros asiganamos sea fijo
n = Notify.Notification.new("Default Title","Default Body")
#StringVar son las variables que usamos para almacenar los datos de nuestras entradas.
name = StringVar()
surname = StringVar()
saludo = StringVar()

#La funcion set es como un placeholder pero la diferencia, es que se tiene que borrar para poder ingresar datos.
# name.set("Escribe aqui tu nombre:")
# surname.set("Escribe aqui tu apellido:")

def saludar():
    saludo.set("Hola " + name.get()+ " " + surname.get())
    n.update("Hola", str(saludo.get()))
    n.show()

#Etiqueta Nombre
label = Label(root, text = "Escribe tu nombre:", bd = 4, bg = "red", font = ("Curier 10"))
label.place(x = 10, y = 10)

#Entrada de Nombre
entry = Entry(root, textvariable = name, bd = 5)
entry.place(x = 170, y = 10)

#Etiqueta apellido
label2 = Label(root, text = "Escribe tu apellido:", bd = 4, bg = "red", font = ("Curier 10"))
label2.place(x = 10, y = 40)

#Entrada de Apellido
entry2 = Entry(root, textvariable = surname, bd = 5)
entry2.place(x = 170, y = 40)

#Boton
btn = Button(root, text = "Saludar ahora", command = saludar, bd = 5, bg = "red")
btn.place(x = 112, y = 123)

entry3 = Entry(root, textvariable = saludo, bd = 20, font = ("Curier 10"), state = "disable") #Con state, el usuario no podra maniupar la entrada.
entry3.place(x = 70, y = 221)



root.mainloop()
