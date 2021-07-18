from tkinter import *
import time

root = Tk()
root.title("Mi primer ventana")
root.geometry("500x300")

btn = Button(root, text = "Minimizar", command = root.iconify, bg = "red")
btn.pack(side = LEFT) #Posiciona en una posicion especifico.

def imprimir():
    print("Imprimiendo.......")
    label = Label(root, text = "Imprimiendo......." )
    label.pack()

btn2 = Button(root, text = "Imprimir", command = imprimir, bg = "blue")
btn2.pack(side = RIGHT) #Posiciona en una posicion especifico.

root.mainloop()
