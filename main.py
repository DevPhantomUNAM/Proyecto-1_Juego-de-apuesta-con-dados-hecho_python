from tkinter import *
from tkinter.filedialog import askopenfile 
from tkinter import PhotoImage
from PIL import Image,ImageTk
import random

raiz = Tk()
raiz.title('Juego de dados')
raiz.geometry('1401x800') 

#Variables 
cantidad_dinero = 1000
cantidad_apuesta = 0
cantidad_apuesta_sin_modificar = 0

apuesta = []

########################## Apuestas ##############################

def aumentar_apuesta_1():
    global cantidad_apuesta_sin_modificar
    global cantidad_dinero
    global cantidad_apuesta
    
    if cantidad_apuesta <=(cantidad_dinero-1):       
        cantidad_apuesta = cantidad_apuesta + 1
        cantidad_apuesta_sin_modificar = cantidad_apuesta_sin_modificar + 1
        Cantidad_apuesta['text'] = cantidad_apuesta
    
def aumentar_apuesta_5():    
    global cantidad_dinero
    global cantidad_apuesta
    global cantidad_apuesta_sin_modificar
    
    if cantidad_apuesta <=(cantidad_dinero-5):       
        cantidad_apuesta = cantidad_apuesta + 5
        cantidad_apuesta_sin_modificar = cantidad_apuesta_sin_modificar + 5
        Cantidad_apuesta['text'] = cantidad_apuesta

def aumentar_apuesta_10():    
    global cantidad_dinero
    global cantidad_apuesta
    global cantidad_apuesta_sin_modificar
    
    if cantidad_apuesta <=(cantidad_dinero-10):       
        cantidad_apuesta = cantidad_apuesta + 10
        cantidad_apuesta_sin_modificar = cantidad_apuesta_sin_modificar + 10
        Cantidad_apuesta['text'] = cantidad_apuesta
        
def aumentar_apuesta_25():    
    global cantidad_dinero
    global cantidad_apuesta
    global cantidad_apuesta_sin_modificar
    
    if cantidad_apuesta <=(cantidad_dinero-25):       
        cantidad_apuesta = cantidad_apuesta + 25
        cantidad_apuesta_sin_modificar = cantidad_apuesta_sin_modificar + 25
        Cantidad_apuesta['text'] = cantidad_apuesta
        
def aumentar_apuesta_50():    
    global cantidad_dinero
    global cantidad_apuesta
    global cantidad_apuesta_sin_modificar
    
    if cantidad_apuesta <=(cantidad_dinero-50):       
        cantidad_apuesta = cantidad_apuesta + 50
        cantidad_apuesta_sin_modificar = cantidad_apuesta_sin_modificar + 50
        Cantidad_apuesta['text'] = cantidad_apuesta
        
def aumentar_apuesta_100():    
    global cantidad_dinero
    global cantidad_apuesta
    global cantidad_apuesta_sin_modificar
    
    if cantidad_apuesta <=(cantidad_dinero-100):       
        cantidad_apuesta = cantidad_apuesta + 100
        cantidad_apuesta_sin_modificar = cantidad_apuesta_sin_modificar + 100
        Cantidad_apuesta['text'] = cantidad_apuesta
        
##----------------------------------------------------------##

def calculoApuesta(args, resultado):
    
    ganancia = [0]    
    par = resultado % 2
    
    
    print(f'90 Apuestas {args}')
    print(f'91 Resultado {resultado}')
    print(f'92 Numero Par: {par}' )
    
    #Columnas  
    
    columnas = [[4,7,10,13,16],[5,8,11,14,17],[6,9,12,15,18]]
    filas = [[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,19]]
    
    for i,e in enumerate(args):
        
        if e[0] == 0:
            if e[1] == 1 and par == 1:
                ganancia.append(e[2]*2)
            elif e[1] == 2 and par == 0:
                ganancia.append(e[2]*2)
                
                
                
        if e[0] == 1:            
            if e[1] == 1 and par == 1:                
                ganancia.append(e[2]*2)
            elif e[1] == 2 and par == 0:                
                ganancia.append(e[2]*2)   
    
        if e[0]==2:
            
            if resultado in filas[e[1]]:              
                ganancia.append(e[2]*8)
                
        if e[0]==3:     
            if resultado in columnas[e[1]]:    
                ganancia.append(e[2]*4)
                
        if e[0]==4:     
            if resultado == e[1]:    
                ganancia.append(e[2]*35)
    
    

    return sum(ganancia)
