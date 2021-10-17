from tkinter import *
from PIL import Image,ImageTk
ventana =Tk()
ventana.geometry("750x500")
img=Image.open("./21-tkinter/p/dog.jpg")
render=ImageTk.PhotoImage(img)
Label(ventana,image=render).pack()
ventana.mainloop()