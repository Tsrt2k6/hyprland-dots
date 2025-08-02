def play_turn(game_board, x, y, piece):
    if not 0 <= x <= 2 or not 0 <= y <= 2:
        return False
    if game_board[y][x]:
        return False
    else:
        game_board[y][x] = piece
        return True