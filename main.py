
def main():

    raiz = Tk()
    raiz.title('Juego de dados')
    raiz.geometry('1401x800') 
    
    prueba = Tablero(raiz)   
    
    prueba.crear_tableros()
   
    raiz.mainloop()

if __name__ == "__main__":

    
    from tkinter import *
    from tkinter.filedialog import askopenfile 
    from tkinter import PhotoImage
    from PIL import Image,ImageTk
    import random
    from interfaz import Tablero

    main()