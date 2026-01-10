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
