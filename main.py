# global variables

import random

player = "O"
computer = "X"


# turn = True # if the turn is true, the player is playing


def rowInput():
    # returns the valid number of rows
    while True:
        try:
            row = int(input('Enter row:'))
            if row >= 0:
                return row
            print('Only enter whole numbers greater than 0!')
        except ValueError:
            print('Enter whole numbers only!')


def columnInput():
    # returns the valid number of columns
    while True:
        try:
            column = int(input('Enter column:'))
            if column >= 0:
                return column
            print('Only enter numbers that are more than 0!')
        except ValueError:
            print('Enter whole numbers only!')


def welcomeMessage():
    print("Welcome to the Game of Connect 4!")


def pickMode():
    # returns the selected mode number from te user
    errorMessage = 'Enter "1", "2", or "3" only!'
    while True:
        try:
            mode = int(input('Enter a mode: '))
            if mode == 1 or mode == 2 or mode == 3:
                return mode
            print(errorMessage)
        except ValueError:
            print(errorMessage)


def updateBoard(b, col, bRow, turn):
    for x in range(len(b)):
        if b[x][col - 1] == '-':
            continue
        else:
            b[x - 1][col - 1] = turnSymbol(turn)
            return

    if b[-1][col - 1] == "-":
        b[-1][col - 1] = turnSymbol(turn)


def turnSymbol(turn):
    if turn:
        return player
    else:
        return computer


def validCol(b, col):
    for x in range(len(b)):
        if b[x][col - 1] == '-':
            return True
        else:
            return False


def colBoardInput(col):
    # returns the valid number of columns for the board
    while True:
        try:
            column = int(input('Enter column:'))
            if 0 < column <= col:
                return column
            print('Only enter numbers that are more than 0 and less than the size of the board!')
        except ValueError:
            print('Enter whole numbers only!')


def playerTurn(b, row, column, turn):
    print("Your turn")
    while True:
        col = colBoardInput(column)
        if validCol(b, col):
            break
        else:
            print('no space left in this column')
    updateBoard(b, col, row, turn)
    printBoard(b)


def computerTurn(b, bRow, bCol, turn):
    print("Computer Turn")
    while True:
        randomColumn = random.randint(0, bCol - 1)
        if validCol(b, randomColumn):
            break
    updateBoard(b, randomColumn, bRow, turn)
    printBoard(b)


def whoGoesFirst(playerNo1, playerNo2, first):
    # recursive function that returns the player name whose going first
    if first == playerNo1 or first == playerNo2:
        return first
    else:
        first = input('Which player is going first?[' + playerNo1 + ' or ' + playerNo2 + '] ')
        # string concatenation
        return whoGoesFirst(playerNo1, playerNo2, first)


# VS HUMAN *********
def vsHuman(b, bRow, bCol):
    first = None
    while True:
        player1 = input('Player 1: ')
        player2 = input('Player 2: ')
        if player1 == player2:
            print('The names should not be the same!')
        else:
            break
    firstPlayer = whoGoesFirst(player1, player2, first)
    playVsHuman(player1, player2, firstPlayer, b, bRow, bCol)


def playVsHuman(player1, player2, first, board, row, col):
    turn = True
    printBoard(board)
    while True:
        print(first + "'s turn")
        playerTurn(board, row, col, turn)
        if gameResult(board, row, col, turn) == 'you win' or \
                gameResult(board, row, col, turn) == 'computer win' or \
                gameResult(board, row, col, turn) == 'draw':
            break
        turn = changeTurn(turn)
        first = changePlayer(player1, player2, first)

    winner = first + ' win'
    if gameResult(board, row, col, turn) == 'you win' or \
            gameResult(board, row, col, turn) == 'computer win':
        print(winner)
    else:
        print('It is a draw!')


def changePlayer(player1, player2, first):
    if first == player1:
        return player2
    else:
        return player1


def changeTurn(turn):
    if turn:
        return False
    else:
        return True


# VS COMPUTER *********
def vsComputer(b, boardRow, boardCol):
    while True:

        turn = True
        playerTurn(b, boardRow, boardCol, turn)
        if gameResult(b, boardRow, boardCol, turn) == 'you win' or \
                gameResult(b, boardRow, boardCol, turn) == 'computer win' or \
                gameResult(b, boardRow, boardCol, turn) == 'draw':
            break

        turn = False
        computerTurn(b, boardRow, boardCol, turn)
        if gameResult(b, boardRow, boardCol, turn) == 'you win' or \
                gameResult(b, boardRow, boardCol, turn) == 'computer wins' or \
                gameResult(b, boardRow, boardCol, turn) == 'draw':
            break

    print(gameResult(b, boardRow, boardCol, turn))


