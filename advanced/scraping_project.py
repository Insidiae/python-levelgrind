import requests
from bs4 import BeautifulSoup
from random import choice


def scrape_quotes():
    BASE_URL = "https://quotes.toscrape.com"
    url = "/page/1"
    fetched_quotes = []

    while url:
        res = requests.get(BASE_URL + url)
        current_page = BeautifulSoup(res.text, features="html.parser")
        quotes = current_page.find_all(class_="quote")

        for quote in quotes:
            fetched_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "href": BASE_URL + quote.find("a")["href"]
            })

        next_page_link = current_page.find(class_="next")
        url = next_page_link.find("a")["href"] if next_page_link else None

    print(f"Fetched {len(fetched_quotes)} quotes.\n")
    return fetched_quotes


def start_game(quote_data):
    should_continue = "y"
    while should_continue in ("y", "yes"):
        random_quote = choice(quote_data)
        author_res = requests.get(random_quote["href"])
        author_details = BeautifulSoup(author_res.text, features="html.parser")

        author_name = random_quote["author"]
        author_born_date = author_details.find(
            class_="author-born-date").get_text()
        author_born_location = author_details.find(
            class_="author-born-location").get_text()

        print(f"Here's a quote:\n\n{random_quote['text']}\n")

        hints = [
            f"Sorry, you've run out of guesses. The answer was {author_name}.\n",
            f"Here's a hint: The author's last name starts with {author_name.split()[-1][0]}\n",
            f"Here's a hint: The author's first name starts with {author_name[0]}\n",
            f"Here's a hint: The author was born in {author_born_date} {author_born_location}.\n"]

        for i in range(4, 0, -1):
            guess = input(f"Who said this? Guesses remaining: {i}. ")

            if guess.lower() == author_name.lower():
                print("You guessed correctly! Congratulations!")
                break
            else:
                print(hints[i - 1])

        should_continue = input("Would you like to play again (y/n)? ")
        while should_continue not in ("y", "n", "yes", "no"):
            should_continue = input("Would you like to play again (y/n)? ")

    print("Ok! See you next time!")


print("Loading quotes...")
quote_data = scrape_quotes()
start_game(quote_data)
