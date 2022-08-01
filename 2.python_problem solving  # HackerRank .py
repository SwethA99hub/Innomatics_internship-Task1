#!/usr/bin/env python
# coding: utf-8

# ### 2.python_problem_solving

# #### Leap year 

# In[ ]:


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 400 ==0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0 :
        return True
    return False
    
    return leap


