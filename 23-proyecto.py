from tkinter import *

ventana=Tk()
ventana.geometry("400x400")
ventana.resizable(0,0)
ventana.title("proyecto final Tkinter")
home_lbl=Label(ventana,text="inicio")
info_lbl=Label(ventana,text="informacion")
add_lbl=Label(ventana,text="añadir")
def ocultarLbl(lbl):
    lbl.grid_remove()

def home():
 
    home_lbl.grid(row=0,column=0)
    #ocultar pantalla
    info_lbl.grid_remove()
    add_lbl.grid_remove()
    
   
def info():
    
    info_lbl.grid(row=0,column=0)
    home_lbl.grid_remove()
    add_lbl.grid_remove()
   
def add():
    
    add_lbl.grid(row=0,column=0)
    info_lbl.grid_remove()
    home_lbl.grid_remove()



#creacion  del menu
mi_menu=Menu(ventana)
mi_menu.add_command(label="inicio",command=home)
mi_menu.add_cascade(label="añadir",command=add)
mi_menu.add_cascade(label="informacion",command=info)
mi_menu.add_command(label="salir",command=ventana.quit)
#cargarmenu
ventana.config(menu=mi_menu)
#campos del formulario
name_data=StringVar()
price_data=StringVar()
add_name_lbl=Label(ventana,text="nombre del producto")
add_name_entry=Entry(ventana,textvariable=name_data)

add_price_lbl=Label(ventana,text="precio del producto")
add_price_entry=Entry(ventana,textvariable=price_data)

add_description_label=Label(ventana,text="Descripcion")
add_descrition_entry=Text(ventana)

#pantalla

ventana.mainloop()


