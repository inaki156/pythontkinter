from tkinter import *

ventana =Tk()
web =IntVar()
movil =IntVar()
encabezado=Label(ventana,text="formulario 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green"
)

def mostrarJob():
    texto=""
    if web.get():
        texto +="desarrollo web"
        mostrar.config(text=texto)
    if movil.get():
         if web.get():
            texto +="desarrollo movil"
            mostrar.config(text=texto)
         else:
            texto +=" y desarrollo movil"
            mostrar.config(text=texto)
 
         
encabezado.grid(row=0,column=0 ,columnspan=5,sticky=W)
Label(ventana,text="a que te dedicas").grid(row=1,column=0)

mostrar =Label(ventana,bg="green",text="buenas")
Checkbutton(ventana,onvalue=1,offvalue=0,variable=web,text="desarrollo web",command=lambda:mostrarJob()).grid(row=2,column=0)
Checkbutton(ventana,onvalue=1,offvalue=0,variable=movil,text="desarrollo movil",command=lambda:mostrarJob()).grid(row=3,column=0)
mostrar.grid(row=4,column=0)
ventana.mainloop()