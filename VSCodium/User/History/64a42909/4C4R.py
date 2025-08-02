def transpose(matrix):
    new = []
    for column in range(len(matrix)):
        nest = []
        for row in range(len(matrix)):
            nest.append(matrix[row][column])
        new.append(nest)

    matrix[:] = new

