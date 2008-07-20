# Clase para rumbo
import math

import conf

class Rumbo:
    def __init__(self, valor=0):
        self.valor = valor

    def x(self):
        return math.sin(math.radians(self.valor))

    def y(self):
        return math.cos(math.radians(self.valor))

    def validar(self):
        if self.valor > conf.MAX_S:
            self.valor = conf.MAX_S + 1
        if self.valor < conf.MIN_S:
            self.valor = conf.MAX_S - self.valor - 1

    def __cmp__(self, rumbo):
        if self.valor == rumbo.valor:
            return 0
        elif self.valor > rumbo.valor:
            return 1
        elif self.valor < rumbo.valor:
            return -1

    def __add__(self, rumbo):
        if isinstance(rumbo, type(self)):
            rumbo = rumbo.valor
        if self.valor + rumbo > conf.MAX_S:
            rumbo = (conf.MAX_S + rumbo) - ( self.valor + 1 )
        elif self.valor + rumbo < conf.MIN_S:
            rumbo = conf.MAX_S + rumbo + 1
        else:
            rumbo = self.valor + rumbo
        return Rumbo(rumbo)

    def __sub__(self, rumbo):
        if isinstance(rumbo, type(self)):
            rumbo = rumbo.valor
        if self.valor - rumbo < conf.MIN_S:
            rumbo = conf.MAX_S - (rumbo - self.valor) + 1
        else:
            rumbo = self.valor - rumbo
        return Rumbo(rumbo)

    def __str__(self):
        return str(self.valor)
