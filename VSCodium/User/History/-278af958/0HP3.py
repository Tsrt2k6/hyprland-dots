def who_won(board):
    one_count = 0
    two_count = 0
    for row in board:
        for column in row:
            if column == 1:
                one_count += 1
            elif column == 2:
                two_count += 1
            