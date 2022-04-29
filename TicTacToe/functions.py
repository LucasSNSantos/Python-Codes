
#functio that creates the board of the game
def create_matrix():
    matrix = []
    for i in range(3):
        line = []
        for j in range(3):
            line += [" "]
        matrix += [line]
    return matrix


#printing the board
def print_matrix(matrix):
    print()
    for i in range(3):
        for j in range(3):
            print("| ", end="")
            print(matrix[i][j], end="")
            print(" |", end="")
        print()
    print()    

#checking the valid positon of the board
def check_valid_position(line,column, matrix):
    p_line = int(line)
    p_col = int(column)
    value = matrix[p_line][p_col]
    if(value == "X" or value == "O"):
        return False
    else:
        return True    


#put a piece on board
def put_piece_on_board(line, column, matrix, piece):
    if piece != "X" and piece != "O":
        return False
    if check_valid_position(line,column,matrix):
        p_line = int(line)
        p_col = int(column)
        matrix[p_line][p_col] = piece
        return True
    else:
        return False


#check the win conditions to see if the game is over
def check_win_game(matrix):
    left = ((matrix[0][0] == matrix[1][0] == matrix[2][0]) and 
    (matrix[0][0] != " " and
     matrix[1][0] != " " and
     matrix[2][0] != " "
    ))
    right = ((matrix[0][2] == matrix[1][2] == matrix[2][2]) and
    (   matrix[0][2] != " " and 
        matrix[1][2] != " " and
        matrix[2][2] != " " 
    ))
    top = ((matrix[0][0] == matrix[0][1] == matrix[0][2]) and 
    (matrix[0][0] != " " and
     matrix[0][1] != " " and 
     matrix[0][2] != " "
    ))
    bottom = ((matrix[2][0] == matrix[2][1] == matrix[2][2]) and
    (matrix[2][0] != " "and
     matrix[2][1] != " " and
     matrix[2][2] != " "
    ))
    diag_1 = ((matrix[0][0] == matrix[1][1] == matrix[2][2]) and
    (matrix[0][0] != " " and
     matrix[1][1] != " " and
     matrix[2][2] != " "
    ))
    diag_2 = ((matrix[0][2] == matrix[1][1] == matrix[2][0]) and
    (matrix[0][2] != " " and 
     matrix[1][1] != " " and
     matrix[2][0] != " "
     ))

    if left or right or top or bottom or diag_1 or diag_2:
        return True
    else:
        return False































