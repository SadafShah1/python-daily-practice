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
save_books(books)
    print("Book added successfully\n")


def view_books(books):
    if not books:
        print("No books available\n")
        return

    for i, b in enumerate(books, start=1):
        print(f"{i}. {b['title']} by {b['author']} [{b['status']}]")
    print()
def search_book(books):
    title = input("Enter book title to search: ").lower()

    for b in books:
        if b["title"].lower() == title:
            print(f"Found: {b['title']} by {b['author']} [{b['status']}]\n")
            return

    print("Book not found\n")
def borrow_book(books):
    title = input("Enter book title to borrow: ").lower()

    for b in books:
        if b["title"].lower() == title:
            if b["status"] == "available":
                b["status"] = "borrowed"
                save_books(books)
                print("Book borrowed successfully\n")
            else:
                print("Book already borrowed\n")
            return

    print("Book not found\n")

def return_book(books):
    title = input("Enter book title to return: ").lower()

    for b in books:
        if b["title"].lower() == title:
            b["status"] = "available"
            save_books(books)
            print("Book returned successfully\n")
            return

    print("Book not found\n")


def main():
    books = load_books()

    while True:
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            borrow_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            break
        else:
            print("Invalid choice\n")


main()
