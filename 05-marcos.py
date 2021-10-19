from tkinter import *

ventana =Tk()
ventana.title("Lunes")
ventana.geometry("700x400")


marco=Frame(ventana,width=250,height=250)
marco.config(
    bg="red",
    bd=12,
    relief=SOLID

)
marco.pack(side=LEFT, anchor=NE)
marco=Frame(ventana,width=250,height=250)
marco.config(
    bg="green",
    bd=12,
    relief=SOLID

)
marco.pack(side=RIGHT, anchor=NE)



padre= Frame(marco, width=300, height=300)
padre.config(
    bg="pink",
    bd=12,
    relief=SOLID

)
padre.pack(side=TOP,fill=X, expand=YES)

marco=Frame(ventana,width=250,height=250)
marco.config(
    bg="blue",
    bd=12,
    relief=SOLID

)
marco.pack_propagate(False)
marco.pack(side=TOP,fill=X, expand=YES)
texto=Label(marco,text="primer marco")
texto.pack()
marco=Frame(marco,width=250,height=250)
ventana.mainloop()
