def column_correct(sudoku, column_no):
    store = []
    for row in sudoku:
        number = row[column_no]
        if number in store and number > 0:
            return False
        return True


sudoku = [
  [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],   # rivi 0
  [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],   # rivi 1
  [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],   # rivi 2
  [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],   # rivi 3
  [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],   # rivi 4
  [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],   # rivi 5
  [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],   # rivi 6
  [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],   # rivi 7
  [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],   # rivi 8
]

print(column_correct(sudoku, 0))