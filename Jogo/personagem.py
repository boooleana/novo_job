from objeto import Objeto

class Personagem(Objeto):
	def __init__(self, ambiente, screen, img, velocidade, posicao, colisao):
		Objeto.__init__(self, ambiente, img, velocidade, posicao)

		self.screen = screen
		self.up, self.down, self.left, self.right = self.amb.K_UP, self.amb.K_DOWN, self.amb.K_LEFT, self.amb.K_RIGHT
		self.colisao = colisao
		self.posicao_plot = self.posicao[:]
		self.indice = 0
		self.image = self.lista_sprites[0][0] 
		self.fpp = 0.1 #frame por pixel
				
	def definir_sprites(self, img):
		spritesheet = self.amb.image.load(img)
		self.size = spritesheet.get_size()
		
		self.lista_sprites = [[], [], [], []]  #[0 - front, 1 - left, 2 - right, 3 - back]
		for j in range(1, 5):
			for i in range(1, 4):
				x_min = (self.size[0]/3)*(i-1)
				y_min = (self.size[1]/4)*(j-1)
				x_max = (self.size[0]/3)*i
				y_max = (self.size[1]/4)*j
				dimensoes = self.amb.Rect(x_min, y_min, x_max-x_min, y_max-y_min)
				self.lista_sprites[j-1].append(spritesheet.subsurface((dimensoes)))
		self.image = self.lista_sprites[0][0]
		self.rect = self.image.get_rect(x=100, y=100)


	def desenhar_sprites(self):
		pressed = self.amb.key.get_pressed()
		self.screen.blit(self.image, self.posicao_plot)
		self.posicao = self.posicao_plot[:]
		if pressed[self.right]:

			self.posicao[0] += self.velocidade[0]+1
			if self.amb.sprite.spritecollide(self, self.colisao, False) == []:
				self.posicao_plot[0] += self.velocidade[0]
			self.image = self.lista_sprites[2][int(self.indice)]

		elif pressed[self.left]:

			self.posicao[0] -= self.velocidade[0]+1
			if  self.amb.sprite.spritecollide(self, self.colisao, False) == []:
				self.posicao_plot[0] -= self.velocidade[0]
			self.image = self.lista_sprites[1][int(self.indice)]

		elif pressed[self.down]:
			
			self.posicao[1] += self.velocidade[1]+1
			if self.amb.sprite.spritecollide(self, self.colisao, False) == []:
				self.posicao_plot[1] += self.velocidade[1]
			self.image = self.lista_sprites[0][int(self.indice)]

		elif pressed[self.up]:
			
			self.posicao[1] -= self.velocidade[1]+1
			if self.amb.sprite.spritecollide(self, self.colisao, False) == []:
				self.posicao_plot[1] -= self.velocidade[1]
			self.image = self.lista_sprites[3][int(self.indice)]

		self.indice = (self.indice+self.fpp)%3

		self.rect = self.image.get_rect()
		self.rect.x = self.posicao[0]
		self.rect.y = self.posicao[1]