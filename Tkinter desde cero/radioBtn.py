from tkinter import *

root = Tk()
root.title("RadioButtons")
root.geometry("400x300")
root.config(bg = "goldenrod3")
root.resizable(0,0)

def operacion():
    number = num.get()
    if opc.get() == 1:
        total = number * 5

    elif opc.get() == 2:
        total = number * 10

    elif opc.get() == 3:
        total = number * 20

    elif opc.get() == 4:
        total = number * 30

    elif opc.get() == 5:
        total = number * 40

    else:
        total = number * number

    print("Total: " + str(total))


opc = IntVar()
num = IntVar()

label = Label(root, text = "Escriba su numero")
label.place(x = 20, y = 20)

entry = Entry(root, bd = 7, font = ("Helvetica 12"), textvariable = num)
entry.place(x = 150, y =20)

label2 = Label(root, text = "Elija la cantidad")
label2.place(x = 20, y = 50)

radioBtnX5 = Radiobutton(root, text = "x5", value = 1, bg = "goldenrod3", bd = 5, variable = opc)
radioBtnX5.place(x = 20, y = 80)

radioBtnX10 = Radiobutton(root, text = "x10", value = 2, bg = "goldenrod3", bd = 5, variable = opc)
radioBtnX10.place(x = 90, y = 80)

radioBtnX20 = Radiobutton(root, text = "x20", value = 3 ,bg = "goldenrod3", bd = 5, variable = opc)
radioBtnX20.place(x = 170, y = 80)

radioBtnX30 = Radiobutton(root, text = "x30", value = 4, bg = "goldenrod3", bd = 5, variable = opc)
radioBtnX30.place(x = 20, y = 110)

radioBtnX40 = Radiobutton(root, text = "x40", value = 5, bg = "goldenrod3", bd = 5, variable = opc)
radioBtnX40.place(x = 90, y = 110)

btn = Button(root, text = "Realizar operacion" , bg = "goldenrod3", bd = 5, command = operacion)
btn.place(x = 20, y = 140)




root.mainloop()
