# Easy Rock Paper Scissors """""AI""""" in two simple steps:
from random import choice

player_score = 0
com_score = 0
winning_score = 3

while player_score < winning_score and com_score < winning_score:
    print(f"Player {player_score} - {com_score} COM")
    print("Rock...\nPaper...\nScissors!!!")
    player = input("Make your move: ").lower()

    while player not in ["rock", "paper", "scissors", "quit"]:
        player = input("Please enter a valid move: ")

    if player == "quit":
        print("Quitting the game...")
        break

    com = choice(["rock", "paper", "scissors"])
    print(f"COM plays: {com}")

    if player == com:
        print("It's a draw!")
    elif player == "rock":
        if com == "scissors":
            print("You score a point!")
            player_score += 1
        else:
            print("COM scores a point!")
            com_score += 1
    elif player == "paper":
        if com == "rock":
            print("You score a point!")
            player_score += 1
        else:
            print("COM scores a point!")
            com_score += 1
    else:
        if com == "paper":
            print("You score a point!")
            player_score += 1
        else:
            print("COM scores a point!")
            com_score += 1

print(f"Player {player_score} - {com_score} COM")
if player_score > com_score:
    print("You win!!!")
elif com_score > player_score:
    print("COM wins!!!")
else:
    print("It's a draw!!!")
