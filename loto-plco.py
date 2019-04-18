
X = "X"
O = "O"
import math
import random

board = list(range(1,10))

def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)


def check_win(board):
    win_coord = ((0,1,2),(3,4,5),
                (6,7,8),(0,3,6),
                (1,4,7),(2,5,8),
                (0,4,8),(2,4,6))
   
    for row in win_coord:
        if board[row[0]] == board[row[1]] == board[row[2]]:
            return board[row[0]]
    return None

def first_player():
    first = (input('Если хотите ходить первым - введите "y"'))
    if first == 'y':
        human = X
        computer = O
    else:
        human = O
        computer = X
    return human, computer



def human_move(human):
    player_answer = int(input('Куда поставим ' + human +'?. Введите число.'))
    if player_answer in range(1,10):
        if (str(board[player_answer-1]) not in 'XO'):
            board[player_answer-1] = human
        else:
            print ('Эта клеточка уже занята')
    else:
        print ('Введите число от 1 до 9.')



def computer_move(board, computer):
    l = []
    for i in board:
        try:
            num = int(i)
            l.append(num)
        except ValueError:
            continue

    j = random.choice(l)
    board[j] = computer
    
    

def next_turn(turn):
    if turn == X:
        return O
    else:
        return X


counter = 0
win = False
computer, human = first_player()
turn = X
while not win:
    draw_board(board)
    if human == X:
        human_move(human)
    else:
        print('Ход компьютера')
        computer_move(board, computer)
        
    turn = next_turn(turn)
    counter += 1
    if counter > 4:
        tmp = check_win(board)
        if tmp:
            print (tmp, "выиграл!")
            win = True
            break
    if counter == 9:
        print ("Ничья!")
        break
draw_board(board)


