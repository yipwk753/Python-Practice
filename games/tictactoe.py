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

def processinput(input):
    pass

board_dict = {
    1: [0,0],
    2: [0,1],
    3: [0,2],
    4: [1,0],
    5: [1,1],
    6: [1,2],
    7: [2,0],
    8: [2,1],
    9: [2,2]
}
game_over = False
game_in_process = True
wins = losses = ties = 0
user_choice = "x"
computer_choice = "o"
rows, cols = (3, 3)

while game_over is not False:
    board = [[" " for x in range(cols)] for x in range(rows)]

    goes_first = random.choice(("user", "computer"))
    if goes_first == "user":
        position = input("Choose between 1 and 9.\n")
        while position not in range(1, 10):
            position = input("Please choose a correct response.\n")
    else:
        position = random.choice(range(1, 10))
        i, j = board_dict.get(position)
        board[i][j] = computer_choice
    game_over = True

    printboard(board)

    while game_in_process:
        continue here