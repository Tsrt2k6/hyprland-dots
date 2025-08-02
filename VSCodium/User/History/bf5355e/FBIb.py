def play_turn(game_board, x, y, piece):
    if game_board[y][x] or 0 <= x <= 2 or 0 <= y <= 2:
        return False
    else:
        game_board[y][x] = piece
        return True