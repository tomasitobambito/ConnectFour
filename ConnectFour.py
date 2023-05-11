import helper

board = [['.'] * 6 for i in range(7)]
player = True

while True:
    helper.print_board(board)

    while True:
        columnId = int(input("Choose a column: ")) if player else helper.generate_computer_move(board)

        try:
            helper.drop_disc(board, columnId, player)
            break
        except ValueError:
            if player:
                print("That move is not valid")

    if helper.is_board_full(board):
        helper.print_board(board)
        print("The board is full, it is a tie")
        break
    
    if helper.detect_four(board):
        helper.print_board(board)
        print("some fuck won idk")
        break

    player = not player
    print(columnId, "was played")


