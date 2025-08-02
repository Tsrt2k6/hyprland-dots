def play_turn(game_board, x, y, piece):
    if game_board[y][x]:
        return False
    else:
        game_board[y][x] == piece
        return True