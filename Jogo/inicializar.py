import pygame
from ball import Ball
from mapa import Mapa
from random import randint
from objeto import Objeto
from personagem import Personagem

class Inicializar(object):
    def __init__(self, largura, altura):
        self.largura, self.altura = largura, altura
        self.amb = pygame
        self.fundo = Mapa(self.amb)
        self.colisao = self.fundo.return_colisao()
        self.inicio()
        self.jogador = Personagem(self.amb, self.screen, "Riven.png", [2,2], [80,100], self.colisao)
        self.ball = Ball(self.amb, self.screen, self.largura, self.altura, self.colisao, self.jogador)
        self.loop()
        
    def inicio(self):
        self.amb.init()
        self.screen = self.amb.display.set_mode((self.largura, self.altura))
        self.done = False
    
    def loop(self):
        while not self.done:
            for event in self.amb.event.get():
                    if event.type == self.amb.QUIT:
                            self.done = True 
            
            self.atualizar_tela()    
            self.amb.display.flip()
    
    def atualizar_tela(self):
        self.screen.fill((0,0,0))
        self.fundo.mapa.draw(self.screen)
        self.jogador.desenhar_sprites()
        self.ball.sortear_posicao()
        self.ball.desenhar_ball()


if __name__ == "__main__":        
    a = Inicializar(960, 640)
