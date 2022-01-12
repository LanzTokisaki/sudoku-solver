GRID_SIZE = 9

board = [
    [0, 5, 0, 6, 0, 9, 7, 2, 8],
    [8, 6, 0, 7, 0, 2, 4, 1, 0],
    [9, 2, 7, 4, 0, 8, 0, 0, 0],
    [7, 0, 0, 0, 2, 3, 0, 6, 0],
    [0, 3, 0, 0, 9, 7, 1, 5, 0],
    [2, 0, 0, 5, 0, 0, 3, 0, 0],
    [3, 0, 8, 0, 6, 5, 2, 0, 1],
    [6, 0, 9, 2, 0, 1, 0, 7, 0],
    [5, 1, 0, 3, 0, 0, 0, 8, 6]
]


def isNumberInRow(number: int, row: int) -> bool:
    for column in range(GRID_SIZE):
        if board[row][column] == number:
            return True
    
    return False 


def isNumberInColumn(number: int, column: int) -> bool:
    for row in range(GRID_SIZE):
        if board[row][column] == number:
            return True
    
    return False 


def isNumberInBox(number: int, row: int, column: int) -> bool:
    localBoxRow = row - row % 3
    localBoxColumn = column - column % 3

    i = localBoxRow
    j = localBoxColumn

    while i < localBoxRow + 3:
        while j < localBoxColumn + 3:
            if board[i][j] == number:
                return True
            j += 1
        i += 1
    
    return False


def isValidPlacement(number: int, row: int, column: int) -> bool:
    return not isNumberInRow(number, row) and \
        not isNumberInColumn(number, column) and \
        not isNumberInBox(number, row, column)
    

def solveBoard():
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            if board[row][column] == 0:
                for i in range(GRID_SIZE):
                    numberToTry = i + 1
                    if isValidPlacement(numberToTry, row, column):
                        board[row][column] = numberToTry

                        if solveBoard(): 
                            return True
                        else:
                            board[row][column] = 0

                return False
    
    return True


def printBoard():
    for row in range(GRID_SIZE):
        if row % 3 == 0 and row != 0:
            print("-----------")

        column_text = ""

        for column in range(GRID_SIZE):
            if column % 3 == 0 and column != 0:
                column_text += "|"
            column_text += str(board[row][column])
        
        print(column_text)
            

def main():
    if solveBoard():
        print("Solved Successfully!")
    else:
        print("Unsolvable board!")

    printBoard()


if __name__ == "__main__":
    main()
