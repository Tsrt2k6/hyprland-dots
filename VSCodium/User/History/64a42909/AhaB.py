def transpose(matrix):
    new = []
    for column in range(len(matrix)):
        for row in range(len(matrix)):
            new.append(matrix[row][column])
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            matrix[row][column] = new[row][column]

store = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
transpose(store)
print(store)