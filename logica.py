
class Funcionalidad():
    def __init__(self,cantidad_dinero = 1000, cantidad_apuesta = 0,cantidad_apuesta_sin_modificar=0,apuesta=0):
        
        self.cantidad_dinero = cantidad_dinero
        self.cantidad_apuesta = cantidad_apuesta
        self.cantidad_apuesta_sin_modificar = cantidad_apuesta_sin_modificar
        self.apuesta = apuesta
        
        
        

    def aumentar_apuesta_1(self):   
        
        if self.cantidad_apuesta <=(self.cantidad_dinero-1):  
            print("Holi")     
            self.cantidad_apuesta = self.cantidad_apuesta + 1
            self.cantidad_apuesta_sin_modificar = self.cantidad_apuesta_sin_modificar + 1
        return self.cantidad_apuesta
            
            

    