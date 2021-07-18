import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tk.py")
root.geometry("500x300")

def seleccionar(opc):
    print(opc)

ttk.Button(root, text = "Python", command = lambda: seleccionar("Python")).pack()  #Lambda se usa cuando queremos recibir un parametro.
ttk.Button(root, text = "Java", command = lambda: seleccionar("Java")).pack()  #Lambda se usa cuando queremos recibir un parametro.
ttk.Button(root, text = "javaScript", command = lambda: seleccionar("javaScript")).pack()  #Lambda se usa cuando queremos recibir un parametro.


root.mainloop()
