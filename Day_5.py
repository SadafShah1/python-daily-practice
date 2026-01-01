#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = int(input("Enter a number: "))
print(num)


# In[2]:


try:
    num = int(input("Enter a number: "))
    print(num)
except:
    print("Invalid input")


# In[3]:


try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Only numbers are allowed")


# In[4]:


try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Error")
else:
    print("You entered:", num)
finally:
    print("Program finished")


# In[ ]:




