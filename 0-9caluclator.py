from tkinter import *
from tkinter import messagebox as box



class Calculadora:
  
    def __init__(self):
        self.numero1=StringVar()
        self.numero2=StringVar()
        self.resultado=StringVar()

    def mostrarResultado(self):
        box.showinfo("resultado",f"el resultado es :{self.resultado.get()}")
    def change(self,res):
        self.resultado.set(str(res))
    def sumar(self):
       
            resuto=float(self.numero1.get())+float(self.numero2.get())
            resultado=self.change(resuto)
            self.mostrarResultado()
      

    def resta(self):
       
            resuto=float(self.numero1.get())+float(self.numero2.get())
            resultado=self.change(resuto)
            self.mostrarResultado()
        
    def multiplicar(self):
        
            resuto=float(self.numero1.get())+float(self.numero2.get())
            resultado=self.change(resuto)
            self.mostrarResultado()
   

    def dividir(self):
            resuto=float(self.numero1.get())/float(self.numero2.get())
            resultado=self.change(resuto)
            self.mostrarResultado()

  

ventana=Tk()
ventana.geometry("400x400")
calculadora=Calculadora()
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


Label(marco,text="primer numero: ").pack()
Entry(marco,textvariable=calculadora.numero1,justify="center").pack()
Label(marco,text="segundo numero: ").pack()
Entry(marco,textvariable=calculadora.numero2,justify="center").pack()

Label(marco,text="").pack()
Button(marco,text="+",command=lambda:calculadora.sumar()).pack(side="right")
Button(marco,text="-",command=lambda:calculadora.resta()).pack(side="right")
Button(marco,text="*",command=lambda:calculadora.multiplicar()).pack(side="right")
Button(marco,text="/",command=lambda:calculadora.dividir()).pack(side="right")
ventana.mainloop()
   