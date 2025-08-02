def block_correct(sudoku, row_no, column_no):
    store = []
    for row in range(row_no, row_no + 3):
        for column in range(column_no, column_no + 3):
            if sudoku[row][column] in store and sudoku[row][column] > 0:
                return False
            else:
                store.append(sudoku[row][column])
    return True

