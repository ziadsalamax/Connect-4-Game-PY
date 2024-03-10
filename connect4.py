# Program: Connect- 4 game. A board of 7 columns x 6 rows is displayed
#          Players choose a symbol, either X or O. In their turn, they drop the symbol from top of the
#          board until it settles in the bottom empty cell. The first player to connect 4 symbols
#          horizontally, vertically or diagonally wins.
# Author: Ziad Ahmed
# Version: 2
# Date: 01/03/2024


def printBoard(board):
    counter = 6
    for i in range(6):
        print(counter, end='')
        counter -= 1
        for j in range(7):
            print(f" {board[i][j]} ", end='')
        print()
    print("  1  2  3  4  5  6  7")

def checkBoard(board):
    # Check Horizontally
    for i in range(6):
        for j in range(4):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] and board[i][j] != '▒':
                return True
    # Check Vertically
    for i in range(7):
        for j in range(3):
            if board[j][i] == board[j+1][i] == board[j+2][i] == board[j+3][i] and board[j][i] != '▒':
                return True
    # Check Diagonally Left to Right
    for i in range(3):
        if board[i][i] == board[i+1][i+1] == board[i+2][i+2] == board[i+3][i+3] and board[i][i] != '▒':
            return True
        elif board[i][i+1] == board[i+1][i+2] == board[i+2][i+3] == board[i+3][i+4] and board[i][i+1] != '▒':
            return True
        if i != 2:
            if board[i][i+2] == board[i+1][i+3] == board[i+2][i+4] == board[i+3][i+5] and board[i][i+2] != '▒':
                return True
    if board[0][3] == board[1][4] == board[2][5] == board[3][6] and board[0][3] != '▒':
        return True
    for i in range(2):
        if board[i+1][i] == board[i+2][i+1] == board[i+3][i+2] == board[i+4][i+3] and board[i+1][i] != '▒':
            return True
    if board[2][0] == board[3][1] == board[4][2] == board[5][3] and board[2][0] != '▒':
        return True

    # Check Diagonally Right to Left
    for i in range(3):
        if board[i][6-i] == board[i+1][6-i-1] == board[i+2][6-i-2] == board[i+3][6-i-3] and board[i][6-i] != '▒':
            return True
        elif board[i][6-i-1] == board[i+1][6-i-2] == board[i+2][6-i-3] == board[i+3][6-i-4] and board[i][6-i-1] != '▒':
            return True
        if i != 2:
            if board[i][6-i-2] == board[i+1][6-i-3] == board[i+2][6-i-4] == board[i+3][6-i-5] and board[i][6-i-2] != '▒':
                return True
    if board[0][3] == board[1][2] == board[2][1] == board[3][0] and board[0][3] != '▒':
        return True
    for i in range(2):
        if board[i+1][6-i] == board[i+2][6-i-1] == board[i+3][6-i-2] == board[i+4][6-i-3] and board[i+1][6-i] != '▒':
            return True
    if board[2][6] == board[3][5] == board[4][4] == board[5][3] and board[2][6] != '▒':
        return True
    return False











def main():
    # Set the game base
    board = [
        ['▒', '▒', '▒', '▒', '▒', '▒', '▒'], #6
        ['▒', '▒', '▒', '▒', '▒', '▒', '▒'], #5
        ['▒', '▒', '▒', '▒', '▒', '▒', '▒'], #4
        ['▒', '▒', '▒', '▒', '▒', '▒', '▒'], #3
        ['▒', '▒', '▒', '▒', '▒', '▒', '▒'], #2
        ['▒', '▒', '▒', '▒', '▒', '▒', '▒']  #1
          #1   #2   #3   #4   #5   #6   #7
    ]
    # Print Weclome Message
    print("Welcome to Connect 4!")
    print("The first player to connect 4 symbols horizontally, vertically or diagonally wins.")
    printBoard(board)
    winner = False
    while not winner:
        # Player X input
        move = int(input("Player X: "))
        # Check if the input is valid
        while move > 7 or move < 1:
            move = int(input("Player X: "))

        # Update the board
        for i in range(5, -1, -1):
            if board[i][move-1] == '▒':
                board[i][move-1] = 'X'
                break
            else:
                continue
        printBoard(board)
        winner = checkBoard(board)
        if winner:
            print("Player X Wins!")
            break

        # Player O input
        move = int(input("Player O: "))
        # Check if the input is valid
        while move > 7 or move < 1:
            move = int(input("Player O: "))

        # update the board
        for i in range(5, -1, -1):
            if board[i][move-1] == '▒':
                board[i][move-1] = 'O'
                break
            else:
                continue
        printBoard(board)
        winner = checkBoard(board)
        if winner:
            print("Player O Wins!")
            break
    if not winner:
        print("Draw!")

main()
