from objeto import Objeto

class Mapa(object):
	def __init__(self, ambiente):
		self.amb = ambiente
		self.floor, self.wall, self.mapa = self.amb.sprite.Group(), self.amb.sprite.Group(), self.amb.sprite.Group()
		self.estrutura()
		self.colisao = []

	def estrutura(self):
		self.fase = [
		"WWWWWWWWWWWWWWW",
		"WFWFFFFFFFFFFFW",
		"WFWWWFFFFWWFFFW",
		"WFFFFFFFFFFFWWW",
		"WWWFFFWWFFFFFFW",
		"WFFFFFFFFFFWWFW",
		"WWWWWFFFFFFFFFW",
		"WFFFFFFWWFFFFFW",
		"WFFFWFFFFFFFFFW",
		"WWWWWWWWWWWWWWW"
		]

		self.x, self.y = 0, 0

		for i in range(len(self.fase)):
			for j in range(len(self.fase[i])):
				if self.fase[i][j] == "W":
					sprite = Objeto(self.amb, 'parede64.png', (0,0), (self.x, self.y))
					self.wall.add(sprite)
					self.mapa.add(sprite)
				if self.fase[i][j] == "F":
					sprite = Objeto(self.amb, 'chao64.png', (0,0), (self.x, self.y))
					self.floor.add(sprite)
					self.mapa.add(sprite)
				self.x += sprite.get_size()[0]
			self.y += sprite.get_size()[1]
			self.x = 0
			
	def return_colisao(self):
		return self.wall