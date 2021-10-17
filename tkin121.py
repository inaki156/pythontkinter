from tkinter import *
import os.path


class Programa:
    def __init__(self):
        self.title = "python"
        self.icono = "./p/tiktok.ico"
        self.icono_alt = "./21-tkinter/p/tiktok.ico"
        self.resiable = True
        

    def cargar(self):
          # crear ventana
        windosw = Tk()
        self.windows=windosw

        # titulo de la ventana
        windosw.title(self.title)
        # comprobacion
        ruta_icono = os.path.abspath(self.icono)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icono_alt)

        # mostrar texto en el programa
        texto = Label(windosw, text=ruta_icono)
        texto.pack()
        # bloquear el tamaño de la ventana
        if self.resiable:
            windosw.resizable(1,1)
        else:
            windosw.resizable(0,0)
        # windosw.resizable(0,0)
        windosw.iconbitmap(ruta_icono)
        # este metodo tiene que ir al final para cargar la ventana
       

    def mostrar(self):
        self.windows.mainloop()
    

#instancia
programa =Programa()
programa.cargar()
programa.mostrar()


      
