from tkinter import *
from tkinter import PhotoImage
from PIL import Image,ImageTk

from logica import Funcionalidad

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
        self.dados = dados
        self.Cantidad_apuesta = ''



        self.Funcionalidad = Funcionalidad()

    def crear_tableros(self):

        self.Apuesta = Frame(self.raiz,width=500,height=1000, bg ="#fff")
        self.Apuesta.place(x=0,y=0)

        self.TableroVerde = Frame(self.raiz,width=901,height=800,bg="white")
        self.TableroVerde.place(x=500,y=0) 

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

    def pintar_tablero(self):

        imagen_tablero = Label(self.TableroVerde, image=  self.img_tablero)
        imagen_tablero.place(x=(0),y=0)
    

    def colocan_labels(self):

        self.Apuesta.place(x=0,y=0) 

        label_dinero = Label(self.Apuesta, text='Dinero:',  bg ="#fff")
        label_dinero.config(font=("Verdana",30))
        label_dinero.place(x=(20),y=10)

        simbolo_dinero = Label(self.Apuesta, text='$',  bg ="#fff")
        simbolo_dinero.config(font=("Verdana",30))
        simbolo_dinero.place(x=(250),y=10)

        Cantidad_dinero = Label(self.Apuesta, text='1000',  bg ="#fff")
        Cantidad_dinero.config(font=("Verdana",30))
        Cantidad_dinero.place(x=(300),y=10)


        label_apuesta = Label(self.Apuesta, text='Apuesta:',  bg ="#fff")
        label_apuesta.config(font=("Verdana",30))
        label_apuesta.place(x=(20),y=60)

        signo = Label(self.Apuesta, text='$',bg ="#fff")
        signo.config(font=("Verdana",30))
        signo.place(x=(250),y=60)

        self.Cantidad_apuesta = Label(self.Apuesta, text= '0',bg ="#fff")
        self.Cantidad_apuesta.config(font=("Verdana",30))
        self.Cantidad_apuesta.place(x=300,y=60)

    def colocan_botones_fichas(self):
        self.btn_1= Button(self.Apuesta,image=self.img, bg ="#fff",text='+1') 
        self.btn_1.place(x=70, y=120) 

        self.btn_5= Button(self.Apuesta,image=self.img_5, bg ="#fff",text='+1') 
        self.btn_5.place(x=130, y=120) 

        self.btn_10= Button(self.Apuesta,image=self.img_10, bg ="#fff",text='+1') 
        self.btn_10.place(x=190, y=120) 

        self.btn_25= Button(self.Apuesta,image=self.img_25, bg ="#fff",text='+1') 
        self.btn_25.place(x=250, y=120) 

        self.btn_50= Button(self.Apuesta,image=self.img_50, bg ="#fff",text='+1') 
        self.btn_50.place(x=310, y=120) 


    def colorar_cotones_apuestas(self):
        self.btn_a_3= Button(self.Apuesta, bg ="#fff",text='3',width=6,height=11) 
        self.btn_a_3.place(x=17, y=180) 

        self.btn_a_6= Button(self.Apuesta, bg ="#fff",text='6',width=6,height=3) 
        self.btn_a_6.place(x=70, y=180) 

        self.btn_a_5= Button(self.Apuesta, bg ="#fff",text='5',width=6,height=3) 
        self.btn_a_5.place(x=70, y=240) 

        self.btn_a_4= Button(self.Apuesta, bg ="#fff",text='4',width=6,height=3) 
        self.btn_a_4.place(x=70, y=300) 

        self.btn_a_4_6= Button(self.Apuesta, bg ="#fff",text='4 to 6',width=6,height=3) 
        self.btn_a_4_6.place(x=70, y=360) 

        self.btn_a_inpar= Button(self.Apuesta, bg ="#fff",text='Inpar',width=6,height=3) 
        self.btn_a_inpar.place(x=70, y=420) 

        self.btn_a_9= Button(self.Apuesta, bg ="#fff",text='9',width=6,height=3) 
        self.btn_a_9.place(x=130, y=180) 

        self.btn_a_8= Button(self.Apuesta, bg ="#fff",text='8',width=6,height=3) 
        self.btn_a_8.place(x=130, y=240) 

        self.btn_a_7= Button(self.Apuesta, bg ="#fff",text='7',width=6,height=3) 
        self.btn_a_7.place(x=130, y=300) 

        self.btn_a_7_9= Button(self.Apuesta, bg ="#fff",text='7 to 9',width=6,height=3) 
        self.btn_a_7_9.place(x=130, y=360) 

        self.btn_a_par= Button(self.Apuesta, bg ="#fff",text='Par',width=6,height=3) 
        self.btn_a_par.place(x=130, y=420) 

        self.btn_a_12= Button(self.Apuesta, bg ="#fff",text='12',width=6,height=3) 
        self.btn_a_12.place(x=190, y=180) 

        self.btn_a_11= Button(self.Apuesta, bg ="#fff",text='11',width=6,height=3) 
        self.btn_a_11.place(x=190, y=240) 

        self.btn_a_10= Button(self.Apuesta, bg ="#fff",text='10',width=6,height=3) 
        self.btn_a_10.place(x=190, y=300) 

        self.btn_a_4_6= Button(self.Apuesta, bg ="#fff",text='10 to 12',width=6,height=3) 
        self.btn_a_4_6.place(x=190, y=360) 

        self.btn_a_rojo= Button(self.Apuesta, bg ="#fff",text='Rojo',width=6,height=3) 
        self.btn_a_rojo.place(x=190, y=420) 

        self.btn_a_15= Button(self.Apuesta, bg ="#fff",text='15',width=6,height=3) 
        self.btn_a_15.place(x=250, y=180) 

        self.btn_a_14= Button(self.Apuesta, bg ="#fff",text='14',width=6,height=3) 
        self.btn_a_14.place(x=250, y=240) 

        self.btn_a_13= Button(self.Apuesta, bg ="#fff",text='13',width=6,height=3) 
        self.btn_a_13.place(x=250, y=300) 

        self.btn_a_13_15= Button(self.Apuesta, bg ="#fff",text='13 to 15',width=6,height=3) 
        self.btn_a_13_15.place(x=250, y=360) 

        self.btn_a_negro= Button(self.Apuesta, bg ="#fff",text='Negro',width=6,height=3) 
        self.btn_a_negro.place(x=250, y=420) 

        self.btn_a_18= Button(self.Apuesta, bg ="#fff",text='18',width=6,height=3) 
        self.btn_a_18.place(x=310, y=180) 

        self.btn_a_17= Button(self.Apuesta, bg ="#fff",text='17',width=6,height=3) 
        self.btn_a_17.place(x=310, y=240) 

        self.btn_a_16= Button(self.Apuesta, bg ="#fff",text='16',width=6,height=3) 
        self.btn_a_16.place(x=310, y=300) 

        self.btn_a_16_18= Button(self.Apuesta, bg ="#fff",text='16 to 18',width=6,height=3) 
        self.btn_a_16_18.place(x=310, y=360) 

        self.btn_a_18= Button(self.Apuesta, bg ="#fff",text='3 colum',width=6,height=3) 
        self.btn_a_18.place(x=370, y=180) 

        self.btn_a_17= Button(self.Apuesta, bg ="#fff",text='2 colum',width=6,height=3) 
        self.btn_a_17.place(x=370, y=240) 

        self.btn_a_16= Button(self.Apuesta, bg ="#fff",text='1 colum',width=6,height=3) 
        self.btn_a_16.place(x=370, y=300) 

        self.tirar= Button(self.Apuesta, bg ="#fff",text='Tirar dados') 
        self.tirar.config(font=("Verdana",20))
        self.tirar.place(x=150, y=480) 

        self.limpiar = Button(self.Apuesta, bg ="#fff",text='Limpiar') 
        self.limpiar.config(font=("Verdana",20))
        self.limpiar.place(x=170, y=540) 

    def agregar_funciones_botones(self):
        self.limpiar['command'] = self.fun_limpiar

        Cantidad_apuesta['text'] = cantidad_apuesta

        self.btn_1['command'] = self.Funcionalidad.aumentar_apuesta_1

    def fun_limpiar(self):   
        
        imagen_tablero = Label(self.TableroVerde, image=self. img_tablero)
        imagen_tablero.place(x=(0),y=0)
        
        limpiada = Label(self.Apuesta, width= 500, height=100,  bg ="#fff")
        limpiada.place(x=70,y=640)



