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
    return False


def take_input(symbol):
    player_answer = int(input('Куда поставим ' + symbol +'?. Введите число.'))
    if player_answer in range(1,10):
        if (str(board[player_answer-1]) not in 'XO'):
            board[player_answer-1] = symbol
        else:
            print ('Эта клеточка уже занята')
    else:
        print ('Введите число от 1 до 9.')



def main(board):
    player1 = input('Введите имя игрока 1: ')
    player2 = input('Введите имя игрока 2: ')
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            print('Ходит ', player1)
            take_input("X")
        else:
            print('Ходит ', player2)
            take_input("O")
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


main(board)