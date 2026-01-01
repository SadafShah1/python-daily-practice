#!/usr/bin/env python
# coding: utf-8

# In[1]:


users = []

def register_user():
    try:
        username = input("Enter username: ")
        if username == "":
            raise ValueError("Username cannot be empty")

        email = input("Enter email: ")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format")

        age = int(input("Enter age: "))
        if age < 18:
            raise ValueError("Age must be 18 or above")

        user = {
            "username": username,
            "email": email,
            "age": age
        }

        users.append(user)
        print("User registered successfully")

    except ValueError as e:
        print("Error:", e)


def view_users():
    if not users:
        print("No users registered yet")
        return

    for user in users:
        print("Username:", user["username"])
        print("Email:", user["email"])
        print("Age:", user["age"])
        print("------")


while True:
    print("\n1. Register User")
    print("2. View Users")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        register_user()
    elif choice == "2":
        view_users()
    elif choice == "3":
        break
    else:
        print("Invalid choice")


# In[ ]:




