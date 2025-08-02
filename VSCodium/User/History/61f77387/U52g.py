def row_correct(sudoku, row_no):
    for column in sudoku[row_no]:
        if column not in store:
            store.append(column)
        else:
            return False
    return True