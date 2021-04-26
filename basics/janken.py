print("Rock...\nPaper...\nScissors!!!")
player1 = input("Player 1, make your move: ").lower()
player2 = input("Player 2, make your move: ").lower()

if player1 not in ["rock", "paper", "scissors"]:
    print("Player 1 has an invalid input!!!")
elif player2 not in ["rock", "paper", "scissors"]:
    print("Player 2 has an invalid input!!!")
elif player1 == player2:
    print("It's a draw!!!")
elif player1 == "rock":
    if player2 == "scissors":
        print("Player 1 wins!!!")
    else:
        print("Player 2 wins!!!")
elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 wins!!!")
    else:
        print("Player 2 wins!!!")
else:
    if player2 == "paper":
        print("Player 1 wins!!!")
    else:
        print("Player 2 wins!!!")
