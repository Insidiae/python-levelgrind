age = input("How old are you? ")

if not age:
    print("You can't enter if you don't tell me your age!!!")
if not age.isnumeric():
    print("?!?!?!")
else:
    age = int(age)
    if age >= 21:
        print("You are good to enter and can drink!")
    elif age >= 18:
        print("You can enter, but you need a wristband!")
    else:
        print("You can't come in, little one! :^(")
