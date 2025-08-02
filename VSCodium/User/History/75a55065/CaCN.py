def block_correct(sudoku, row_no, column_no):
    store = []
    for row in range(row_no, row_no + 3):
        for column in range(column_no, column_no + 3):
            if column in store and column:
                return False
            else:
                store.append(column)
            