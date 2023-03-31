import os 

import random 

  

empty = [[" ", " ", " "], 

         [" ", " ", " "], 

         [" ", " ", " "]] 

  

board = [[" ", " ", " "], 

         [" ", " ", " "], 

         [" ", " ", " "]] 

  

def print_introduction(): 

    print("Welcome to Tic Tac Toe!") 

  

def clear_board(): 

    global board 

    board = empty 

  

def print_board(): 

    os.system('clear') 

    for row in board: 

        for box in row: 

            print(f"[{box}]", end=" ") 

        print() 

  

def make_move(x, y, xo): 

    if x not in range(3) or y not in range(3): 

        raise Exception("Invalid coordinates! Enter values between 0 and 2.") 

    if board[x][y] != " ": 

        raise Exception("Box is not empty!") 

    board[x][y] = xo 

    print_board() 

  

def flip_coin(): 

    print("\n\nFlipping coin to determine who goes first!") 

    n = random.randint(0, 1) 

    input() 

    if n == 1: 

        print("Heads wins!") 

    else: 

        print("Tails wins") 

  

def is_win(): 

    win = False 

    # check for horizontal 

    for i in range(3): 

        if board[i][0] == board[i][1] == board[i][2] != " ": 

            return True 

  

    # check for vertical 

    for i in range(3): 

        if board[0][i] == board[1][i] == board[2][i] != " ": 

            return True 

  

    # check for diagonal 

    if board[0][0] == board[1][1] == board[2][2] != " ": 

        return True 

    if board[0][2] == board[1][1] == board[2][0] != " ": 

        return True 

         

    return False 

  

def is_draw(): 

    for row in board: 

        if " " in row: 

            return False 

    return True 

  

def main(): 

    print_introduction() 

    flip_coin() 

    player = "x" 

    while True:   

        inputs = input("Enter coordinates separated by space (0-2) (0-2): ").split(" ") 

        x = int(inputs[0]) 

        y = int(inputs[1]) 

         

        try: 

            make_move(x, y, player) 

        except Exception as e: 

            print(e) 

            continue 

             

        if is_win(): 

            print(f"Player {player} wins!") 

            break 

             

        if is_draw(): 

            print("It's a draw!") 

            break 

             

        if player == "x": 

            player = "o" 

        else: 

            player = "x" 

  

if __name__ == "__main__": 

    main() 

 

 

 

 




