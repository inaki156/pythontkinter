import tkinter


from tkinter import *
ventana =Tk()
mi_menu=Menu(ventana)
ventana.config(menu=mi_menu)
ventana.geometry("600x600")

archivo=Menu(mi_menu)
archivo.add_command(label="nuevo archivo")
archivo.add_command(label="nueva ventana")
archivo.add_separator()
archivo.add_command(label="abrir archivo")
archivo.add_command(label="abrir ventana")
archivo.add_command(label="salir",command=ventana.quit)
mi_menu.add_cascade(label="archivo",menu=archivo)
mi_menu.add_cascade(label="editar")
mi_menu.add_cascade(label="seleccionar")

ventana.mainloop()