################################################################
##################### Calculo total apuestas ###################
def obtener_apuesta(apuesta):
    total = []
    for i,e in enumerate(apuesta):
        total.append(e[2])
    return sum(total)


###############################################################
################## Diferencia ################################
def diferencia(apuesta_total,ganancia_total):
    
    print(f'136 Apuesta_total {apuesta_total}')
    print(f'137 Ganancia Total {ganancia_total}')
    
    label_resultado_text = 'Apostaste: $' + str(apuesta_total)
    
    
    label_resultado = Label(Tablero,text = label_resultado_text) 
    label_resultado.config(font=("Verdana",30))
    label_resultado.place(x=100,y=630)
    
    
    
    label_ganancia = Label(Tablero) 
    
    
    if apuesta_total < ganancia_total:
        label_text = "Ganaste: $" + str(ganancia_total)
        label_ganancia['text'] = label_text
    else:
        label_text = "Perdiste: $" + str(ganancia_total)
        label_ganancia['text'] = label_text
    
    label_ganancia.config(font=("Verdana",30))
     
    label_ganancia.place(x=500,y=630)
###########################################################    
######################## Dados ##############################
def pintar_dado(numero,posicion_x,posicion_y):
    
    global dados
    
    label_dado = Label(Apuesta, image=dados[numero])                      
    label_dado.place(x=posicion_x,y=posicion_y)
############################################################
####################### Tirar Dados ##########################
def tirar_dados():
    
    global cantidad_dinero
    global cantidad_apuesta
    global cantidad_apuesta_sin_modificar
    global apuesta
    
    dado_1 = random.randint(1,6)  
    pintar_dado(dado_1,70,650)

    dado_2 = random.randint(1,6) 
    pintar_dado(dado_2,170,650)
    
    dado_3 = random.randint(1,6)
    pintar_dado(dado_3,270,650)
    
    
    resultado = dado_1 + dado_2 + dado_3
    
    limpiada = Label(Apuesta, width= 100, height=10,  bg ="#fff")
    limpiada.place(x=380,y=650)
    
    
    label_resultado = Label(Apuesta, text=resultado,  bg ="#fff")
    label_resultado.config(font=("Verdana",35))
    label_resultado.place(x=395,y=665)
    
    
    ganancia_total = calculoApuesta(apuesta, resultado)
    apuesta_total = obtener_apuesta(apuesta)
    
    print(f"202 Ganancia total: {ganancia_total}")
    print(f"203 Apuesta total: {apuesta_total}")
    
    diferencia(apuesta_total,ganancia_total)
    
    cantidad_dinero =  cantidad_dinero + ganancia_total
    
    Cantidad_dinero['text'] = cantidad_dinero 
    
    apuesta = []
    
    cantidad_apuesta = 0
    cantidad_apuesta_sin_modificar = 0
    
###################################################################
####################### Poner Fichas ##########################


def poner_fichas(posicion_x,posicion_y):
    global cantidad_dinero
    global cantidad_apuesta
    global apuesta
    
    print(f'222 Cantidad Apuesta: {cantidad_apuesta}')
    
    
    if cantidad_apuesta >= 100:
        fichas = int(cantidad_apuesta/100)       
        labels100 = []
        aumentador = 0
        for i in range(fichas): 
            labels100.append(0) 
            labels100[i] = Label(Tablero, image=img_100)
            ubicacion = posicion_x +aumentador
            labels100[i].place(x=ubicacion,y=posicion_y)
            aumentador += 7
        posicion_x = posicion_x + aumentador
        cantidad_apuesta = cantidad_apuesta - (fichas*100)
        
    if cantidad_apuesta >= 50:
        fichas = int(cantidad_apuesta/50)       
        labels50 = []
        aumentador = 0
        for i in range(fichas):
            labels50.append(0) 
            labels50[i] = Label(Tablero, image=img_50)
            ubicacion = posicion_x +aumentador
            labels50[i].place(x=ubicacion,y=posicion_y)
            aumentador += 7
        posicion_x = posicion_x + aumentador
        cantidad_apuesta = cantidad_apuesta - 50
        
    if cantidad_apuesta >= 25:  
        aumentador = 0
        labels25 = Label(Tablero, image=img_25)   
        ubicacion = posicion_x +aumentador
        labels25.place(x=ubicacion,y=posicion_y)
        aumentador += 7
        posicion_x = posicion_x + aumentador 
        cantidad_apuesta = cantidad_apuesta - 25
        
    if cantidad_apuesta >= 10:
        fichas = int(cantidad_apuesta/10)              
        labels100 = []       
        aumentador = 0    
        for i in range(fichas):       
            labels100.append(0)      
            labels100[i] = Label(Tablero, image=img_10)         
            ubicacion = posicion_x +aumentador            
            labels100[i].place(x=ubicacion,y=posicion_y)
            aumentador += 7
        posicion_x = posicion_x + aumentador
        cantidad_apuesta = cantidad_apuesta - (fichas*10)
        
    if cantidad_apuesta >= 5:  
        aumentador = 0
        labels25 = Label(Tablero, image=img_5)   
        ubicacion = posicion_x +aumentador
        labels25.place(x=ubicacion,y=115)
        aumentador += 7
        posicion_x = posicion_x + aumentador 
        cantidad_apuesta = cantidad_apuesta - 5
        
    if cantidad_apuesta >= 1:
        fichas = cantidad_apuesta           
        labels100 = []       
        aumentador = 0    
        for i in range(fichas):       
            labels100.append(0)      
            labels100[i] = Label(Tablero, image=img)         
            ubicacion = posicion_x +aumentador            
            labels100[i].place(x=ubicacion,y=posicion_y)
            aumentador += 7            
        posicion_x = posicion_x + aumentador
        cantidad_apuesta = cantidad_apuesta - (fichas*1)
        
##############################################################################
############################################################################# APUESTAS
def apostar_al_3():
    global cantidad_apuesta_sin_modificar
    global cantidad_dinero
    global cantidad_apuesta
    global apuesta
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    
    poner_fichas(100,115)
    
    print(f'321 Se aposto {cantidad_apuesta_sin_modificar} al 3')
    apuesta.append([4,3,cantidad_apuesta_sin_modificar])
    cantidad_apuesta_sin_modificar = 0
    
def apostar_al_6():
    global cantidad_apuesta_sin_modificar
    global cantidad_dinero
    global cantidad_apuesta
    global apuesta
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    
    poner_fichas(205,115)
    
    print(f'338 Se aposto {cantidad_apuesta_sin_modificar} al 6')
    apuesta.append([4,6,cantidad_apuesta_sin_modificar])
    cantidad_apuesta_sin_modificar = 0
def apostar_al_9():
    global cantidad_apuesta_sin_modificar
    global cantidad_dinero
    global cantidad_apuesta
    global apuesta
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    
    poner_fichas(300,115)
    
    print(f'354 Se aposto {cantidad_apuesta_sin_modificar} al 9')
    apuesta.append([4,9,cantidad_apuesta_sin_modificar])
    cantidad_apuesta_sin_modificar = 0
def apostar_al_12():
    global cantidad_apuesta_sin_modificar
    global cantidad_dinero
    global cantidad_apuesta
    global apuesta
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    
    poner_fichas(400,115)
    
    print(f'470 Se aposto {cantidad_apuesta_sin_modificar} al 12')
    apuesta.append([4,12,cantidad_apuesta_sin_modificar])
    cantidad_apuesta_sin_modificar = 0
    
def apostar_al_15():
    global cantidad_apuesta_sin_modificar
    global cantidad_dinero
    global cantidad_apuesta
    global apuesta
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    
    poner_fichas(500,115)
    
    print(f'387 Se aposto {cantidad_apuesta_sin_modificar} al 15')
    apuesta.append([4,15,cantidad_apuesta_sin_modificar])
    cantidad_apuesta_sin_modificar = 0
def apostar_al_18():
    global cantidad_apuesta_sin_modificar
    global cantidad_dinero
    global cantidad_apuesta
    global apuesta
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    
    poner_fichas(600,115)
    
    print(f'403 Se aposto {cantidad_apuesta_sin_modificar} al 18')
    apuesta.append([4,18,cantidad_apuesta_sin_modificar])
    cantidad_apuesta_sin_modificar = 0
    
## Segunda Columna

def apostar_al_5():
    global cantidad_apuesta_sin_modificar
    global cantidad_dinero
    global cantidad_apuesta
    global apuesta
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    
    poner_fichas(205,215)
    
    print(f'422 Se aposto {cantidad_apuesta_sin_modificar} al 5')
    apuesta.append([4,5,cantidad_apuesta_sin_modificar])
    cantidad_apuesta_sin_modificar = 0
def apostar_al_8():
    global cantidad_apuesta_sin_modificar
    global cantidad_dinero
    global cantidad_apuesta
    global apuesta
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    
    poner_fichas(300,215)
    
    print(f'438 Se aposto {cantidad_apuesta_sin_modificar} al 8')
    apuesta.append([4,8,cantidad_apuesta_sin_modificar])
    cantidad_apuesta_sin_modificar = 0
def apostar_al_11():
    global cantidad_apuesta_sin_modificar
    global cantidad_dinero
    global cantidad_apuesta
    global apuesta
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    
    poner_fichas(400,215)
    
    print(f'454 Se aposto {cantidad_apuesta_sin_modificar} al 11')
    apuesta.append([4,11,cantidad_apuesta_sin_modificar])
    cantidad_apuesta_sin_modificar = 0
    
def apostar_al_14():
    global cantidad_apuesta_sin_modificar
    global cantidad_dinero
    global cantidad_apuesta
    global apuesta
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    
    poner_fichas(500,215)
    
    print(f'471 Se aposto {cantidad_apuesta_sin_modificar} al 14')
    apuesta.append([4,14,cantidad_apuesta_sin_modificar])
    cantidad_apuesta_sin_modificar = 0
def apostar_al_17():
    global cantidad_apuesta_sin_modificar
    global cantidad_dinero
    global cantidad_apuesta
    global apuesta
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    
    poner_fichas(600,215)
    
    print(f'487 Se aposto {cantidad_apuesta_sin_modificar} al 17')
    apuesta.append([4,17,cantidad_apuesta_sin_modificar])
    cantidad_apuesta_sin_modificar = 0
    
## TERCERA COLUMNA

def apostar_al_4():
    global cantidad_apuesta_sin_modificar
    global cantidad_dinero
    global cantidad_apuesta
    global apuesta
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    
    poner_fichas(205,315)
    
    print(f'506 Se aposto {cantidad_apuesta_sin_modificar} al 4')
    apuesta.append([4,4,cantidad_apuesta_sin_modificar])
    cantidad_apuesta_sin_modificar = 0
def apostar_al_7():
    global cantidad_apuesta_sin_modificar
    global cantidad_dinero
    global cantidad_apuesta
    global apuesta
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    
    poner_fichas(300,315)
    
    print(f'522 Se aposto {cantidad_apuesta_sin_modificar} al 7')
    apuesta.append([4,7,cantidad_apuesta_sin_modificar])
    cantidad_apuesta_sin_modificar = 0
def apostar_al_10():
    global cantidad_apuesta_sin_modificar
    global cantidad_dinero
    global cantidad_apuesta
    global apuesta
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    
    poner_fichas(400,315)
    
    print(f'538 Se aposto {cantidad_apuesta_sin_modificar} al 10')
    apuesta.append([4,10,cantidad_apuesta_sin_modificar])
    cantidad_apuesta_sin_modificar = 0
    
