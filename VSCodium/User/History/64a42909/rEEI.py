def transpose(matrix):
    new = []
    for column in range(len(matrix)):
        nest = []
        for row in range(len(matrix)):
            nest.append(matrix[row][column])
        new.append(nest)

    for row in range(len(matrix)):
        for column in range(len(matrix)):
            matrix[row][column] = new[row][column]

store = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
transpose(store)
print(store)