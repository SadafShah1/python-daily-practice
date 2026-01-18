import expense_utils

expenses = []

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

   choice = input("Choose: ")

    if choice == "1":
        amount = int(input("Amount: "))
        category = input("Category: ")
        expense_utils.add_expense(expenses, amount, category)
