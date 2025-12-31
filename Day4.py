#!/usr/bin/env python
# coding: utf-8

# In[10]:


tasks = ["Study", "Practice Python", "Daily Practice "]


# In[11]:


tasks.append("Apply for internship")   # add
tasks.remove("Study")                  # remove
print(tasks[0])                         # access


# In[12]:


for task in tasks:
    print(task)


# In[13]:


student = {
    "name": "Sadaf",
    "age": 21,
    "field": "Artificial Intelligence"
}


# In[14]:


print(student["name"])


# In[15]:


student["age"] = 22


# In[16]:


for key, value in student.items():
    print(key, ":", value)

