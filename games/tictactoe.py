import random

def printboard(board):
    b = (
        f"{board[0][0]}|{board[0][1]}|{board[0][2]}\n"
        f"- - -\n"
        f"{board[1][0]}|{board[1][1]}|{board[1][2]}\n"
        f"- - -\n"
        f"{board[2][0]}|{board[2][1]}|{board[2][2]}"
        )
    print(b)

def checkboard(board, input):
    if (
        board[0][0] == board[0][1] == board[0][2] == input
        or board[1][0] == board[1][1] == board[1][2] == input
        or board[2][0] == board[2][1] == board[2][2] == input
        or board[0][0] == board[1][0] == board[2][0] == input
        or board[0][1] == board[1][1] == board[2][1] == input
        or board[0][2] == board[1][2] == board[2][2] == input
        or board[0][0] == board[1][1] == board[2][2] == input
        or board[0][2] == board[1][1] == board[2][0] == input
    ):
        return True
    else:
        return False

board_dict = {
    "1": [0,0],
    "2": [0,1],
    "3": [0,2],
    "4": [1,0],
    "5": [1,1],
    "6": [1,2],
    "7": [2,0],
    "8": [2,1],
    "9": [2,2]
}
game_over = False
game_in_process = True
wins = losses = ties = 0
user_choice = "x"
computer_choice = "o"
rows, cols = (3, 3)

while game_over is not True:
    board = [[" " for x in range(cols)] for x in range(rows)]
    open_spots = [str(i) for i in list(range(1,10))]

    goes_first = random.choice((0, 1))
    while game_in_process:
        if goes_first == 0:
            position = input(f"Choose one of these numbers: {open_spots}\n")
            while position.isnumeric() == False or position not in open_spots:
                position = input(f"Please choose a correct response: {open_spots}\n")

            i, j = board_dict.get(position)
            open_spots.remove(position)
            board[i][j] = user_choice
            printboard(board)            
            game_won = checkboard(board, user_choice)
            if game_won:
                wins +=1
                game_in_process = False
                print("You won.")
            elif len(open_spots) == 0:
                ties +=1
                game_in_process = False
                print("You tied.")
            goes_first = 1
        else:
            position = str(random.choice(open_spots))
            i, j = board_dict.get(position)
            open_spots.remove(position)
            board[i][j] = computer_choice
            printboard(board)
            game_won = checkboard(board, computer_choice)
            if game_won:
                losses += 1
                game_in_process = False
                print("You lost.")
            elif len(open_spots) == 0:
                ties +=1
                game_in_process = False
                print("You tied.")
            goes_first = 0
        print()
    answer = input("Do you want to play again? Yes/No or y/n\n")
    while answer.lower() not in ("yes", "y", "no", "n"):
        answer = input("Please input a correct choice: Yes/No or y/n\n")
    if (answer.lower() in ("yes", "y")):
        game_in_process = True
    else:
        game_over = True
print(f"You won {wins} time(s).")
print(f"You lost {losses} time(s).")
print(f"You tied {ties} time(s).")