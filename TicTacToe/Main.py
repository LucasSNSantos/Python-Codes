import functions as fc
import os

board = fc.create_matrix()
player_input = ""
line_axis = ""
column_axis = ""
turn_icon = "X"
winner_icon = ""
game_over = False
valid_position = False

print("Tic Tac Toe for Noobies")
print()
print("Press any button to Start game")
print("2 -  Exit")

player_input = input()

if player_input == "2":
    quit()
else:
    while game_over is False:
        os.system('cls')
        print("Round " + turn_icon)
        fc.print_matrix(board)
        print()
        print("Put the line and column")
        valid_position = False
        while valid_position is False:
            line_axis = input()
            column_axis = input()
            valid_position = fc.check_valid_position(line_axis,column_axis,board)
            if valid_position is True:
                fc.put_piece_on_board(line_axis,column_axis,board,turn_icon)
                winner_icon = turn_icon
                if turn_icon == "X":
                    turn_icon = "O"
                else:
                    turn_icon = "X"
            game_over = fc.check_win_game(board)



os.system('cls')
print("The Winner is the player: " + winner_icon)

            
















