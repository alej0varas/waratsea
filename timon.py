# Clase Timon

class Timon:
    def __init__(self, tipo):
        self.posicion = 0
        self.max = tipo['max']
        self.min = tipo['max']*-1
        self.largo = tipo['largo']
        self.alto = tipo['alto']

    def de(self, cant):
        if self.posicion + cant < self.max:
            self.posicion += cant
        else:
            self.posicion = self.max
        #print self.posicion

    def iz(self, cant):
        if self.posicion - cant > self.min:
            self.posicion -= cant
        else:
            self.posicion = self.min
        #print self.posicion

    def a(self, posicion=0):
        if posicion > self.min and posicion < self.max:
            self.posicion = posicion
