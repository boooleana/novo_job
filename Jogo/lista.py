
#1.a) rodas - b)material - c)paredes, teto

#2
class Circle(object):
	def __init__(self, raio):
		self.raio = int(raio)

	def calcular_circunferencia(self):
		c = 3,14*self.raio^2
		return c

#3
class Animal(object):
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

class Cachorro(Animal):
	def __init__(self, nome, idade, raca, cor_pelo):
		Animal.__init__(nome, idade)
		self.raca = raca
		self.cor_pelo = cor_pelo

#4. classe é a estrutura e o objeto é o que já foi "estruturado" o que já foi construido com os moldes da classe

#5

class Ponto(object):
	def __init__(self, coord):
		self.x = coord[0]
		self.y = coord[1]

class Triangulo(Ponto):
	def __init__(self, coord_1, coord_2, coord_3):
		self.ponto_1 = Ponto(coord_1)
		self.ponto_2 = Ponto(coord_2)
		self.ponto_3 = Ponto(coord_3)

class Quadrado(Ponto):
	def __init__(self, coord_1, coord_2, coord_3, coord_4):
		self.ponto_1 = Ponto(coord_1)
		self.ponto_2 = Ponto(coord_2)
		self.ponto_3 = Ponto(coord_3)
		self.ponto_4 = Ponto(coord_4)