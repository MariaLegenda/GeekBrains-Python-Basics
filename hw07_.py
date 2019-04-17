
from random import randint

class Card:
    def __init__(self, name):
        bag = [x for x in range(1, 91)]  
        self.card = [__class__.card_line(bag), 
                     __class__.card_line(bag),
                     __class__.card_line(bag)]
        self.name = name
        self.count_barrel = 15  

    @staticmethod
    def card_line(bag):
        string = ['' for _ in range(9)]
        for x in range(8, 3, -1):
            digit = randint(0, x)  
            while string[digit] != '':  
                digit += 1
            string[digit] = bag.pop(randint(0, len(bag) - 1))
        return string

    def __str__(self):
        rez = '{:-^26}\n'.format(self.name)
        for x in range(3):
            rez += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'\
                    .format(*self.card[x]) + '\n'
        return rez + '-'*27

computer = Card(' Карточка компьютера ')
player = Card(' Карточка игрока ')
bag = [x for x in range(1, 91)]  
while True:
    if len(bag) < 1:
        print('Бочёнки в мешке закончились. Результат:\n'
              'у компьютера осталось {} числа/чисел,\n'
              'у игрока осталось {} числа/чисел.'
              .format(computer.count_barrel, player.count_barrel))
        break

    barrel = bag.pop(randint(0, len(bag) - 1))
    print('\nНовый бочонок: {} (осталось {})'.format(barrel, len(bag)))
    print(computer)
    print(player)
   
    reply = (input('Зачеркнуть цифру? (y/n/q)')).lower()
    while len(reply) == 0 or reply not in 'ynq':
        print('\n!!! Ответ не распознан!\n')
        print('Новый бочонок: {} (осталось {})'.format(barrel, len(bag)))
        print(computer)
        print(player)
        reply = (input('Зачеркнуть цифру? (y/n/q)')).lower()
        

    if reply == 'q':
        print('Вы сдались. Выиграл компьютер')
        break
    elif reply == 'y':
        test = False  
        for x in range(3):
            if barrel in player.card[x]:
                test = True
                player.card[x][player.card[x].index(barrel)] = '-'
                player.count_barrel -= 1
            if barrel in computer.card[x]:
                computer.card[x][computer.card[x].index(barrel)] = '-'
                computer.count_barrel -= 1
        if test:
            if player.count_barrel < 1:
                print('Вы выиграли!')
                break
            elif computer.count_barrel < 1:
                print('Компьютер выиграл!')
                break
        else:
            print('Вы проиграли! Такого числа нет на Вашей карточке!')
            break
    elif reply == 'n':
        test = False  
        for x in range(3):
            if barrel in player.card[x]:
                print('Вы проиграли! Такое число есть на Вашей карточке!')
                test = True
                break
            if barrel in computer.card[x]:
                computer.card[x][computer.card[x].index(barrel)] = '-'
                computer.count_barrel -= 1
        if test:
            break
        if player.count_barrel < 1:
            print('Вы выиграли!')
            break
        elif computer.count_barrel < 1:
            print('Компьютер выиграл!')
            break