# coding=utf-8
from random import randint


class Generator_Fibonacci:

	"""
	Генератор Фибоначчи (аддитивный)
	Входные параметры:
	1) s - лаг
	2) r - лаг, размер начального набора
	3) N - модуль
	4) out_size - количество генерируемых чисел
	"""

	def __init__(self, s: int = randint(5, 100), r: int = randint(10, 500), N: int = 2**randint(5, 16), out_size: int = 100):
		self.__s = s
		self.__r = r
		if self.__r <= self.__s:
			self.__r = s + 1
			self.__s = r
		self.__N = N
		self.__out_size = out_size

	def gen(self):
		fibs = []
		for i in range(self.__r):
			fibs.append(randint(0, self.__N))
		f = open('fib_out.txt', 'w')
		for i in range(self.__out_size):
			x = (fibs[0] + fibs[-self.__s]) % self.__N
			f.write(str(x) + "\n")
			fibs.pop(0)
			fibs.append(x)
		f.close()

	def __str__(self):
		return f"Генератор Фибоначчи:\n1) s = {self.__s}\n2) r = {self.__r}\n3) N = {self.__N}\n4) out_size = {self.__out_size}"

	def __repr__(self):
		return f"Generator_Fibonacci({self.__s}, {self.__r}, {self.__N}, {self.__out_size})"
