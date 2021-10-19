from tkinter import *
from tkinter import messagebox as box

ventana=Tk()
ventana.config(bd=70)

def sacarAlerta():
        box.showinfo("alerta","soy una alerta")
def salir(nombre):
        print(nombre)
        resultado= box.askquestion("salir","quieres salir")
        if resultado !="yes":
            box.showinfo("adios",f"adios{nombre}")
            ventana.destroy()
Button(ventana,text="mostrar alerta",command=lambda:salir("IGNACIO"))
ventana.mainloop()