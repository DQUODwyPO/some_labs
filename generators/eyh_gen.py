# coding=utf-8
from random import randint
from math import sqrt


class Generator_Eich:
	"""
	Генератор Эйхенауэра-Лена с обращением
	Входные параметры:
	1) a - множитель
	2) x0 - зерно, начальное значение
	3) c - приращение
	4) N - модуль
	5) out_size - количество генерируемых чисел
	"""

	def __init__(self, a: int = None, x0: int = None, c: int = None, N: int = None, out_size: int = 100):
		self.__a = a
		self.__x0 = x0
		self.__c = c
		self.__N = N
		self.gen_par()
		self.__out_size = out_size

	def gen(self):
		xt = self.__x0
		f = open('eyh_out.txt', 'w')
		f.write(str(xt) + '\n')
		for i in range(self.__out_size):
			if xt == 0:
				f.write(str(self.__c) + '\n')
				xt = self.__c
			else:
				xt = (self.__a * self.ext_evc(self.__N, xt)[2] + self.__c) % self.__N
				f.write(str(xt) + '\n')
		f.close()

	def gen_par(self):
		if self.__N is None:
			self.__N = randint(5, 2 ** 16)
			while self.is_prime(self.__N) == 0:
				self.__N = randint(5, 2 ** 16)

		if self.__x0 is None:
			self.__x0 = randint(1, 2 ** 31) % self.__N
			while self.__x0 % 2 != 1:
				self.__x0 = randint(5, 2 ** 16) % self.__N

		if self.__a is None:
			self.__a = randint(1, 2 ** 31) % self.__N
			while self.__a % 2 != 1 and self.__a % 4 == 1:
				self.__a = randint(1, 2 ** 16) % self.__N

		if self.__c is None:
			self.__c = randint(1, 2 ** 31) % self.__N
			while self.__c % 2 != 0 and self.__c % 4 == 2:
				self.__c = randint(1, 2 ** 16) % self.__N

	@staticmethod
	def is_prime(a):
		cnt = int(sqrt(a))
		for i in range(2, cnt + 1):
			if a % i == 0:
				return 0
		return 1

	@staticmethod
	def ext_evc(a, b):
		x2 = 1
		x1 = 0
		y2 = 0
		y1 = 1
		while b > 0:
			q = a // b
			r = a - q * b
			x = x2 - q * x1
			y = y2 - q * y1
			a = b
			b = r
			x2 = x1
			x1 = x
			y2 = y1
			y1 = y
		return [a, x2, y2]

	def __str__(self):
		return f"Генератор Эйхенауэра-Лена с обращением:\n1) a = {self.__a}\n2) x0 = {self.__x0}\n" \
			   f"3) c = {self.__c}\n4) N = {self.__N}\n5) out_size = {self.__out_size}"

	def __repr__(self):
		return f"Generator_Eich({self.__a}, {self.__x0}, {self.__c}, {self.__N}, {self.__out_size})"
