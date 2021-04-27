for x in range(1, 21):
    if x == 4 or x == 13:
        adjective = "unlucky"
    elif x % 2 == 0:
        adjective = "even"
    else:
        adjective = "odd"
    print(f"{x} is {adjective}")
