from objeto import Objeto
from random import randint

class Ball(Objeto):
	def __init__(self, ambiente, screen, largura, altura, colisao, sprite_boneco):
		posicao = [0,0]
		Objeto.__init__(self, ambiente, "circle.png", [0,0], posicao)
		self.screen = screen
		self.colisao = colisao
		self.sprite_boneco = sprite_boneco
		self.largura, self.altura = largura, altura
		self.time = 500
		self.count = self.time 
		self.score = 0
		
	def sortear_posicao(self):
		if self.count != self.time:
			self.count = (self.count+1)%(self.time+1)
		else:
			x = randint(0, self.largura)
			y = randint(0, self.altura)
			self.posicao = [x,y]
			self.rect.x, self.rect.y = self.posicao
			if self.amb.sprite.spritecollide(self, self.colisao, False) == []:
				self.count = 0
		self.verificar_colisao()

	def verificar_colisao(self):
		if self.amb.sprite.collide_rect(self, self.sprite_boneco) == 1:
			self.count = self.time
			self.score += 10
			print("Score: "+ str(self.score))

	def desenhar_ball(self):
		self.screen.blit(self.image, self.posicao)