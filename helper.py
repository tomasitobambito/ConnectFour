def print_board(board):
    for i in range(len(board[0])):
        string = ''
        for j in range(len(board)):
            string += board[j][i] + ' '

        print(string)

def drop_disc(board, columnid, player):
    symbol = "X" if player else "O"

    # check if selected colum is full
    while True:
        for entry in board[columnid]:
            if entry == '.':
                break

        raise ValueError("Invalid move")

    #

    