def gameResult(board, bRow, bCol, turn):
    new_turn = turnSymbol(turn)
    # col check
    for row in range(bRow):
        for col in range(bCol):
            if col < bCol - 3:
                if board[row][col] == new_turn and \
                        board[row][col + 1] == new_turn and \
                        board[row][col + 2] == new_turn and \
                        board[row][col + 3] == new_turn:
                    return winCondition(turn)

    # row check
    for col in range(bCol):
        for row in range(bRow):
            if row < bRow - 3:
                if board[row][col] == new_turn and \
                        board[row + 1][col] == new_turn and \
                        board[row + 2][col] == new_turn and \
                        board[row + 3][col] == new_turn:
                    return winCondition(turn)

    # diagonal check
    if diagonal(board, new_turn, bRow, bCol):
        return winCondition(turn)

    # draw
    if draw(board, bRow, bCol):
        return 'draw'

    return


def diagonal(board, turn, ROWS, COLUMNS):
    # returns true if the diagonal tiles are four, otherwise return false
    for row in range(ROWS):
        for col in range(COLUMNS):
            if board[row][col] == turn:
                # bottom left to top right diagonal check

                # bottom left first input check
                # if there are three of the same symbol top right
                if row + 3 < ROWS and col - 3 > -1 and \
                        board[row + 1][col - 1] == turn and \
                        board[row + 2][col - 2] == turn and \
                        board[row + 3][col - 3] == turn:
                    return True

                # bottom left second input check
                # if there are two of the same symbol top right
                # and check if there is one of the same symbol left bottom
                if row + 2 < ROWS and row - 1 > -1 and \
                        col + 1 < COLUMNS and col - 2 > -1 and \
                        board[row - 1][col + 1] == turn and \
                        board[row + 1][col - 1] == turn and \
                        board[row + 2][col - 2] == turn:
                    return True

                # bottom left third input check
                # if there are two of the same symbol right bottom
                # and check if there is one of the same symbol top right
                if row - 2 > -1 and row + 1 < ROWS and \
                        col + 2 < COLUMNS and col - 1 > -1 and \
                        board[row - 1][col + 1] == turn and \
                        board[row - 2][col + 2] == turn and \
                        board[row + 1][col - 1] == turn:
                    return True

                # bottom left fourth input check
                # if there are three of the same symbol bottom left
                if row - 3 > -1 and col + 3 < COLUMNS and \
                        board[row - 1][col + 1] == turn and \
                        board[row - 2][col + 2] == turn and \
                        board[row - 3][col + 3] == turn:
                    return True

                ###################################################
                # top left to bottom right diagonal check

                # top left first input check
                # if there are three of the same symbol bottom right
                if row + 3 < ROWS and col + 3 < COLUMNS and \
                        board[row + 1][col + 1] == turn and \
                        board[row + 2][col + 2] == turn and \
                        board[row + 3][col + 3] == turn:
                    return True

                # top left second input check
                # if there are two of the same symbol bottom right
                # and there is of the same symbol top left
                if row + 2 < ROWS and col + 2 < COLUMNS and \
                        row - 1 > -1 and col - 1 > -1 and \
                        board[row - 1][col - 1] == turn and \
                        board[row + 1][col + 1] == turn and \
                        board[row + 2][col + 2] == turn:
                    return True

                # top left third input check
                # if there are two of the same symbol top left
                # and there is of the same symbol bottom right
                if row - 2 > -1 and col - 2 > -1 and \
                        row + 1 < ROWS and col + 1 < COLUMNS and \
                        board[row - 1][col - 1] == turn and \
                        board[row - 2][col - 2] == turn and \
                        board[row + 1][col + 1] == turn:
                    return True

                # top left fourth input check
                # if there are three of the same symbol top left
                if row - 3 > -1 and col - 3 > -1 and \
                        board[row - 1][col - 1] == turn and \
                        board[row - 2][col - 2] == turn and \
                        board[row - 3][col - 3] == turn:
                    return True

    return False


def draw(board, bRow, bCol):
    for row in range(bRow):
        for col in range(bCol):
            if board[row][col] == '-':
                return False

    return True


def winCondition(turn):
    if turn:
        return 'you win'
    else:
        return 'computer wins'


def printBoard(b):
    for x in range(len(b)):
        for y in range(len(b[0])):
            print(b[x][y], end=" ")
        print()  # next line


def initializeBoard(ROWS, COLUMNS):
    # creates a new board
    rowList = []
    for i in range(0, ROWS):
        columnList = []
        for j in range(0, COLUMNS):
            columnList.append('-')
        rowList.append(columnList)
    return rowList


def gameMode():
    print('What is your preferred board size?')
    while True:
        row = rowInput()
        column = columnInput()
        if row < 4 or column < 4:
            print("The board has to be at least 4 by 4")
        else:
            break

    board = initializeBoard(row, column)
    printBoard(board)

    print('GAME MODE')
    print('1: Player VS Computer')
    print('2: Player1 VS Player 2')
    print('3: Exit')
    mode = pickMode()
    if mode == 1:
        vsComputer(board, row, column)
    elif mode == 2:
        vsHuman(board, row, column)
    else:
        print('Game Ends')


if __name__ == '__main__':
    welcomeMessage()
    gameMode()


