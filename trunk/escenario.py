from conf import *
from random import randint
from nave import Nave
import pygame

class Escenario:
    def __init__(self, screen, naves):
        MIN_A = 0
        MAX_A = 2
        MIN_V = 0
        MAX_V = 5
        self.screen = screen
        #self.corriente = [(randint(MIN_A, MAX_A), randint(0,359)) for i in range(0, MAX_X*MAX_Y)]
        #self.viento = [(randint(MIN_V, MAX_V), randint(0,359)) for i in range(0, MAX_X*MAX_Y)]
        self.crear_naves(naves)

    def __str__(self):
        """
        corriente = ''
        formato_x = ' '
        formato_y = '\n'
        simbolo_s = '-'
        for i in range(1,len(self.corriente)+1):
            for nave in self.naves:
                if nave.x == (i % MAX_X) and nave.y == (i/MAX_Y):
                    simbolo = '%s%s' % (formato_x, nave.simbolo)
                else:
##                    simbol = '%3d' % self.corriente[i-1]#'o'
##                    simbol = '%3d' % self.viento[i-1]#'o'
                    simbolo = '%s%s' % (formato_x, simbolo_s)
            if not i % MAX_X and i != 0:
                simbolo += '%s' % formato_y
            corriente += simbolo
        corriente += '\n%s' % ' '.join([str(i) for i in self.naves])
        return corriente
        """
        for nave in self.naves:
            print nave
        return ''

    def juega(self):
        for nave in self.naves:
            nave.jugar()
            print nave
#        viento = []

    def crear_naves(self, naves):
        self.naves = [Nave(self, i) for i in naves]

    def dibuja(self):
        for nave in self.naves:
            rect = (nave.x, nave.y, 2, 2)
            pygame.draw.rect(self.screen, pygame.color.Color("white"), rect)
