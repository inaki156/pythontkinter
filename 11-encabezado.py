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

Label(ventana,text="genero").grid(row=5)
opcion =StringVar()
opcion.set(None)
def marcar():
    marcado.config(text=opcion.get())
def seleccionado():
    selecion.config(text=opcion.get())
#radiobuttons
Radiobutton(ventana,text="masculino",variable=opcion,command=marcar,value="masculino").grid(row=6)
Radiobutton(ventana,text="femenino",variable=opcion,command=marcar,value="femenino").grid(row=7)
marcado=Label(ventana)
marcado.grid(row=8)
#menu
opcion=StringVar()
opcion.set("opcion 1")
select =OptionMenu(ventana,opcion,"opcion 1","opcion 2","opcion 3","opcion 4")
select.grid(row=6,column=1)
Button(ventana,text="ver",command=seleccionado).grid(row=7,column=1)
selecion=Label(ventana)
selecion.grid(row=8,column=1)
ventana.mainloop()