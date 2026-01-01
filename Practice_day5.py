#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Practice 1: Number input validation

try:
    age = int(input("Enter your age: "))
    print("Age:", age)
except ValueError:
    print("Invalid age input")


# In[2]:


# Practice 2: Division with error handling

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")


# In[ ]:




