#!/usr/bin/env python
# coding: utf-8

# In[1]:


def create_profile(name, age, field):
    return {
        "name": name,
        "age": age,
        "field": field
    }

students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        field = input("Enter field: ")

        students.append(create_profile(name, age, field))
        print("Student added")

    elif choice == "2":
        for s in students:
            print(s)

    elif choice == "3":
        break


# In[ ]:




