def sudoku_grid_correct(sudoku):
    for row in sudoku:
        state = row_correct

def row_correct(sudoku, row_no):
    store = []
    for column in sudoku[row_no]:
        if column == 0:
            continue
        if column not in store and column:
            store.append(column)
        else:
            return False
    return True

def column_correct(sudoku, column_no):
    store = []
    for row in sudoku:
        number = row[column_no]
        if number in store and number > 0:
            return False
        else:
            store.append(number)
    return True

def block_correct(sudoku, row_no, column_no):
    store = []
    for row in range(row_no, row_no + 3):
        for column in range(column_no, column_no + 3):
            if sudoku[row][column] in store and sudoku[row][column] > 0:
                return False
            else:
                store.append(sudoku[row][column])
    return True

