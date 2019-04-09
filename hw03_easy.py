__author__ = 'Потапова Мария'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number = number * (10 ** ndigits)
    if float(number) - int(number) >= 0.5:
         number = number // 1 + 1
    else:
         number = number // 1
    return number / (10 ** ndigits)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(2.444467, 3))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
	if (sum(list(map(int, list(str(ticket_number)[:3])))) == sum(list(map(int, list(str(ticket_number)[3:]))))):
		return 'Билет счастливый!'
	else:
		return 'Билет обычный.'

print(lucky_ticket(123006), 'Номер билета 123006')
print(lucky_ticket(12321), 'Номер билета 12321')