from random import randint

while True:
    random_number = randint(1, 10)
    guess = None
    while guess != random_number:
        guess = input("Guess a number between 1 and 10: ")
        while not guess.isnumeric():
            guess = input("Please input a valid number: ")
        guess = int(guess)
        if guess > random_number:
            print("Too high, try again!")
        elif guess < random_number:
            print("Too low, try again!")
        else:
            print("You guessed it! You won!")

    keep_playing = input("Do you want to keep playing? (y/n): ").lower()
    while keep_playing != "y" and keep_playing != "yes" and keep_playing != "n" and keep_playing != "no":
        keep_playing = input("Do you want to keep playing? (y/n): ").lower()

    if keep_playing == "n" or keep_playing == "no":
        break

print("Thanks for playing. Bye!")
