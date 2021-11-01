from random import choice
from termcolor import cprint
from pyfiglet import figlet_format
import requests

cprint(figlet_format("Dad Joke 3000"), "magenta")

topic = input("Let me tell you a joke! Give me a topic: ")


url = "https://icanhazdadjoke.com/search"
payload = {"term": topic}
headers = {"Accept": "application/json"}

res = requests.get(url, params=payload, headers=headers)

data = res.json()

if data["total_jokes"] > 1:
    print(
        f"I've got {data['total_jokes']} jokes about \"{topic}\". Here's one:"
    )
    print(choice(data["results"])["joke"])
elif data["total_jokes"] == 1:
    print(
        f"I've got one joke about \"{topic}\":"
    )
    print(choice(data["results"])["joke"])
else:
    print(f"Sorry, I don't have any jokes about \"{topic}\". Try again!")
