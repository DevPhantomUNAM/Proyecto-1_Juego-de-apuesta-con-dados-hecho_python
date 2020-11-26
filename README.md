# Proyecto 1 Bootcamp 
## Juego de apuesta con dados hecho python

![](https://raw.githubusercontent.com/DevPhantomUNAM/Proyecto-1_Juego-de-apuesta-con-dados-hecho_python/master/assets/Tablero_shadow.png)

Videojuego diseñado para apostar a un formato donde se tiran **3 dados** y la suma del resultado de cada uno, es el valor que se determinar para un tablero donde se hacen las apuestas.

## Contenido 
1. Diseño de material gráfico
    1. Diseño del tablero
    2. Diseño de las fichas para apostar 
    3. Diseño de los 6 dados
2. Librerias


1. Diseño de material gráfico para el videojuego.
2. Librerias

## 1. Diseño de material gráfico

### 1.1 Diseño del tablero

Para el tablero se utiliza la idea del tablero clásico de ruleta y adapatada a los tiros de los dados donde contiene las siguientes posibilidades:
* Apostar del 3 al 18
* Apostar a numeros pares
* Apostar a numeros nones
* Apostar al Rojo
* Apostar al Negro
* Apostar a las columnas con los numeros [6, 9, 12, 15, 18], [5, 8, 11, 14, 17] y [4,7,10,13,16]
* Apostar a las filas con los numeros [4, 5, 6], [7, 8, 9], [10, 11, 12,], [13, 14, 15] y [16, 17, 18]

![](https://raw.githubusercontent.com/DevPhantomUNAM/Proyecto-1_Juego-de-apuesta-con-dados-hecho_python/master/Tablero.png)



### 1.2 Diseño de las fichas para apostar 
Los valores diseñados para este juego son:
* Fichas de 1
* Fichas de 5
* Fichas de 10
* Fichas de 25
* Fichas de 50
* Fichas de 100

![](https://raw.githubusercontent.com/DevPhantomUNAM/Proyecto-1_Juego-de-apuesta-con-dados-hecho_python/master/assets/FIchas_completa.png)

### 1.3 Diseño de los 6 dados

![](https://raw.githubusercontent.com/DevPhantomUNAM/Proyecto-1_Juego-de-apuesta-con-dados-hecho_python/master/assets/Dados%20completa.png)

## 2. Librerias

Las librerias que utilizamos son: 
* Tkinter para la interfaz
* Random para obtener los tiros de dados
* Pil para las imagenes

```
from tkinter import *
from tkinter.filedialog import askopenfile 
from tkinter import PhotoImage
from PIL import Image,ImageTk
import random
```

## 3. Crear Interfaz base
Para la intefaz, debemos crear una instancia para la base, donde regularmente se le nombre root, yo opto por raiz

```
raiz = Tk()
raiz.title('Juego de dados')
raiz.geometry('1401x800') 
```

Y para que nuestra interfaz se muestre, debemos colocar el loop que debe ir al final del programa.

```
raiz.mainloop()
```

Con esto ya podemos correr nuestro programa y nos desplegara una ventada

## 4. Asignar los recursos de imagenes
*Este codigo siempre ira antes de raiz.mainloop()*

Antes de empezar a crear nuestra estructura, estaremos creando las imagenes que estaremos utilizando para nuestros frames, borones y labels.

Para mandar a llamar una imagen, y redimencionarla, utilizaremos ```img = Image.open('Ficha_1')``` y despues ```img = ImageTk.PhotoImage(img)``` y con esto ya contamos con la imagen para la Ficha 1 y haremos el proceso para todas las imagenes.

```
img = Image.open('Ficha_1.png')
img = ImageTk.PhotoImage(img)

img_5 = Image.open('Ficha_5.png')
img_5 = ImageTk.PhotoImage(img_5)

img_10 = Image.open('Ficha_10.png')
img_10 = ImageTk.PhotoImage(img_10)

img_25 = Image.open('Ficha_25.png')
img_25 = ImageTk.PhotoImage(img_25)

img_50 = Image.open('Ficha_50.png')
img_50 = ImageTk.PhotoImage(img_50)

img_100 = Image.open('Ficha_100.png')
img_100 = ImageTk.PhotoImage(img_100)

img_tablero= Image.open('Tablero.png')
img_tablero= ImageTk.PhotoImage(img_tablero)
```

## 5. Crear la estructura
*Este codigo siempre ira antes de raiz.mainloop()*

Para la estructura, debemos definir los lugares donde colocaremos nuestros elementos.


Yo usare dos Frames para esto.

* Frame para las apuestas
* Frame para el tablero

```
Apuesta = Frame(raiz,width=500,height=1000, bg ="#fff")
Apuesta.place(x=0,y=0) 
```

```
Tablero = Frame(raiz,width=901,height=800,bg="white")
Tablero.place(x=500,y=0) 
```

### 5.1 Apuesta

Para el Frame de apuesta, defini cuales son los elementos que deben aparecer al usuario:

* Dinero Total
* Dinero por apostar
* Botones para poner la cantidad a apostar ( Se hizo de esta manera para mantener la experiencia de poner las fichas directo en el tablero)
* Botones para elegir a que apostar que estos se componen (Mencionados en la sección 1.1)
* Un botón para tirar dados
* Un botón para limpiar tablero

#### 5.2 Labels de Dinero y apuesta

Para pintar los 6 labels que usaremos (2 para el texto "Dinero" y "Apuesta", 2 para los signos "$" y los ultimos 2 que seran dinámicos para mostrar sus respectivos estados

Dinero
```
label_dinero = Label(Apuesta, text='Dinero:',  bg ="#fff")
label_dinero.config(font=("Verdana",30))
label_dinero.place(x=(20),y=10)

simbolo_dinero = Label(Apuesta, text='$',  bg ="#fff")
simbolo_dinero.config(font=("Verdana",30))
simbolo_dinero.place(x=(250),y=10)

Cantidad_dinero = Label(Apuesta, text='1000',  bg ="#fff")
Cantidad_dinero.config(font=("Verdana",30))
Cantidad_dinero.place(x=(300),y=10)
```

Apuesta
```
label_apuesta = Label(Apuesta, text='Apuesta:',  bg ="#fff")
label_apuesta.config(font=("Verdana",30))
label_apuesta.place(x=(20),y=60)

signo = Label(Apuesta, text='$',bg ="#fff")
signo.config(font=("Verdana",30))
signo.place(x=(250),y=60)

Cantidad_apuesta = Label(Apuesta, text= '0',bg ="#fff")
Cantidad_apuesta.config(font=("Verdana",30))
Cantidad_apuesta.place(x=(300),y=60)
```

Corre el código y ya te debe aparecer así.

![](https://raw.githubusercontent.com/DevPhantomUNAM/Proyecto-1_Juego-de-apuesta-con-dados-hecho_python/master/assets/Labels_dinero.png)


#### 5.3 Creando instancias de botones para colocar las fichas
*Este codigo siempre ira antes de raiz.mainloop()*

Para crear un botton, utilizamos la instancia **Button** que al igual que label, tambien recibe parametros para su configuración.

```
btn_1= Button(Apuesta,image=img, bg ="#fff",text='+1',command=aumentar_apuesta_1) 
btn_1.place(x=70, y=120) 
```
Este botón tiene una llamada a una función ```command = aumentar_apuesta_1``` por el momento la puedes borrar pero para que puedas visualizar que de esta forma, más adelante estaremos mandando a llamar las funciones correwspondientes a cada botón.

Quedaria así:

```
btn_1= Button(Apuesta,image=img, bg ="#fff",text='+1') 
btn_1.place(x=70, y=120) 
```
Tambien en un parametro **image** le estamos asignando el valor **img** esto viene de la ficha 1 que hicimos en el apartado 4

Así que aplicaremos la misma idea a los botones restantes. Recuerda borrarles su funcion para que no marque error.

```
btn_1= Button(Apuesta,image=img, bg ="#fff",text='+1',command=aumentar_apuesta_1) 
btn_1.place(x=70, y=120) 

btn_5= Button(Apuesta,image=img_5, bg ="#fff",text='+1',command=aumentar_apuesta_5) 
btn_5.place(x=130, y=120) 

btn_10= Button(Apuesta,image=img_10, bg ="#fff",text='+1',command=aumentar_apuesta_10) 
btn_10.place(x=190, y=120) 

btn_25= Button(Apuesta,image=img_25, bg ="#fff",text='+1',command=aumentar_apuesta_25) 
btn_25.place(x=250, y=120) 

btn_50= Button(Apuesta,image=img_50, bg ="#fff",text='+1',command=aumentar_apuesta_50) 
btn_50.place(x=310, y=120) 

btn_100= Button(Apuesta,image=img_100, bg ="#fff",text='+1',command=aumentar_apuesta_100) 
btn_100.place(x=370, y=120) 
```

Ya puedes correr el código despues de haberles quitado el parametro command y el valor y te debe aparecer así:

![](https://github.com/DevPhantomUNAM/Proyecto-1_Juego-de-apuesta-con-dados-hecho_python/blob/master/assets/Botones_apuesta.png?raw=true)

#### 5.4 Botones para apostar

Estos botones se utilizaran a la hora de tu haber apostado una cantidad n de dinero, decidir a que suerte quieres apostar. 

El primer botón que pondremos es el del numero 6 para explicar:

```
btn_a_6= Button(Apuesta, bg ="#fff",text='6',width=6,height=3,command=apostar_al_6) 
btn_a_6.place(x=70, y=180) 
```

Es un botón que le estamos asignando el **texto = 6** y tambien tiene una función llamamada **apostar_al_6** que volvemos a repetir: debe ser borrada para que el programa corra ya que aun no tenemos estas funciones creadas.

Para toda la tabla de apuestas hicimos un botón correspondiente asi que ahora pintaremos cada botón.

```
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
```

Podemos correr el código

![](https://raw.githubusercontent.com/DevPhantomUNAM/Proyecto-1_Juego-de-apuesta-con-dados-hecho_python/master/assets/Apuesta_botones.png)


#### 5.5 Botones para tirar dados y limpiar

Una vez que ya se aposto dinero a una suerte, necesitaremos el botón para aventar los dados.

```
tirar= Button(Apuesta, bg ="#fff",text='Tirar dados',command= tirar_dados) 
tirar.config(font=("Verdana",20))
tirar.place(x=150, y=480) 
```

Tambien un botón para limpiar el tablero 

```
tirar= Button(Apuesta, bg ="#fff",text='Limpiar',command= limpiar) 
tirar.config(font=("Verdana",20))
tirar.place(x=170, y=540) 
```

Le borramos los **command** y corremos:

![](https://raw.githubusercontent.com/DevPhantomUNAM/Proyecto-1_Juego-de-apuesta-con-dados-hecho_python/master/assets/Tirar_dados.png)

## 6 Funcionalidad.

Ahora empezaremos a dar la funcionalidad a cada botón. 

### 6.1 Funcionalidad para botones de fichas

Cada botón de ficha debe de subir el valor de la apuesta y dismunuir el dinero total, así que crearemos variables que estaremos pasando entre funciones.

Definimos estas varaibles despues del apartado 3 en especial la linea ```raiz.geometry('1401x800') ```

```
#Variables 
cantidad_dinero = 1000
cantidad_apuesta = 0
cantidad_apuesta_sin_modificar = 0

apuesta = []
```

y ahora crearemos una funcion para aumentar la apuesta cada que aumentamos una ficha

```
def aumentar_apuesta_1():
    global cantidad_apuesta_sin_modificar
    global cantidad_dinero
    global cantidad_apuesta
    
    if cantidad_apuesta <=(cantidad_dinero-1):       
        cantidad_apuesta = cantidad_apuesta + 1
        cantidad_apuesta_sin_modificar = cantidad_apuesta_sin_modificar + 1
        Cantidad_apuesta['text'] = cantidad_apuesta
```

Estamos utilizando 2 variables que cambian ```cantidad_apuesta``` y ```cantidad_apuesta_sin_modificar``` que se utilizaran para el label Apuesta y el cálculo de fichas a poner. Tambien evaluaremos que si aun podemos apostar siempre y cuando no exeda el dinero total.

Y crearemos las funciones para las funcionales Ficha 1, 5, 10, 25, 50 y 100

```
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
```

Recuerdas que borramos las funciones de los botones, en la sección 5.1.2 puedes volver a copiarlos y ahora correr el programa y veras que aumenta nuestra apuesta.

### 6.2 Funcionalidad para botones de fichas

Usaremos el ejemplo del botón "Apostar a para" para exlicar su funcionailidad.

El botón manda a llamar la función ```apostar_al_par()```

```
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
 ```
1. Lo primero que hacemos es restarle al dinero total, el dinero de la apuesta y resetear el dinero de la apuesta
2. Mandamos a llamar la función ```poner_fichas(x,y)``` y lo que hace la funcion poner_fichas es obtener la posición de donde se deben poner las fichas apostadas asi que veremos la función poner_fichas
 ```
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
 ```

Y la ponemos antes de ```Apostar_al_par()```. Lo que hace es hacer el cálculo de la apuesta empezando por la más grande de 100 y difividarlas en fichas correspondientes y se pongan en el tablero.

Crear un labels100 y le colocan la imagen de la ficha correspondiente y la posición dada por los aprametros.

Regresnado a la función **apostar_al_par()** tenemos la instrucción ```apuesta.append([0,2,cantidad_apuesta_sin_modificar])``` 

Lo que hicimos fue crear una lista *Apuesta* donde se metieran todas las apuestas que se hacian, dando la posibilidad de apostar a más opciones como en la ruleta.

Nuestro formato es el sigueinte:

La apuesta consiste en una lista de 3 elementos [v1,v2,v3] donde:

V1: Es el tipo de apuesta:

  0: A Pares y Nones
  
  1: A color
  
  2: A fila
  
  3: A Columna
  
  4: A Numero
  
V2: Modo de apuesta dependiendo de V1

  0:  1: Al inpar
  
  0:  2: Al par
  
  
  1:  1: A color Negro
  
  1:  2: A color Rojo
  
  
  2:  0: Columnas correspondientes al aparatodo 1.1
  
  2:  1: Columnas correspondientes al aparatodo 1.1
  
  2:  2: Columnas correspondientes al aparatodo 1.1
  
  
  3:  0: Filas correspondientes al apartado 1.1
  
  3:  1: Filas correspondientes al apartado 1.1
  
  3:  2: Filas correspondientes al apartado 1.1
  
  3:  3: Filas correspondientes al apartado 1.1
  
  3:  4: Filas correspondientes al apartado 1.1
  
  4:  1: Apuesta correspondiente a Numero 1
  ...

V3: El valor de apuesta que se le hacia

  [0,1,500]  Se hacia una apuesta a Pares y Nones, apostandole al Inpar y apostando 500
  
Así que se sumaran cada una de las apuestas en la lista

Example
```
Apuesta = [[0,2,300],[2.2.300]]
```

Y por ultimo se resetea el contador de apuestas.

**Todos los botones tienen el mismo formato**

Estos son las funciones para todos los botones:

```
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
```
