from tkinter import *

ventana=Tk()
ventana.geometry("750x750")
ventana.title("formularios")
encabezado=Label(ventana,text="formulario 1")
encabezado.config(
    fg="white", 
    bg="darkgray"
)
encabezado.grid(row=0,column=0,columnspan=2,sticky=W)

#label  
label =Label(ventana,text="nombre")
label.grid(row=1,column=0,pady=4,padx=4)
label2 =Label(ventana,text="apellido")
label2.grid(row=2,column=0,pady=4,padx=4)

txt_name=Entry(ventana)
txt_name.grid(row=1,column=1,sticky=W,padx=5,pady=5)
txt_name2=Entry(ventana)
txt_name2.grid(row=2,column=1,sticky=W,padx=5,pady=5)

btn_01=Button(ventana,text="Enviar")
btn_01.grid(row=4,column=1)

ventana.mainloop()