from random import randint

def print_board(board):
    """Prints connect 4 board to the command line

    Args:
        board (ndarray): 2D list containing the connect 4 board
    """

    for i in range(len(board[0])):
        string = ''
        for j in range(len(board)):
            string += board[j][i] + ' '

        print(string)
    
    print('0 1 2 3 4 5 6')

def drop_disc(board, columnid, player):
    """Modifies board list to insert a new disc in a specific column.

    Args:
        board (ndarray): 2D list containing the connect 4 board.
        columnid (int): ID of the column being modified.
        player (bool): Boolean to determine whether the player is playing or the computer is playing.

    Raises:
        ValueError: Error raised when column is full.
    """
    symbol = "X" if player else "O"

    # check if selected colum is full
    if board[columnid][0] != ".":
        raise ValueError("Invalid move")
            
    for i in range(1, len(board[columnid]) + 1):
        if board[columnid][-i] == ".":
            board[columnid][-i] = symbol
            break

def is_board_full(board):
    """Checks if the board is completly filled.

    Args:
        board (ndarray): 2D list containing the connect 4 board.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    for column in board:
        for entry in column:
            if entry == ".":
                return False
            
    return True

def generate_computer_move(board):
    """Calculates the best move based on the current board.

    Args:
        board (ndarray): 2D list containing the connect 4 board.

    Returns:
        int: The ID of the column that the AI chooses to play.
    """
    return randint(0,6)

