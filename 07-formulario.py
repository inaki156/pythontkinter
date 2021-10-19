from tkinter import *
ventana=Tk()
ventana.config(
    bd=50
)
dato=StringVar()
resultado=StringVar()

def getDato():
  resultado.set(dato.get())
Label(ventana,text="texto").pack()
Entry(ventana,textvariable=dato).pack(anchor=NW)
Label(ventana,text="Dato recogido").pack(anchor=NW)
Label(ventana,textvariable=resultado).pack(anchor=NW)
Button(ventana,text="mostrar dato",command=getDato).pack(anchor=NW)

ventana.mainloop()