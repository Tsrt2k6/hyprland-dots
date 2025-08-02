def row_correct(sudoku, row_no):
    for row in sudoku:
        store = []
        for column in sudoku:
            if column not in store:
                store.append(column)
            else:
                return False
    return True