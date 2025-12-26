from player import HumanPlayer
from board import GameBoard

# Initialize players
player1 = HumanPlayer("X")
player2 = HumanPlayer("O")

# Initialize board
board = GameBoard()

# Game loop
current_player = player1
while True:
    board.print_board()
    pos = current_player.make_move(board)

    if board.place_symbol(current_player, pos):
        if board.check_winner(current_player, pos):
            board.print_board()
            print(f"Congrats! Player {current_player.get_symbol()} wins!")
            break
        # Switch player
        current_player = player2 if current_player == player1 else player1
    else:
        print("Invalid move! Try again.")