def apostar_al_13():
    global cantidad_apuesta_sin_modificar
    global cantidad_dinero
    global cantidad_apuesta
    global apuesta
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    
    poner_fichas(500,315)
    
    print(f'555 Se aposto {cantidad_apuesta_sin_modificar} al 13')
    apuesta.append([4,13,cantidad_apuesta_sin_modificar])
    cantidad_apuesta_sin_modificar = 0
def apostar_al_16():
    global cantidad_apuesta_sin_modificar
    global cantidad_dinero
    global cantidad_apuesta
    global apuesta
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    
    poner_fichas(600,315)
    
    print(f'571 Se aposto {cantidad_apuesta_sin_modificar} al 16')
    apuesta.append([4,16,cantidad_apuesta_sin_modificar])
    cantidad_apuesta_sin_modificar = 0

        
def apostar_al_inpar():
    
    global cantidad_dinero
    global cantidad_apuesta
    global cantidad_apuesta_sin_modificar
    global apuesta
    
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    poner_fichas(205,515)
    
    
    print(f'590 Se aposto {cantidad_apuesta_sin_modificar} a impar')
    apuesta.append([0,1,cantidad_apuesta_sin_modificar])
    cantidad_apuesta_sin_modificar = 0

def apostar_al_par():
    
    global cantidad_dinero
    global cantidad_apuesta
    global cantidad_apuesta_sin_modificar
    global apuesta
    
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    poner_fichas(295,515)
    print(f'606 Se aposto {cantidad_apuesta_sin_modificar} a par')
    apuesta.append([0,2,cantidad_apuesta_sin_modificar])
    cantidad_apuesta_sin_modificar = 0
    
def apostar_al_rojo():
    
    global cantidad_dinero
    global cantidad_apuesta
    global cantidad_apuesta_sin_modificar
    global apuesta
    
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    poner_fichas(400,515)

    print(f'623 Se aposto {cantidad_apuesta_sin_modificar} a rojo')
    apuesta.append([1,2,cantidad_apuesta_sin_modificar])
    cantidad_apuesta_sin_modificar = 0

def apostar_al_negro():
    
    global cantidad_dinero
    global cantidad_apuesta
    global cantidad_apuesta_sin_modificar
    global apuesta
    
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    poner_fichas(500,515)

    print(f'640 Se aposto {cantidad_apuesta_sin_modificar} a negro')
    apuesta.append([1,1,cantidad_apuesta_sin_modificar])
    
    cantidad_apuesta_sin_modificar = 0
    
def apostar_al_4_to_6():
    global cantidad_dinero
    global cantidad_apuesta
    global cantidad_apuesta_sin_modificar
    global apuesta
    
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    poner_fichas(205,415)

    print(f'657 Se aposto {cantidad_apuesta_sin_modificar} a 4_to_6')
    apuesta.append([2,0,cantidad_apuesta_sin_modificar])
    
    cantidad_apuesta_sin_modificar = 0
    
def apostar_al_7_to_9():
    global cantidad_dinero
    global cantidad_apuesta
    global cantidad_apuesta_sin_modificar
    global apuesta
    
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    poner_fichas(300,415)

    print(f'674 Se aposto {cantidad_apuesta_sin_modificar} a 7_to_9')
    apuesta.append([2,1,cantidad_apuesta_sin_modificar])
    
    cantidad_apuesta_sin_modificar = 0
    
def apostar_al_10_to_12():
    global cantidad_dinero
    global cantidad_apuesta
    global cantidad_apuesta_sin_modificar
    global apuesta
    
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    poner_fichas(400,415)

    print(f'691 Se aposto {cantidad_apuesta_sin_modificar} a 10_to_12')
    apuesta.append([2,2,cantidad_apuesta_sin_modificar])
    
    cantidad_apuesta_sin_modificar = 0

def apostar_al_13_to_15():
    global cantidad_dinero
    global cantidad_apuesta
    global cantidad_apuesta_sin_modificar
    global apuesta
    
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    poner_fichas(500,415)

    print(f'708 Se aposto {cantidad_apuesta_sin_modificar} a 13_to_15')
    apuesta.append([2,3,cantidad_apuesta_sin_modificar])
    
    cantidad_apuesta_sin_modificar = 0
    
