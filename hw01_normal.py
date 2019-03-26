__author__ = 'Потапова Мария'

import math

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

print('Задание 1. Нахождение максимальной составляющей числа')
a = abs(int(input('Введите целое число: ')))

max=0
while a>0:
    n = a % 10
    if n>max:
        max = n
    a = a // 10
print(max)




# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

print('Задание 2. Изменение значений переменных')
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

a = a+b
b = a-b
a = a-b

print('Измененное число a:', a)
print('Измененное число b:', b)




# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print('Задание 3. Нахождение корней уравнения вида ax² + bx + c = 0')
a = float(input('Введите число a: '))
b = float(input('Введите число b: '))
c = float(input('Введите число c: '))

D = b**2-4*a*c
if D<0:
    print('квартарное уравнение не имеет корней')
elif D == 0:
    x = -b/2/a
    print('Уравнение имеет один корень: ', x)
else:
    x1 = (-b+math.sqrt(D))/2/a
    x2 = (-b-math.sqrt(D))/2/a
    print('Первый корень кв. уравнения: ', x1, ' Второй корень кв. уравнения: ', x2)


