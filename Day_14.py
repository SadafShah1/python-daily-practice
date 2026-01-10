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

