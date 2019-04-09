__author__ = 'Потапова Мария'

import math
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class triangle:
	def __init__(self, A1, A2, A3):
		self.A1 = [1,3]		
		self.A2 = [4,7]
		self.A3 = [3,3]

		#определение длин сторон
		def lenght(point1, point2):
			return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

		self.A1A3 = lenght(self.A1, self.A3)
		self.A1A2 = lenght(self.A1, self.A2)
		self.A2A3 = lenght(self.A2, self.A3)

	#определение периметра
	def perimeter(self):
		return round(self.A1A3+self.A2A3+self.A1A2)

	#определение площади
	def area(self):
		S = [(self.A1[0]-self.A3[0]), (self.A1[1]-self.A3[1])],\
			[(self.A2[0]-self.A3[0]), (self.A2[1]-self.A3[1])]
		return round(abs(S[0][0]*S[1][1]-S[1][0]*S[0][1])/2)
		 
	#определение высот
	def height(self):
		h1 = round(self.area()/self.A1A2) 
		h2 = round(self.area()/self.A1A3)
		h3 = round(self.area()/self.A2A3) 
		return(h1, h2, h3)

	def info(self):
		print('периметр треугольника: ' + str(self.perimeter()))
		print('площадь треугольника: ' + str(self.area()))
		print ('высоты треугольника: ' + str(self.height()))
		print()


Tr3 = triangle([],[],[])
Tr3.info()


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class trapezium:
	def __init__(self, a, b, c, d):
		self.a = [1,3]		
		self.b = [4,7]
		self.c = [5,7]
		self.d = [8,3]

		#определение длин сторон
		def lenght(point1, point2):
			return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

		self.ab = lenght(self.a, self.b)
		self.bc = lenght(self.b, self.c)
		self.cd = lenght(self.c, self.d)
		self.da = lenght(self.d, self.a)

		self.ac = lenght(self.a, self.c)
		self.bd = lenght(self.b, self.d)

	#для печати длин сторон
	def line(self):
		return( str(round(self.ab)) , str(round(self.bc)) , str(round(self.cd)) ,str(round(self.da)))
	
	#определение периметра
	def perimeter(self):
		return round(self.ab+self.bc+self.cd+self.da)

	#определение высоты
	def height(self):
		return round(math.sqrt(self.ab**2-(((self.da-self.bc)**2+self.ab**2-self.cd**2)\
			/2/(self.da**2-self.bc**2))**2))

	#определение площади
	def area(self):
		return round((self.da+self.bc)*self.height()/2)

	#проверка равнобедренности по равенству диагоналей
	def check(self):
		if self.ac == self.bd:
			print('трапеция равнобедренная')
		else:
			print('трапеция не равнобедренная')

	def info(self):
		print('Длина сторон: '+ str(self.line()))
		print('периметр трапеции: ' + str(self.perimeter()))
		print('площадь трапеции: ' + str(self.area()))
		

Tr4 = trapezium([],[],[],[])
Tr4.info()
Tr4.check()