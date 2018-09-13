import pygame

class Objeto(pygame.sprite.Sprite):
    def __init__(self, ambiente, img, velocidade, posicao):
        super().__init__()
        self.amb = ambiente
        self.imagem = img
        self.velocidade = velocidade
        self.posicao = posicao
        self.definir_sprites(img)

    def definir_sprites(self, imagem):
        self.image = self.amb.image.load(imagem)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.posicao

    def get_size(self):
        return(self.image.get_size())

    def get_posicao(self):
        return self.posicao

    def retornar_velocidade(self):
        return self.velocidade

    def retornar_imagem(self):
        return self.image