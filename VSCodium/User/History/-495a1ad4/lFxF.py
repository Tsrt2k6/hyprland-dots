def print_sudoku(sudoku):
    for row in range(9):
        for column in range(9):
            if sudoku[row][column] > 0:
                print(f"{sudoku[row][column]} ", end="")
            else:
                print("_ ", end="")
            if column % 3 == 0 and column > 0:
                print(" ", end="")
        print("")
        if row % 3 == 0 and column > 0:
            print("")
            

def add_number(sudoku):
    pass


sudoku  = [
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print_sudoku(sudoku)
