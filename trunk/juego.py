# waratsea it is a naval strategy game
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
import time
import pygame

from classes import *
from conf import *
#from comandos import comandos

class Juego:
    def __init__(self):
        self.jugar = True
        # Inicio pygame
        pygame.init()
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        pygame.key.set_repeat(1, 5)
        self.screen = pygame.display.set_mode((MAX_X, MAX_Y))
        self.font = pygame.font.SysFont("vera", T_LETRA)
        # Fin pygame
        self.naves = ('carak',)
        imagen = self.cargar_imagen('fondo')
        self.escenario = Escenario(self, imagen)
        self.comando = ''
        self.comandando = False

    def main(self):
        while self.jugar:
            event = pygame.event.poll()
            if self.comando:
                self.escribir(self.comando, 0, 50, relleno=20)
            if event.type == pygame.KEYDOWN:
                if self.comandando:
                    if event.key == pygame.K_RETURN:
                        self.escribir(' '*50, 0, 50, 'black') # borra comando
                        self.comando = self.comando.strip()
                        if self.comando[0] == 'a':
                            valor = int(self.comando.split()[1])
                            self.escenario.naves[0].rumbo = Rumbo(valor)
                            self.comando = ''
                            self.comandando = False
                        #ejecutar(comando)
                        #print "ENTER"
                    else:
                        #self.escribir(self.comando, 0, 50)
                        if event.key == pygame.K_BACKSPACE:
                            self.comando = self.comando[:-1]
                        elif event.key == pygame.K_ESCAPE:
                            self.comando = ''
                            self.comandando = False
                        else:
                            try:
                                self.comando += chr(event.key)
                            except ValueError:
                               pass
                else:
                    if event.key == pygame.K_LEFT:
                        self.escenario.naves[0].iz()
                    elif event.key == pygame.K_RIGHT:
                        self.escenario.naves[0].de()
                    elif event.key == pygame.K_c:
                        self.comandando = True
                if event.key == pygame.K_ESCAPE:
                    exit()

            self.escenario.juega()
            self.escenario.dibuja()
            #print escenario
            time.sleep(0.1)
            pygame.display.flip()

    def cargar_imagen(self, archivo, directorio='data', formato='png'):
        #directorio = os.path(directorio) #TODO
        #if not self.formato in archivo:
        #    formato = self.formato
        imagen = pygame.Surface.convert_alpha(pygame.image.load(directorio+'/'+archivo+'.'+formato))
        return imagen

    def escribir(self, text, x=0, y=0, color='white', relleno=5):
        text = '%s' % (text) + ' '*relleno
        font_s = self.font.render(text, 0, pygame.color.Color(color))
        rect = font_s.get_rect()
        self.screen.blit(self.escenario.imagen, (x, y), rect) #Borra anterior
        self.screen.blit(font_s, (x, y), rect)

    #def ejecutar(comando):
    #    print "ejecutando " + comando
    #    comandos[comando]()
