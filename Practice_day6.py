#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
from datetime import datetime
import re

# Math module
print("Square root of 49:", math.sqrt(49))

# Datetime module
now = datetime.now()
print("Current time:", now.strftime("%Y-%m-%d %H:%M"))

# Regex validation
email = input("Enter email: ")

if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Valid email")
else:
    print("Invalid email")


# In[ ]:




