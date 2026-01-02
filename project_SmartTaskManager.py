#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
import re

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validate_priority(priority):
    if priority not in ["low", "medium", "high"]:
        raise ValueError("Priority must be low, medium, or high")
    return priority

def create_task():
    try:
        email = input("Enter your email: ")
        if not validate_email(email):
            raise ValueError("Invalid email format")

        task_name = input("Enter task name: ")
        if task_name.strip() == "":
            raise ValueError("Task name cannot be empty")

        priority = input("Enter priority (low/medium/high): ").lower()
        validate_priority(priority)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        task = f"{email} | {task_name} | {priority} | {timestamp}\n"

        save_task(task)
        print("Task created and logged successfully")

    except ValueError as e:
        print("Error:", e)

def save_task(task):
    with open("task_log.txt", "a") as file:
        file.write(task)

def view_tasks():
    try:
        with open("task_log.txt", "r") as file:
            print("\n--- TASK LOG ---")
            print(file.read())
    except FileNotFoundError:
        print("No tasks found yet")

while True:
    print("\n1. Create Task")
    print("2. View Task Log")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        create_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        break
    else:
        print("Invalid option")


# In[ ]:




