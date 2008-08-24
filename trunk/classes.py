# Classes definition
# Copyright (C) 2008 Alejandro Varas <alej0varas@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor Boston, MA 02110,  USA
# or see <http://www.gnu.org/licenses/>

#python
import math
from random import randint

#other
import pygame
#import numpy

#waratsea
from conf import *
from data import *


class Escenario:
    def __init__(self, juego, imagen):
        MIN_A = 0
        MAX_A = 2
        MIN_V = 0
        MAX_V = 5
        self.juego = juego
        # pygame
        self.imagen = imagen
        self.imagen_prev = self.imagen
        self.juego.screen.blit(self.imagen, self.imagen.get_rect())
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
        #return '\n'.join( i.__str__() for i in self.naves)
        return ''

    def juega(self):
        for nave in self.naves:
            nave.jugar()
            #print nave
#        viento = []

    def crear_naves(self, naves):
        self.naves = [Nave(self, i, self.juego.cargar_imagen('nave')) for i in naves]

    def dibuja(self):
        for nave in self.naves:
            #pygame.draw.rect(self.juego.screen, pygame.color.Color("white"), rect) #TODO color
            rect = nave.imagen.get_rect()
            rect_borrar = nave.imagen.get_rect(center=(nave.x, nave.y))
            pos = (nave.x - rect.centerx, nave.y - rect.centery)
            self.juego.screen.blit(self.imagen_prev, nave.pos_ultima, rect_borrar)
            self.juego.screen.blit(nave.imagen, pos, rect)
            nave.set_pos_ultima()
            self.juego.escribir(str(nave))


class Nave:
    def __init__(self, escenario, tipo, imagen):
        tipo = naves[tipo]
        self.imagen = imagen
        self.imagen_ori = self.imagen
        self.rumbo = Rumbo(0) # donde debe ir
        self.rumbo_verdadero = Rumbo(self.rumbo.valor) #donde va la nave
        #self.rumbo_relativo = 0 #donde apunta la nave
        self.timones = [ Timon(i) for i in tipo['timones'] ]
        self.timonel = Timonel(self)
        #self.tipo = naves[tipo]
        #self.escenario = escenario
        self.x = MAX_X/2
        self.xc = 0.0
        self.y = MAX_Y/2
        self.yc = 0.0
        self.set_pos_ultima()
        self.velocidad = 1.0
        self.vel_max = tipo['vel_max']
        #self.palos = []
        #self.construir_palos()
        self.rvc = 0.0 # rumbo verdadero contador
        self.simbolos = ('/\\', '->', '\\/', '<-')
        self.simbolo = 'X'


    def __str__(self):
        #       X     Y   sentido  velocidad
        return '(%d, %d)|%d|%d|->%f (%s)' % (self.x, self.y, self.rumbo_verdadero.valor, self.rumbo.valor, self.velocidad, self.simbolo)

    def jugar(self):
        self.acelerar()
        self.avanzar()
        self.girar()
        self.timonel.jugar()

    def acelerar(self):
        incremento = 0
        pos = self.y*(MAX_Y-1)+self.x-1
        #incremento = self.escenario.corriente[pos][0]*self.escenario.corriente[pos][1]
        #incremento += self.calcular_F_velas()
        if self.velocidad + incremento < 0 or self.velocidad + incremento > self.vel_max:
            incremento = 0
        self.velocidad += incremento

    def avanzar(self):
        self.xc += self.rumbo_verdadero.x()
        if abs(self.xc) > 1:
            delta = abs(self.xc) - abs(int(self.xc))
            self.x += int(self.xc)*self.velocidad
            self.xc = delta
        if self.x > MAX_X:
            self.x = MAX_X-1
        if self.x < 0:
            self.x = 0

        self.yc -= self.rumbo_verdadero.y()
        delta = abs(self.yc) - abs(int(self.yc))
        if abs(self.yc) > 1:
            self.y += int(self.yc)*self.velocidad
            self.yc = delta
        if self.y > MAX_Y:
            self.y = MAX_Y-1
        if self.y < 0:
            self.y = 0

    def girar(self):
        """
        #self.sentido += self.escenario.viento[self.y*(MAX_Y-1)+self.x-1]
        #self.rumbo += 1
        """
        self.rvc += self.timones[0].posicion/28.0 # TODO
        # suma una y conserva la fraccion
        #print self.rvc, int(self.rvc)
        if abs(self.rvc) > 1:
            self.rumbo_verdadero += int(self.rvc)
            self.rvc -= int(self.rvc)
            #print self.rvc
        #
        sentido = self.rumbo_verdadero.valor + 45
        if sentido > MAX_S:
            sentido -= MAX_S
        self.simbolo = self.simbolos[sentido/90]
        self.imagen = pygame.transform.rotate(self.imagen_ori, -self.rumbo_verdadero.valor)#TODO: girar imagen

    def calcular_F_velas(self):
        return randint(-3, 2)

    def construir_palos(self):
        for tipo in self.tipo['palos']:
            self.palos.append(Palo(tipo))

    def de(self):
        self.rumbo += 1

    def iz(self):
        self.rumbo += -1

    def set_pos_ultima(self):
        self.pos_ultima = self.imagen.get_rect(center=(self.x, self.y))


class Palo:
    def __init__(self, tipo):
        self.tipo = palos[tipo]
        self.velas = [ Vela(tipo) for tipo in self.tipo['velas'] ]


class Rumbo:
    def __init__(self, valor=0):
        self.valor = valor

    def x(self):
        return math.sin(math.radians(self.valor))

    def y(self):
        return math.cos(math.radians(self.valor))

    def validar(self):
        if self.valor > MAX_S:
            self.valor = MAX_S + 1
        if self.valor < MIN_S:
            self.valor = MAX_S - self.valor - 1

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
        if self.valor + rumbo > MAX_S:
            rumbo = (MAX_S + rumbo) - ( self.valor + 1 )
        elif self.valor + rumbo < MIN_S:
            rumbo = MAX_S + rumbo + 1
        else:
            rumbo = self.valor + rumbo
        return Rumbo(rumbo)

    def __sub__(self, rumbo):
        if isinstance(rumbo, type(self)):
            rumbo = rumbo.valor
        if self.valor - rumbo < MIN_S:
            rumbo = MAX_S - (rumbo - self.valor) + 1
        else:
            rumbo = self.valor - rumbo
        return Rumbo(rumbo)

    def __str__(self):
        return str(self.valor)


class Timon:
    def __init__(self, tipo):
        tipo = timones[tipo]
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


class Timonel:
    def __init__(self, nave):
        self.habilidad = 0.5
        self.nave = nave

    def jugar(self):
        self.timonear()

    def timonear(self):
        dr = self.nave.rumbo_verdadero.valor - self.nave.rumbo.valor
        if dr:
            cant = 1
            lado = ''
            if self.nave.rumbo_verdadero.valor < 180:
                if self.nave.rumbo.valor < 180:
                    if dr > 0:
                        lado = 'iz'
                    else:
                        lado = 'de'
                else:
                    if abs(dr) < 180:
                        lado = 'de'
                    else:
                        lado = 'iz'
            else:
                if self.nave.rumbo.valor > 180:
                    if dr > 0:
                        lado = 'iz'
                    else:
                        lado = 'de'
                else:
                    if dr > 180:
                        lado = 'de'
                    else:
                        lado = 'iz'
            if lado == 'de':
                [ i.de(cant) for i in self.nave.timones ]
            else:
                [ i.iz(cant) for i in self.nave.timones ]



class Vela:
    def __init__(self, tipo):
        self.tipo = velas[tipo]
        self.alto = self.tipo["alto"]
        self.ancho = self.tipo["ancho"]
        #self.formula =tipo.formula
