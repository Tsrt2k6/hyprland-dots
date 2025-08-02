def print_sudoku(sudoku):
    new = sudoku[:]
    for row in range(9):
        for column in range(9):
            if new[row][column] > 0:
                print(f"{new[row][column]} ", end="")
            else:
                print("_ ", end="")

            if (column + 1) % 3 == 0 and column > 0:
                print(" ", end="")

        print("")
        if (row + 1) % 3 == 0 and row > 0:
            print("")