def apostar_al_16_to_18():
    global cantidad_dinero
    global cantidad_apuesta
    global cantidad_apuesta_sin_modificar
    global apuesta
    
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    poner_fichas(590,415)

    print(f'725 Se aposto {cantidad_apuesta_sin_modificar} a 16_to_18')
    apuesta.append([2,4,cantidad_apuesta_sin_modificar])
    
    cantidad_apuesta_sin_modificar = 0
    
def apostar_al_colum_3():
    global cantidad_dinero
    global cantidad_apuesta
    global cantidad_apuesta_sin_modificar
    global apuesta
    
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    poner_fichas(700,100)

    print(f'742 Se aposto {cantidad_apuesta_sin_modificar} a la columna 3')
    apuesta.append([3,2,cantidad_apuesta_sin_modificar])
    
    cantidad_apuesta_sin_modificar = 0

def apostar_al_colum_2():
    global cantidad_dinero
    global cantidad_apuesta
    global cantidad_apuesta_sin_modificar
    global apuesta
    
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    poner_fichas(700,200)

    print(f'Se aposto {cantidad_apuesta_sin_modificar} a la columna 2')
    apuesta.append([3,1,cantidad_apuesta_sin_modificar])
    
    cantidad_apuesta_sin_modificar = 0
    
def apostar_al_colum_1():
    global cantidad_dinero
    global cantidad_apuesta
    global cantidad_apuesta_sin_modificar
    global apuesta
    
    
    cantidad_dinero = cantidad_dinero - cantidad_apuesta
    Cantidad_dinero['text'] = cantidad_dinero
    Cantidad_apuesta['text'] = 0
    poner_fichas(700,300)

    print(f'776 Se aposto {cantidad_apuesta_sin_modificar} a la columna 1')
    apuesta.append([3,1,cantidad_apuesta_sin_modificar])
    
    cantidad_apuesta_sin_modificar = 0
    
############################################################################# 
############################################################################# TIRAR 
def tirar():
    
    global cantidad_dinero
    global cantidad_apuesta
    global apuesta
    
    tirar_dados()
############################################################################
############################################################################   LIMPIAR
def limpiar():   
    imagen_tablero = Label(Tablero, image=img_tablero)
    imagen_tablero.place(x=(0),y=0)
    
    limpiada = Label(Apuesta, width= 500, height=100,  bg ="#fff")
    limpiada.place(x=70,y=640)
########################################################
Apuesta = Frame(raiz,width=500,height=1000, bg ="#fff")
Apuesta.place(x=0,y=0) 


label_dinero = Label(Apuesta, text='Dinero:',  bg ="#fff")
label_dinero.config(font=("Verdana",30))
label_dinero.place(x=(20),y=10)

simbolo_dinero = Label(Apuesta, text='$',  bg ="#fff")
simbolo_dinero.config(font=("Verdana",30))
simbolo_dinero.place(x=(250),y=10)

Cantidad_dinero = Label(Apuesta, text='1000',  bg ="#fff")
Cantidad_dinero.config(font=("Verdana",30))
Cantidad_dinero.place(x=(300),y=10)


label_apuesta = Label(Apuesta, text='Apuesta:',  bg ="#fff")
label_apuesta.config(font=("Verdana",30))
label_apuesta.place(x=(20),y=60)

signo = Label(Apuesta, text='$',bg ="#fff")
signo.config(font=("Verdana",30))
signo.place(x=(250),y=60)

Cantidad_apuesta = Label(Apuesta, text= '0',bg ="#fff")
Cantidad_apuesta.config(font=("Verdana",30))
Cantidad_apuesta.place(x=(300),y=60)

##img = img.resize((1000, 250), Image.ANTIALIAS) # Redimension (Alto, Ancho)

img = Image.open('Ficha_1.png')
img = ImageTk.PhotoImage(img)

btn_1= Button(Apuesta,image=img, bg ="#fff",text='+1',command=aumentar_apuesta_1) 
btn_1.place(x=70, y=120) 

