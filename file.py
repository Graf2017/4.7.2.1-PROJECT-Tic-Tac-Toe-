# 4.7.2.1 PROJECT: Tic-Tac-Toe

from random import randrange
board = [[3*y+x+1 for x in range(3)]for y in range(3)]
board[1][1] ='x'
def display_board(board):
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ', board[0][0], '  |  ', board[0][1], '  |  ', board[0][2], '  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ', board[1][0], '  |  ', board[1][1], '  |  ', board[1][2], '  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ', board[2][0], '  |  ', board[2][1], '  |  ', board[2][2], '  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')


def enter_move(board):
    ring = True
    while ring:

        move = int(input('Enter your move\n'))
        if move < 1 or move > 9:
            print('Out of range')
            continue

        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == move:
                    board[x][y] = 'o'
                    ring = False
                    return
        print('the move has already been earlier')


def make_list_of_free_fields(board):
    lst = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] not in ['o','x']: # if board[i][check] != 'O' and board[i][check] != 'X':
                lst.append((x,y))
    return lst


def victory_for(board, sign):
    if sign == 'x':
        winner = 'comp win!!!'
    elif sign == 'o':
        winner = 'i win!!!'

    for line in range(len(board)):
        if board[line][0] == sign and board[line][1] == sign and board[line][2] == sign:
            return winner
        if board[0][line] == sign and board[1][line] == sign and board[2][line] == sign:
            return winner
        if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
            return winner
        if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
            return winner
    if len(make_list_of_free_fields(board)) == 0:
        return 'no winner'
def draw_move(board):
    freefield = make_list_of_free_fields(board)
    if len(freefield) > 0:
        comp_step = randrange(len(freefield))
        x,y = freefield[comp_step]
        board[x][y] ='x'


winner =''
while victory_for(board, 'o') == None or victory_for(board, 'x') == None:
    display_board(board)
    enter_move(board)
    victory_for(board, 'o')
    if victory_for(board, 'o'):
        winner = victory_for(board, 'o')
        break
    make_list_of_free_fields(board)
    draw_move(board)
    display_board(board)
    victory_for(board, 'x')
    if victory_for(board, 'x'):
        winner = victory_for(board, 'x')
        break
print(f'{winner.title()}')
