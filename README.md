# Proyecto 1 Bootcamp 
## Juego de apuesta con dados hecho python

![](https://raw.githubusercontent.com/DevPhantomUNAM/Proyecto-1_Juego-de-apuesta-con-dados-hecho_python/master/assets/Tablero_shadow.png)

Videojuego diseñado para apostar a un formato donde se tiran **3 dados** y la suma del resultado de cada uno, es el valor que se determinar para un tablero donde se hacen las apuestas.

## Contenido 

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
* Un boton para tirar dados
* Un boton para limpiar tablero

#### 5.1.1 Labels de Dinero y apuesta

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


#### 5.1.2 Creando instancias de botones para colocar las fichas
*Este codigo siempre ira antes de raiz.mainloop()*

Para crear un botton, utilizamos la instancia **Button** que al igual que label, tambien recibe parametros para su configuración.

```
btn_1= Button(Apuesta,image=img, bg ="#fff",text='+1',command=aumentar_apuesta_1) 
btn_1.place(x=70, y=120) 
```
Este boton tiene una llamada a una función ```command = aumentar_apuesta_1``` por el momento la puedes borrar pero para que puedas visualizar que de esta forma, más adelante estaremos mandando a llamar las funciones correwspondientes a cada boton.

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

#### 5.1.3 Botones para apostar

Estos botones se utilizaran a la hora de tu haber apostado una cantidad n de dinero, decidir a que suerte quieres apostar. 

El primer boton que pondremos es el del numero 6 para explicar:

```
btn_a_6= Button(Apuesta, bg ="#fff",text='6',width=6,height=3,command=apostar_al_6) 
btn_a_6.place(x=70, y=180) 
```

Es un boton que le estamos asignando el **texto = 6** y tambien tiene una funcion llamamada **apostar_al_6** que volvemos a repetir debe ser borrada para que el programa corra ya que aun no tenemos estas funciones creadas.

Para toda la tabla de apuestas hicimos un boton correspondiente asi que ahora pintaremos cada boton.

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
