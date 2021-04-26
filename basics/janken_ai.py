# Easy Rock Paper Scissors """""AI""""" in two simple steps:
from random import choice
com = choice(["rock", "paper", "scissors"])

print("Rock...\nPaper...\nScissors!!!")
player = input("Make your move: ").lower()

print(f"COM plays: {com}")

if player == com:
    print("It's a draw!!!")
elif player == "rock":
    if com == "scissors":
        print("You win!!!")
    else:
        print("COM wins!!!")
elif player == "paper":
    if com == "rock":
        print("You win!!!")
    else:
        print("COM wins!!!")
elif player == "scissors":
    if com == "paper":
        print("You win!!!")
    else:
        print("COM wins!!!")
else:
    print("You have an invalid input!!!")
