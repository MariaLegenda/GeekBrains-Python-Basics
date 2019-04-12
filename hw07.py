import random

def get_nums( nums ):
    while len(nums):
        idx = random.randint(0, len(nums)-1)
        yield nums.pop(idx)

def get_barrels_for_card():
    return get_nums(list(range(1,91)))

def get_place():
    return get_nums(list(range (0,9)))


class Card:
    def __init__(self, name):
        self._name = name
        self._card = self._make_card('')
        self._count_barrel = 9

    def _make_card(self, name):
        self.name = name
        self._card = []

        for l in range(3):
            line = [0 for i in range(9)]
            nums = [get_barrals_for_card(__next__()) for i in range(5)]
            nums.sort()
            
            places = [get_place(__next__()) for i in range(5)]
            places.sort()

            for place,num in list(zip(places, nums)):
                line[place] = num
            
            self._card.append(line)
        return self._card

    def print_card(self):
        for row in self._card:
            line = " "
            for col in row:
                ph = " " if col == 0 else " ttt" if col == -1 else str(col)
                line += "{:2}".format(ph) + ' '
            print(line)
            

    def find_number(self, number):
        for i in range(len(self._card)):
            for j in range(len(self._card[i])):
                if self._card[i][j] == number:
                    self._card[i][j] = "-"
                    self._count_barrel -= 1
        return self._card

    def get_card(self):
        return self._card

    def get_card_barrel_count(self):
        return self._count_barrel

    def get_name(self):
        return self._name


class Bag:
    def __init__(self):
        self._bag = [i for i in range(1, 91)]

    def pick_barrel(self):
        barrel = random.choice(self._bag)
        self._bag.remove(barrel)
        print("Новый бочонок: {} (осталось {})".format(barrel, len(self._bag)))
        return barrel


class Game:
    def __init__(self, player, comp):
        self.player = player
        self.comp = comp
        self.bag = Bag()
        self._start()

    def _get_current_stats(self):
        print("------- Ваша карточка ------")
        self.player.print_card()
        print("-"*28)
        print("---- Карточка компьютера ---")
        self.comp.print_card()
        print("-"*28)

    def _check_winner(self):
        if self.player.get_card_barrel_count() == 0 and self.comp.get_card_barrel_count() != 0:
            print("Победил {}".format(self.player.get_name()))
        elif self.comp.get_card_barrel_count() == 0 and self.player.get_card_barrel_count() != 0:
            print("Победил {}".format(self.comp.get_name()))
        elif self.player.get_card_barrel_count() == 0 and self.comp.get_card_barrel_count() == 0:
            print("Ничья")

    def _start(self):
        while self.player.get_card_barrel_count() != 0 and self.comp.get_card_barrel_count() != 0:
            current_barrel = self.bag.pick_barrel()
            self._get_current_stats()
            answer = input("Зачеркнуть цифру? (y/n) ")
            while answer not in "yn":
                print("Неизвестная команда")
                answer = input("Зачеркнуть цифру? (y/n) ")
            if answer == "y":
                if any(current_barrel in x for x in self.player.get_card()):
                    self.player.find_number(current_barrel)
                else:
                    print("Вы проиграли. Цифра {} была у вас в карточке".format(current_barrel))
                    break
            elif answer == "n":
                if any(current_barrel in x for x in self.player.get_card()):
                    print("Вы проиграли. Цифра {} была у вас в карточке".format(current_barrel))
                    break
            if any(current_barrel in x for x in self.player.get_card()):
                self.player.find_number(current_barrel)
            if any(current_barrel in x for x in self.comp.get_card()):
                self.comp.find_number(current_barrel)

        self._check_winner()


game = Game(Card("Игрок"), Card("Компьютер"))