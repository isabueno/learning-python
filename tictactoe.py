def starting_input():
    #validate input
    player1 = input("Player 1, choose your character (O,X): ")
    if player1 == 'X':
        player2 = 'O'
        print("Player 2 will be O")
    elif player1 == 'O':
        player2 = 'X'
        print("Player 2 will be X")
    
    print("THIS IS {}, {}".format(player1, player2))
    #empty board
    print("    |    |    \n ------------- \n    |    |    \n ------------- \n    |    |   ")

def choose_position():
    position = int(input("Choose your position from 1-9: "))

    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    board.insert(position-1, 'X')
    
    #board
    print(" "+ board[0] + " | " + board[1] + " | " + board[2] + "\n-----------\n" + " "+ board[3] + " | " + board[4] + " | " + board[5] + "\n-----------\n" + " "+ board[6] + " | " + board[7] + " | " + board[8])
    #check_position(board)


def check_position(brd):
    if brd[0] == brd[1] == brd[2] or brd[3] == brd[4] == brd[5] or brd[6] == brd[7] == brd[8] or brd[0] == brd[4] == brd[8]:
        print("Has won")


def game():
    #getting input
    starting_input()

    #turns

    choose_position()

#
game()