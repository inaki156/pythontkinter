from tkinter import *
from tkinter import messagebox as box

ventana=Tk()
ventana.geometry("400x400")
numero1=StringVar()
numero2=StringVar()
resultado=StringVar()

marco =Frame(ventana,width=250,height=250)
marco.config(
    bd=5,
    relief=SOLID,
    padx=15
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)
ventana.config(
    bd=25
)
def mostrarResultado():
    box.showinfo("resultado",f"el resultado es :{resultado.get()}")

def change(res):
    resultado.set(str(res))
def sumar():
    try:
        resuto=float(numero1.get())+float(numero2.get())
        resultado=change(resuto)
        mostrarResultado()
    except:
        box.showerror("error","introduce bien los datos")

def resta():
    try:
        resuto=float(numero1.get())-float(numero2.get())
        resultado=change(resuto)
        mostrarResultado()
    except:
        box.showerror("error","introduce bien los datos")
def multiplicar():
    try:
        resuto=float(numero1.get())*float(numero2.get())
        resultado=change(resuto)
        mostrarResultado()
    except:
        box.showerror("error","introduce bien los datos")

def dividir():
    try:
        resuto=float(numero1.get())/float(numero2.get())
        resultado=change(resuto)
        mostrarResultado()
    except:
        box.showerror("error","introduce bien los datos")


Label(marco,text="primer numero: ").pack()
Entry(marco,textvariable=numero1,justify="center").pack()
Label(marco,text="segundo numero: ").pack()
Entry(marco,textvariable=numero2,justify="center").pack()

Label(marco,text="").pack()
Button(marco,text="+",command=lambda:sumar()).pack(side="right")
Button(marco,text="-",command=lambda:resta()).pack(side="right")
Button(marco,text="*",command=lambda:multiplicar()).pack(side="right")
Button(marco,text="/",command=lambda:dividir()).pack(side="right")
ventana.mainloop()
