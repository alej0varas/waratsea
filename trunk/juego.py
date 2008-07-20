# waratsea
import time
import pygame

from escenario import Escenario
from conf import *
from comandos import comandos
from rumbo import Rumbo


class Juego:
    def __init__(self):
        self.jugar = True

    def main(self):
        # Inicio pygame
        pygame.init()
        pygame.event.set_blocked(pygame.MOUSEMOTION) 
        pygame.key.set_repeat(1, 5)    
        screen = pygame.display.set_mode((MAX_X, MAX_Y))
        # Fin pygame
        naves = ('carak',)
        escenario = Escenario(screen, naves)
        comando = ''
        comandando = False
        while self.jugar:
            event = pygame.event.poll()
            if event.type == pygame.KEYDOWN:
                if comandando:
                    if event.key == pygame.K_RETURN:
                        if comando[0] == 'a':
                            valor = int(comando.split()[1])
                            escenario.naves[0].rumbo = Rumbo(valor)
                            comando = ''
                            comandando = False
                        #ejecutar(comando)
                        #print "ENTER"
                    else:
                        comando += chr(event.key)
                        #print comando
                else:
                    if event.key == pygame.K_LEFT:
                        escenario.naves[0].iz()
                    elif event.key == pygame.K_RIGHT:
                        escenario.naves[0].de()
                    elif event.key == pygame.K_c:
                        comandando = True
                if event.key == pygame.K_ESCAPE:
                    exit()

            escenario.juega()
            escenario.dibuja()
            #print escenario
            time.sleep(0.1)
            pygame.display.flip()
    
    #def ejecutar(comando):
    #    print "ejecutando " + comando
    #    comandos[comando]()