def sudoku_grid_correct(sudoku):


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

