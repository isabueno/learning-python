    #scope
#1. player 1 choose char, player2 gets the other in a dict OK
#2. print a board OK
#3. player chooses position, checks if its empty and marks the original board. if not, asks it again. OK
#4. checks if game is won or tied OK
#5. if not, 3 and 4 until game is finished. OK
#6. validating inputs

def starting_input():
    player1 = ''
    while not (player1 == 'X' or player1 == 'O'):
        player1 = input("Player 1, choose your character (O,X): ")
    
    if player1 == 'X':
        player2 = 'O'
        print("Player 2 will be O")
    elif player1 == 'O':
        player2 = 'X'
        print("Player 2 will be X")
    
    return {"player1": player1, "player2": player2}

def choose_position(char, board):
    empty_position  = False

    while empty_position == False:
        number = input("Choose your position from 1-9: ")
        if number in ['1','2','3','4','5','6','7','8','9']:
            position = int(number) -1
            if board[position] == ' ':
                board[position] = char
                game_board = " "+ board[0] + " | " + board[1] + " | " + board[2] + "\n-----------\n" + " "+ board[3] + " | " + board[4] + " | " + board[5] + "\n-----------\n" + " "+ board[6] + " | " + board[7] + " | " + board[8]
                empty_position = True
            else:
                print("Position already marked!")

    return game_board #doesnt this always return?

def check_win(brd, char):
    return ((brd[0] == char and brd[1] == char and brd[2] == char) or 
    (brd[3] == char and brd[4] == char and brd[5] == char) or 
    (brd[6] == char and brd[7] == char and brd[8] == char) or 
    (brd[0] == char and brd[4] == char and brd[8] == char) or 
    (brd[2] == char and brd[4] == char and brd[6] == char) or 
    (brd[0] == char and brd[3] == char and brd[6] == char) or 
    (brd[1] == char and brd[4] == char and brd[7] == char) or 
    (brd[2] == char and brd[5] == char and brd[8] == char))

def game():
    players = starting_input()
    #brd = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    brd = [' '] * 9 

    for i in range(9):
        if i % 2 == 0:
            char = players["player1"]
            print(choose_position(char, brd))
            if check_win(brd, char):
                print('Player 1 has won!')
                break
        elif i % 2 != 0:
            char = players["player2"]
            print(choose_position(char, brd))
            if check_win(brd, char):
                print('Player 2 has won!')
                break        
        else:
            print('Game is tied!')


game()

