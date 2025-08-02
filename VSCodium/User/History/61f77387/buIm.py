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

