from tkinter import *
from tkinter import font
ventana =Tk()
ventana.geometry("500x500")

texto=Label(ventana,text="Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="black",
    padx=20,
    pady=20,
    font=("Arial")
)
texto.pack()

word="sos un capo jefe"
texto =Label(ventana,text="soy ignacio Fernandez")
texto.pack()
texto.config(
    height=3,
    justify=RIGHT,
    anchor=SE,
    bg="red",
    font=("Arial",18),
    cursor="spider"
)
texto.pack(anchor=SE)
ventana.mainloop()