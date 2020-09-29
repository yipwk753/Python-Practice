import random
choices = ["Rock" , "Paper", "Scissors"]
game_over = False
draw = 0
wins = 0
loss = 0
while game_over is not True:
    user_choice = input("What is your choice: Rock, Paper, or Scissors?\n")
    if user_choice.capitalize() not in choices:
        print("Please pick a correct choice.")
        continue
    opponent_choice = random.choice(choices)
    user_choice = user_choice.lower()
    opponent_choice = opponent_choice.lower()
    if user_choice == opponent_choice:
        draw += 1
        print(f"You both chose {user_choice}.  Draw.")
    elif (
        user_choice == "rock" and opponent_choice == "scissors"
        or user_choice == "paper" and opponent_choice == "rock"
        or user_choice == "scissors" and opponent_choice == "paper"):
            wins += 1
            print(f"You chose {user_choice} and your opponent chose {opponent_choice}.  You win.")
    elif (
        user_choice == "scissors" and opponent_choice == "rock"
        or user_choice == "rock" and opponent_choice == "paper"
        or user_choice == "paper" and opponent_choice == "scissors"):
            loss += 1
            print(f"You chose {user_choice} and your opponent chose {opponent_choice}.  You lose.")
    print()
    answer = input("Do you want to play again? Yes/No\n")
    if (answer.lower() in ("yes", "y")):
        continue
    elif (answer.lower() in ("no", "n")):
        game_over = True
print(f"You won {wins} time(s).")
print(f"You lost {loss} time(s).")
print(f"You tied {draw} time(s).")