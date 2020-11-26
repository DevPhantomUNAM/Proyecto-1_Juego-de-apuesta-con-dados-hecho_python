# Proyecto 1 Bootcamp 
## Juego de apuesta con dados hecho python

![](https://raw.githubusercontent.com/DevPhantomUNAM/Proyecto-1_Juego-de-apuesta-con-dados-hecho_python/master/Tablero_shadow.png)

Videojuego diseñado para apostar a un formato donde se tiran **3 dados** y la suma del resultado de cada uno, es el valor que se determinar para un tablero donde se hacen las apuestas.

## Contenido 

1. Diseño de material gráfico para el videojuego.
2. Librerias

## 1. Diseño de material gráfico

1. Creacion del tablero

Para el tablero se utiliza la idea del tablero clásico de ruleta y adapatada a los tiros de los dados donde contiene las siguientes posibilidades:
* Apostar del 3 al 18
* Apostar a numeros pares
* Apostar a numeros nones
* Apostar al Rojo
* Apostar al Negro
* Apostar a las columnas con los numeros [6, 9, 12, 15, 18], [5, 8, 11, 14, 17] y [4,7,10,13,16]
* Apostar a las filas con los numeros [4, 5, 6], [7, 8, 9], [10, 11, 12,], [13, 14, 15] y [16, 17, 18]
![](https://raw.githubusercontent.com/DevPhantomUNAM/Proyecto-1_Juego-de-apuesta-con-dados-hecho_python/master/Tablero.png)



2. Creación de las fichas para apostar 
Los valores diseñados para este juego son:
* Fichas de 1
* Fichas de 5
* Fichas de 10
* Fichas de 25
* Fichas de 50
* Fichas de 100
![](https://raw.githubusercontent.com/DevPhantomUNAM/Proyecto-1_Juego-de-apuesta-con-dados-hecho_python/master/FIchas_completa.png)

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
