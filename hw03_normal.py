__author__ = 'Потапова Мария'

import math

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
	f1=f2=1
	f_list=[f1,f2]
	i = 0
	while len(f_list) < m:
		f_sum = f1 + f2
		f1 = f2
		f2 = f_sum
		i += 1
		f_list.append(f_sum)
	return f_list[n-1:m];

print('ряд Фибоначчи:', fibonacci(1, 5))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
	origin_list = list(origin_list)
	l = len(origin_list)
	for i in range(l-1):
		for j in range(l-i-1):
			if origin_list[j] > origin_list[j+1]:
				origin_list[j], origin_list[j+1] = origin_list[j+1], origin_list[j]
	return origin_list

 
print('Исходный список: ',[2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print('Отсортированный список: ',sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def user_filter(func, iter):
	if func is None:
		return (i for i in iter if i)
	else:
		return (i for i in iter if func(i))

print(list(user_filter(lambda x: True if x == '499' else False, ['376', '43', '499', '880', '880', '43', '499'])))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
def paral(A1, A2, A3, A4):

	A1A2 = math.sqrt((A2[0]-A1[0])**2 + (A2[1]-A1[1])**2)
	A3A2 = math.sqrt((A3[0]-A2[0])**2 + (A3[1]-A2[1])**2)
	A3A4 = math.sqrt((A3[0]-A4[0])**2 + (A3[1]-A4[1])**2)
	A4A1 = math.sqrt((A4[0]-A1[0])**2 + (A4[1]-A1[1])**2)
	A3A1 = math.sqrt((A3[0]-A1[0])**2 + (A3[1]-A1[1])**2)
	A2A4 = math.sqrt((A2[0]-A4[0])**2 + (A2[1]-A4[1])**2)

	if A1A2 == A3A4 and A3A2==A4A1 and (A3A1**2+A2A4**2 == 2*A4A1**2+2*A1A2**2):
		return 'Точки являются вершинами параллелограмм'
	else:
		return 'Точки не образуют пкараллелограмм'

print(paral([1,1], [2,4], [6,4], [5,1]))
print(paral([1,-1], [1,2], [5,2], [5,-1]))
print(paral([-1,-1], [1,2], [5,2], [5,-1]))