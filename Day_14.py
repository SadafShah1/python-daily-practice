expenses = []


def add_expense():
    title = input("Enter expense title: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "title": title,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added successfully\n")

def view_expenses():
    if not expenses:
        print("No expenses found\n")
        return

    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['title']} - {e['amount']} ({e['category']})")
    print()


def total_expense():
    total = sum(e["amount"] for e in expenses)
    print(f"Total Expense: {total}\n")


def search_by_category():
    cat = input("Enter category to search: ")

found = False
    for e in expenses:
        if e["category"].lower() == cat.lower():
            print(f"{e['title']} - {e['amount']}")
            found = True

    if not found:
        print("No expenses in this category\n")
    else:
        print()


while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Search by Category")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        search_by_category()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option\n")