img_5 = Image.open('Ficha_5.png')
img_5 = ImageTk.PhotoImage(img_5)

btn_5= Button(Apuesta,image=img_5, bg ="#fff",text='+1',command=aumentar_apuesta_5) 
btn_5.place(x=130, y=120) 

img_10 = Image.open('Ficha_10.png')
img_10 = ImageTk.PhotoImage(img_10)

btn_10= Button(Apuesta,image=img_10, bg ="#fff",text='+1',command=aumentar_apuesta_10) 
btn_10.place(x=190, y=120) 

img_25 = Image.open('Ficha_25.png')
img_25 = ImageTk.PhotoImage(img_25)

btn_25= Button(Apuesta,image=img_25, bg ="#fff",text='+1',command=aumentar_apuesta_25) 
btn_25.place(x=250, y=120) 

img_50 = Image.open('Ficha_50.png')
img_50 = ImageTk.PhotoImage(img_50)

btn_50= Button(Apuesta,image=img_50, bg ="#fff",text='+1',command=aumentar_apuesta_50) 
btn_50.place(x=310, y=120) 

img_100 = Image.open('Ficha_100.png')
img_100 = ImageTk.PhotoImage(img_100)

btn_100= Button(Apuesta,image=img_100, bg ="#fff",text='+1',command=aumentar_apuesta_100) 
btn_100.place(x=370, y=120) 

#cantidad_apuesta = Entry(Apuesta,width=10,justify= RIGHT)
#cantidad_apuesta .config(font=("Verdana",30))
#cantidad_apuesta.place(x=100, y=150)


############### Tablero##############
Tablero = Frame(raiz,width=901,height=800,bg="white")
Tablero.place(x=500,y=0) 

img_tablero= Image.open('Tablero.png')
img_tablero= ImageTk.PhotoImage(img_tablero)

imagen_tablero = Label(Tablero, image=img_tablero)
imagen_tablero.place(x=(0),y=0)

################################# Imagenes Dados ####################

dados = [0,1,2,3,4,5,6]

dados[1] = Image.open('1.png')
dados[1] = ImageTk.PhotoImage(dados[1])

dados[2] = Image.open('2.png')
dados[2] = ImageTk.PhotoImage(dados[2])

dados[3] = Image.open('3.png')
dados[3] = ImageTk.PhotoImage(dados[3])

dados[4] = Image.open('4.png')
dados[4] = ImageTk.PhotoImage(dados[4])

dados[5] = Image.open('5.png')
dados[5] = ImageTk.PhotoImage(dados[5])

dados[6] = Image.open('6.png')
dados[6] = ImageTk.PhotoImage(dados[6])

################################# Botone Apuestas############################

btn_a_3= Button(Apuesta, bg ="#fff",text='3',width=6,height=11,command=apostar_al_3) 
btn_a_3.place(x=17, y=180) 

btn_a_6= Button(Apuesta, bg ="#fff",text='6',width=6,height=3,command=apostar_al_6) 
btn_a_6.place(x=70, y=180) 

btn_a_5= Button(Apuesta, bg ="#fff",text='5',width=6,height=3,command=apostar_al_5) 
btn_a_5.place(x=70, y=240) 

btn_a_4= Button(Apuesta, bg ="#fff",text='4',width=6,height=3,command=apostar_al_4) 
btn_a_4.place(x=70, y=300) 

btn_a_4_6= Button(Apuesta, bg ="#fff",text='4 to 6',width=6,height=3,command=apostar_al_4_to_6) 
btn_a_4_6.place(x=70, y=360) 

btn_a_inpar= Button(Apuesta, bg ="#fff",text='Inpar',width=6,height=3,command=apostar_al_inpar) 
btn_a_inpar.place(x=70, y=420) 



btn_a_9= Button(Apuesta, bg ="#fff",text='9',width=6,height=3,command=apostar_al_9) 
btn_a_9.place(x=130, y=180) 

btn_a_8= Button(Apuesta, bg ="#fff",text='8',width=6,height=3,command=apostar_al_8) 
btn_a_8.place(x=130, y=240) 

btn_a_7= Button(Apuesta, bg ="#fff",text='7',width=6,height=3,command=apostar_al_7) 
btn_a_7.place(x=130, y=300) 

btn_a_7_9= Button(Apuesta, bg ="#fff",text='7 to 9',width=6,height=3,command=apostar_al_7_to_9) 
btn_a_7_9.place(x=130, y=360) 

btn_a_par= Button(Apuesta, bg ="#fff",text='Par',width=6,height=3,command=apostar_al_par) 
btn_a_par.place(x=130, y=420) 



btn_a_12= Button(Apuesta, bg ="#fff",text='12',width=6,height=3,command=apostar_al_12) 
btn_a_12.place(x=190, y=180) 

btn_a_11= Button(Apuesta, bg ="#fff",text='11',width=6,height=3,command=apostar_al_11) 
btn_a_11.place(x=190, y=240) 

btn_a_10= Button(Apuesta, bg ="#fff",text='10',width=6,height=3,command=apostar_al_10) 
btn_a_10.place(x=190, y=300) 

btn_a_4_6= Button(Apuesta, bg ="#fff",text='10 to 12',width=6,height=3,command=apostar_al_10_to_12) 
btn_a_4_6.place(x=190, y=360) 


btn_a_rojo= Button(Apuesta, bg ="#fff",text='Rojo',width=6,height=3,command=apostar_al_rojo) 
btn_a_rojo.place(x=190, y=420) 




btn_a_15= Button(Apuesta, bg ="#fff",text='15',width=6,height=3,command=apostar_al_15) 
btn_a_15.place(x=250, y=180) 

btn_a_14= Button(Apuesta, bg ="#fff",text='14',width=6,height=3,command=apostar_al_14) 
btn_a_14.place(x=250, y=240) 

btn_a_13= Button(Apuesta, bg ="#fff",text='13',width=6,height=3,command=apostar_al_13) 
btn_a_13.place(x=250, y=300) 

btn_a_13_15= Button(Apuesta, bg ="#fff",text='13 to 15',width=6,height=3,command=apostar_al_13_to_15) 
btn_a_13_15.place(x=250, y=360) 

btn_a_negro= Button(Apuesta, bg ="#fff",text='Negro',width=6,height=3,command=apostar_al_negro) 
btn_a_negro.place(x=250, y=420) 



btn_a_18= Button(Apuesta, bg ="#fff",text='18',width=6,height=3,command=apostar_al_18) 
btn_a_18.place(x=310, y=180) 

btn_a_17= Button(Apuesta, bg ="#fff",text='17',width=6,height=3,command=apostar_al_17) 
btn_a_17.place(x=310, y=240) 

btn_a_16= Button(Apuesta, bg ="#fff",text='16',width=6,height=3,command=apostar_al_16) 
btn_a_16.place(x=310, y=300) 

btn_a_16_18= Button(Apuesta, bg ="#fff",text='16 to 18',width=6,height=3,command=apostar_al_16_to_18) 
btn_a_16_18.place(x=310, y=360) 

btn_a_18= Button(Apuesta, bg ="#fff",text='3 colum',width=6,height=3,command=apostar_al_colum_3) 
btn_a_18.place(x=370, y=180) 

btn_a_17= Button(Apuesta, bg ="#fff",text='2 colum',width=6,height=3,command=apostar_al_colum_2) 
btn_a_17.place(x=370, y=240) 

btn_a_16= Button(Apuesta, bg ="#fff",text='1 colum',width=6,height=3,command=apostar_al_colum_1) 
btn_a_16.place(x=370, y=300) 

tirar= Button(Apuesta, bg ="#fff",text='Tirar dados',command= tirar_dados) 
tirar.config(font=("Verdana",20))
tirar.place(x=150, y=480) 

tirar= Button(Apuesta, bg ="#fff",text='Limpiar',command= limpiar) 
tirar.config(font=("Verdana",20))
tirar.place(x=170, y=540) 

raiz.mainloop()