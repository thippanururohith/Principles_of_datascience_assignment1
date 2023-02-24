#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import json
import seaborn as sns


# In[2]:


data = pd.read_csv("C:/Users/Administrator/Desktop/data science/StudentsPerformance.csv")


# In[4]:


data


# In[11]:


data=data.drop(columns =['lunch'])


# In[12]:


data.to_csv("C:/Users/Administrator/Desktop/Principles_of_data_science_Assignment-1/Question_2_Student_performance/data_clean/studentperformance_clean.csv")


# In[ ]:





# In[ ]:




