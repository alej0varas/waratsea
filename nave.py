#python
import math
import random

#other
#import numpy

#waratsea
import conf
from naves import tipos_nave
from palo import Palo
from rumbo import Rumbo
from timon import Timon
from timonel import Timonel


class Nave:
    def __init__(self, escenario, tipo):
        self.rumbo = Rumbo(0) # donde debe ir
        self.rumbo_verdadero = Rumbo(self.rumbo.valor) #donde va la nave
        #self.rumbo_relativo = 0 #donde apunta la nave
        self.timon = Timon(tipos_nave[tipo]['timon'])
        self.timonel = Timonel(self)
        #self.tipo = tipos_nave[tipo]
        #self.escenario = escenario
        self.x = conf.MAX_X/2
        self.xc = 0.0
        self.y = conf.MAX_Y/2
        self.yc = 0.0
        self.velocidad = 1.0
        #self.palos = []
        #self.construir_palos()
        self.rvc = 0.0
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
        pos = self.y*(conf.MAX_Y-1)+self.x-1
        #incremento = self.escenario.corriente[pos][0]*self.escenario.corriente[pos][1]
        incremento += self.calcular_F_velas()
        if self.velocidad + incremento < 0:
            incremento = 0
        self.velocidad += incremento

    def avanzar(self):
        self.xc += self.rumbo_verdadero.x()
        if abs(self.xc) > 1:
            self.x += int(self.xc)*self.velocidad
            self.xc = 0.0
        if self.x > conf.MAX_X:
            self.x = conf.MAX_X-1
        if self.x < 0:
            self.x = 0

        self.yc -= self.rumbo_verdadero.y()
        if abs(self.yc) > 1:
            self.y += int(self.yc)*self.velocidad
            self.yc = 0.0
        if self.y > conf.MAX_Y:
            self.y = conf.MAX_Y-1
        if self.y < 0:
            self.y = 0

    def girar(self):
        """
        #self.sentido += self.escenario.viento[self.y*(MAX_Y-1)+self.x-1]
        #self.rumbo += 1
        """
        self.rvc += self.timon.posicion/28.0
        # suma una y conserva la fraccion
        #print self.rvc, int(self.rvc)
        if abs(self.rvc) > 1:
            self.rumbo_verdadero += int(self.rvc)
            self.rvc -= int(self.rvc)
            #print self.rvc
        #
        sentido = self.rumbo_verdadero.valor + 45
        if sentido > conf.MAX_S:
            sentido -= conf.MAX_S
        self.simbolo = self.simbolos[sentido/90]

    def calcular_F_velas(self):
        return random.randint(-3, 2)

    def construir_palos(self):
        for tipo in self.tipo['palos']:
            self.palos.append(Palo(tipo))

    def de(self):
        self.rumbo += 1

    def iz(self):
        self.rumbo += -1
