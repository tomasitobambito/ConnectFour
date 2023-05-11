import helper

board = [['.'] * 6 for i in range(7)]
player = True
depth = 1000

while True:
    helper.print_board(board)

    while True:
        if player:
            # verify player input
            while True:
                columnId = int(input("Choose the column you want to play: "))
                
                if 0 <= columnId <= 6:
                    break
                
                print("Choose a valid integer column")
            
        else:
            columnId = helper.generate_computer_move(board, depth)

        # check if move is legal
        try:
            helper.drop_disc(board, columnId, player)
            break
        except ValueError:
            print("That move is not valid")

    if helper.is_board_full(board):
        helper.print_board(board)
        print("The board is full, it is a tie")
        break
    
    if helper.detect_four(board):
        helper.print_board(board)
        print("Congrats you beat the AI" if player else "Congrats you lost to your new overlord")
        break

    player = not player
    print(columnId, "was played")


