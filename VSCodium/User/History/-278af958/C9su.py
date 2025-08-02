def who_won(board):
    one_count = 0
    two_count = 0
    for row in board:
        for column in row:
            if column == 1:
                one_count += 1
            elif column == 2:
                two_count += 1
    if one_count > two_count:
        return 1
    elif two_count > one_count:
        return 2
    else:
        return 0