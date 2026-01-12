# ATM Withdrawal Program

balance = 10000

print("Welcome to ATM")

try:
    amount = int(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Amount must be greater than zero")

    elif amount > balance:
        print("Insufficient balance")

    else:
        balance -= amount
        print(f"Withdrawal successful. Remaining balance: {balance}")

except ValueError:
    print("Please enter numbers only")

except Exception as error:
    print("Something went wrong:", error)

finally:
    print("Thank you for using ATM")

