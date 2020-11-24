from tkinter import *
from tkinter import PhotoImage
from PIL import Image,ImageTk


class Tablero:
    def __init__(self,raiz,img='',img_5='',img_25='',img_50='',img_100='',img_tablero='',Apuesta='',TableroVerde='',dados=[0,1,2,3,4,5,6]):
        self.raiz = raiz
        self.img = img
        self.img_5 = img_5
        self.img_25 = img_25   
        self.img_50 = img_50
        self.img_100 = img_100
        self.img_tablero = img_tablero
        self.Apuesta = Apuesta
        self.TableroVerde = TableroVerde

    def crear_tableros(self):
        self.Apuesta = Frame(self.raiz,width=500,height=1000, bg ="#fff")
        self.TableroVerde = Frame(self.raiz,width=901,height=800,bg="white")
    

    def obtener_imagenes(self): 
        self.img = Image.open('Ficha_1.png')
        self.img = ImageTk.PhotoImage(self.img)

        self.img_5 = Image.open('Ficha_5.png')
        self.img_5 = ImageTk.PhotoImage(self.img_5)

        self.img_10 = Image.open('Ficha_10.png')
        self.img_10 = ImageTk.PhotoImage(self.img_10)

        self.img_25 = Image.open('Ficha_25.png')
        self.img_25 = ImageTk.PhotoImage(self.img_25)

        self.img_50 = Image.open('Ficha_50.png')
        self.img_50 = ImageTk.PhotoImage(self.img_50)

        self.img_100 = Image.open('Ficha_100.png')
        self.img_100 = ImageTk.PhotoImage(self.img_100)

        self.img_tablero= Image.open('Tablero.png')
        self.img_tablero= ImageTk.PhotoImage(self.img_tablero)
    
        self.dados[1] = Image.open('1.png')
        self.dados[1] = ImageTk.PhotoImage(self.dados[1])

        self.dados[2] = Image.open('2.png')
        self.dados[2] = ImageTk.PhotoImage(self.dados[2])

        self.dados[3] = Image.open('3.png')
        self.dados[3] = ImageTk.PhotoImage(self.dados[3])

        self.dados[4] = Image.open('4.png')
        self.dados[4] = ImageTk.PhotoImage(self.dados[4])

        self.dados[5] = Image.open('5.png')
        self.dados[5] = ImageTk.PhotoImage(self.dados[5])

        self.dados[6] = Image.open('6.png')
        self.dados[6] = ImageTk.PhotoImage(self.dados[6])


















    # def crear_tablero_apuesta(self):
        
    #     self.Apuesta.place(x=0,y=0) 

    #     label_dinero = Label(self.Apuesta, text='Dinero:',  bg ="#fff")
    #     label_dinero.config(font=("Verdana",30))
    #     label_dinero.place(x=(20),y=10)

    #     simbolo_dinero = Label(self.Apuesta, text='$',  bg ="#fff")
    #     simbolo_dinero.config(font=("Verdana",30))
    #     simbolo_dinero.place(x=(250),y=10)

    #     Cantidad_dinero = Label(self.Apuesta, text='1000',  bg ="#fff")
    #     Cantidad_dinero.config(font=("Verdana",30))
    #     Cantidad_dinero.place(x=(300),y=10)


    #     label_apuesta = Label(self.Apuesta, text='Apuesta:',  bg ="#fff")
    #     label_apuesta.config(font=("Verdana",30))
    #     label_apuesta.place(x=(20),y=60)

    #     signo = Label(self.Apuesta, text='$',bg ="#fff")
    #     signo.config(font=("Verdana",30))
    #     signo.place(x=(250),y=60)

    #     Cantidad_apuesta = Label(self.Apuesta, text= '0',bg ="#fff")
    #     Cantidad_apuesta.config(font=("Verdana",30))
    #     Cantidad_apuesta.place(x=(300),y=60)

    # def crear_imagenes(self):
    #     

    #     btn_1= Button(self.Apuesta,image=self.img, bg ="#fff",text='+1',command=aumentar_apuesta_1) 
    #     btn_1.place(x=70, y=120) 

    #     

    #     btn_5= Button(self.Apuesta,image=self.img_5, bg ="#fff",text='+1',command=aumentar_apuesta_5) 
    #     btn_5.place(x=130, y=120) 

    #     

    #     btn_10= Button(self.Apuesta,image=self.img_10, bg ="#fff",text='+1',command=aumentar_apuesta_10) 
    #     btn_10.place(x=190, y=120) 

    #    

    #     btn_25= Button(self.Apuesta,image=self.img_25, bg ="#fff",text='+1',command=aumentar_apuesta_25) 
    #     btn_25.place(x=250, y=120) 

    #     

    #     btn_50= Button(self.Apuesta,image=self.img_50, bg ="#fff",text='+1',command=aumentar_apuesta_50) 
    #     btn_50.place(x=310, y=120) 

    #     

    #     self.img_tablero= Image.open('Tablero.png')
    #     self.img_tablero= ImageTk.PhotoImage(self.img_tablero)

    # def crear_tablero_ruleta(self):
    #     Tablero = Frame(raiz,width=901,height=800,bg="white")
    #     Tablero.place(x=500,y=0) 

    #     imagen_tablero = Label(Tablero, image=img_tablero)
    #     imagen_tablero.place(x=(0),y=0)