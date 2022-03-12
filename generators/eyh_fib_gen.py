
import random
from math import sqrt

eyh_a = 0
eyh_x0 = 0
eyh_c = 0
out_size = 0

def is_prime(a):
	cnt = int(sqrt(a))
	for i in range(2,cnt+1):
		if a%i==0:
			return 0
	return 1

def ext_evc(a,b):
	x2 = 1
	x1 = 0
	y2 = 0
	y1 = 1
	while b>0:
		q = a // b
		r = a - q*b
		x = x2 - q*x1
		y = y2 - q*y1
		a = b
		b = r
		x2 = x1
		x1 = x
		y2 = y1
		y1 = y
	return [a,x2,y2]

def set_eyh_par():
	global eyh_x0
	global eyh_a
	global eyh_c
	global out_size
	print("Параметр x_0:", end='')
	eyh_x0 = input()
	print("Параметр a:", end='')
	eyh_a = input()
	print("Параметр c:", end='')
	eyh_c = input()
	print("Длина выходной последовательности:", end='')
	out_size = input()
	return

def gen_eyh_par():
	global eyh_x0
	global eyh_a
	global eyh_c
	global out_size
	out_size = random.randint(5,2**16)
	while is_prime(out_size)==0:
		out_size = random.randint(5,2**16)
	eyh_x0 = random.randint(1,2**31)%out_size
	while eyh_x0%2!=1:
		eyh_x0 = random.randint(5,2**16)%out_size
	eyh_a = random.randint(1,2**31)%out_size
	while eyh_a%2!=1 and eyh_a%4==1:
		eyh_a = random.randint(1,2**16)%out_size
	eyh_c = random.randint(1,2**31)%out_size
	while eyh_c%2!=0 and eyh_c%4==2:
		eyh_c = random.randint(1,2**16)%out_size
	print("Параметр x0:",eyh_x0,"\nПараметр a:",eyh_a,"\nПараметр c:",eyh_c,"\nДлина выходной последовательности:",out_size)
	return

def eyh_comp():
	xt = eyh_x0
	a = eyh_a
	c = eyh_c
	N = out_size
	f = open('eyh_out.txt','w')
	f.write(str(xt)+'\n')
	for i in range(N):
		if xt==0:
			f.write(str(c)+'\n')
			xt = c
		else:
			xt = (a*ext_evc(N,xt)[2]+c)%N
			f.write(str(xt)+'\n')
	f.close()
	return

def eyh_read_file():
	global eyh_x0
	global eyh_a
	global eyh_c
	global out_size
	f = open('eyh_par.txt','r')
	l = [line.strip() for line in f]
	eyh_x0 = int(l[0])
	eyh_a = int(l[1])
	eyh_c = int(l[2])
	out_size = int(l[3])
	f.close()
	return


def start_eyh():
	print("sPar - Установить параметры вручную")
	print("gPar - Сгенерировать параметры случайно")
	cmd = input()
	if cmd=='sPar':
		set_eyh_par()
	elif cmd=='gPar':
		gen_eyh_par()
	else:
		eyh_read_file()
	eyh_comp()
	return


def start_fib():
	return


if __name__ == '__main__':
	print("eyh - Запустить генератор Эйхенауэра-Лена")
	print("fib - Запустить генератор Фибоначи\nВведите команду:",end='')
	cmd = input()
	if cmd=='eyh':
		start_eyh()
	if cmd=='fib':
		start_fib()
	#print(ext_evc(11,2))