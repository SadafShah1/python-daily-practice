#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

print(math.sqrt(16))
print(math.pi)


# In[2]:


from math import sqrt

print(sqrt(25))


# In[3]:


from datetime import datetime

now = datetime.now()
print(now)


# In[4]:


print(now.strftime("%Y-%m-%d %H:%M:%S"))


# In[5]:


import re

email = "test@gmail.com"

if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Valid email")
else:
    print("Invalid email")


# In[6]:


def square(n):
    return n * n

result = square(4)


# In[ ]:




