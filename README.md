# Proyecto 1 Bootcamp 
## Juego de apuesta con dados hecho python

![](https://raw.githubusercontent.com/DevPhantomUNAM/Proyecto-1_Juego-de-apuesta-con-dados-hecho_python/master/Tablero_shadow.png)

Videojuego diseñado para apostar a un formato donde se tiran **3 dados** y la suma del resultado de cada uno, es el valor que se determinar para un tablero donde se hacen las apuestas.

## Contenido 

1. Diseño de material gráfico para el videojuego.
2. Librerias

## 1. Diseño de material gráfico

### 1. Diseño del tablero

Para el tablero se utiliza la idea del tablero clásico de ruleta y adapatada a los tiros de los dados donde contiene las siguientes posibilidades:
* Apostar del 3 al 18
* Apostar a numeros pares
* Apostar a numeros nones
* Apostar al Rojo
* Apostar al Negro
* Apostar a las columnas con los numeros [6, 9, 12, 15, 18], [5, 8, 11, 14, 17] y [4,7,10,13,16]
* Apostar a las filas con los numeros [4, 5, 6], [7, 8, 9], [10, 11, 12,], [13, 14, 15] y [16, 17, 18]

![](https://raw.githubusercontent.com/DevPhantomUNAM/Proyecto-1_Juego-de-apuesta-con-dados-hecho_python/master/Tablero.png)



### 2. Diseño de las fichas para apostar 
Los valores diseñados para este juego son:
* Fichas de 1
* Fichas de 5
* Fichas de 10
* Fichas de 25
* Fichas de 50
* Fichas de 100

![](https://raw.githubusercontent.com/DevPhantomUNAM/Proyecto-1_Juego-de-apuesta-con-dados-hecho_python/master/FIchas_completa.png)

### 3. Diseño de los 6 dados



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

y debemos agregar al final de nuestro codigo. SIEMPRE DEBE ESTAR AL FINAL

```
raiz.mainloop()
```

Con esto ya podemos correr nuestro programa y nos despelgara una ventada

## 4. Crear la estructura

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

