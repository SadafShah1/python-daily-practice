import os

FILE_NAME = "books.txt"


def load_books():
    books = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                title, author, status = line.strip().split("|")
                books.append({
                    "title": title,
                    "author": author,
                    "status": status
                })
    return books
  def save_books(books):
    with open(FILE_NAME, "w") as f:
        for b in books:
            f.write(f"{b['title']}|{b['author']}|{b['status']}\n")


def add_book(books):
    title = input("Book title: ")
    author = input("Author: ")

    books.append({
        "title": title,
        "author": author,
        "status": "available"
    })
