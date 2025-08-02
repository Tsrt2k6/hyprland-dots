def print_sudoku(sudoku):
    for row in sudoku:
        for column in sudoku[row]:
            if column > 0:
                print(column)
            else:
                print("_")
        print("")
            

def add_number(sudoku):
    pass