#!/usr/bin/env python
# coding: utf-8

# In[2]:


# List practice
skills = ["Python", "C++", "Web development"]

skills.append("Problem Solving")

for skill in skills:
    print("Skill:", skill)


# Dictionary practice
profile = {
    "name": "Sadaf",
    "degree": "AI",
    "status": "Student"
}

profile["status"] = "Learner"

for key, value in profile.items():
    print(key, "=>", value)


# In[ ]:




