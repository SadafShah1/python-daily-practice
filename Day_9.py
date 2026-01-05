#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
)
""")

conn.commit()
conn.close()

print("Table created successfully")


# In[ ]:

import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()




