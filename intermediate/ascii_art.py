from pyfiglet import figlet_format
from termcolor import cprint, COLORS

text = input("What message do you want to print? ")
color = input("What color? ")

while color not in COLORS:
    print(f"Valid colors: {', '.join(COLORS)}")
    color = input("Please enter a valid color: ")

cprint(figlet_format(text), color)
