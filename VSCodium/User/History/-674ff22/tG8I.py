def column_correct(sudoku, column_no):
    store = []
    for row in sudoku:
        number = row[column_no]
        if number in store and number > 0:
            return False
        else:
            store.append(number)
    return True
