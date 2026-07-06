


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

next_play = 'X' 
gameRunning = True
winner = None 
fill = 0 

def printBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

def switch(next_play):
    if(next_play == 'X'):
        next_play = 'O'
    else:
        next_play = 'X'
    return next_play

def checkWinOrTie(board, fill):
    ## if win or tie then gameRunning = False
    if(((board[0] == board[1] == board[2] != '-') or (board[3] == board[4] == board[5] != '-')
       or (board[6] == board[7] == board[8] != '-') or (board[0] == board[3] == board[6] != '-')
       or (board[1] == board[4] == board[7] != '-') or (board[2] == board[5] == board[8] != '-')
       or (board[0] == board[5] == board[8] != '-') or (board[2] == board[5] == board[6] != '-'))
       and (fill >=5)):
        print("You win!")
        printBoard(board)
        print("Game over")
        return False
        ## board full is also tie
    elif (fill == 9):
        print("Board Full ! Game tied !")
        return False
    else:
        return True

def makeMove(gameRunning, board, next_play, fill):
    while(gameRunning):
        ## Display board and whose turn it is
        printBoard(board)
        print('Its ' + next_play + ' move.')
        ## Check for winner or tie and display if yes , if not record their move
        play = int(input('Enter a number between 1 to 9: '))
        while(play< 1 or play > 9 or board[play-1]!='-'):
            print("Invalid number entered. Enter again!")
            play = int(input('Number :'))
        fill+= 1 
        board[play-1] = next_play
        next_play = switch(next_play)
        gameRunning = checkWinOrTie(board, fill)
        

def main():
    gameRunning = True
    print("X moves first!")
    makeMove(gameRunning, board, 'X', 0)

main()
    
