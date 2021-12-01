import sqlite3
import requests
from bs4 import BeautifulSoup


def get_title(book):
    return book.find("h3").find("a")["title"]


def get_price(book):
    price = book.select(".price_color")[0].get_text()
    price = float(price.replace("£", "").replace("Â", ""))
    return price


def get_rating(book):
    RATING_VALUES = {
        "Zero": 0,
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5}

    rating = book.select(".star-rating")[0].get_attribute_list("class")[1]
    return RATING_VALUES[rating]


def save_books(books):
    connection = sqlite3.connect("files/books.db")
    c = connection.cursor()

    # You can also manually create the books table using sqlite3
    # c.execute("CREATE TABLE books (title TEXT, price REAL, rating INTEGER)")

    c.executemany("INSERT INTO books VALUES (?, ?, ?)", books)

    connection.commit()
    connection.close()


def scrape_books(url):
    res = requests.get(url)

    soup = BeautifulSoup(res.text, "html.parser")
    books = soup.find_all(class_="product_pod")

    # all_books = []
    # for book in books:
    #     book_data = (get_title(book), get_price(book), get_rating(book))
    #     all_books.append(book_data)

    all_books = [(get_title(book), get_price(book), get_rating(book))
                 for book in books]
    save_books(all_books)


if __name__ == "__main__":
    BASE_URL = "https://books.toscrape.com/catalogue/category/books/history_32/index.html"
    scrape_books(BASE_URL)
