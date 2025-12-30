#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Personal Expense Tracker

expenses = []

def add_expense():
    title = input("Enter expense title: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/Study/etc): ")

    expenses.append({
        "title": title,
        "amount": amount,
        "category": category
    })
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses added yet.\n")
        return

    print("\nYour Expenses:")
    for exp in expenses:
        print(exp["title"], "-", exp["amount"], "-", exp["category"])
    print()

def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print("Total Expense:", total, "\n")

def save_to_file():
    file = open("expenses.txt", "w")
    for exp in expenses:
        line = f'{exp["title"]},{exp["amount"]},{exp["category"]}\n'
        file.write(line)
    file.close()
    print("Expenses saved to file.\n")

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Save & Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        save_to_file()
        print("Thank you for using Expense Tracker")
        break
    else:
        print("Invalid choice\n")


# In[ ]:




