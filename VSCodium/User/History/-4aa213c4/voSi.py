def sudoku_grid_correct(sudoku):
    for row_no in range(len(sudoku)):
        if not row_correct(sudoku, row_no):
            return False
    for column_no in range(len(sudoku[0])):
        if not column_correct(sudoku, column_no):
            return False
    block_list = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for block in block_list:
        if not block_correct(sudoku, block[0], block[1]):
            return False
    return True

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


