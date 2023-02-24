#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df = pd.read_csv('D:/data/raw_frailty_data.csv')


# In[3]:


print(df.shape)
# How many data points and features


# In[4]:


print(df.columns)
# What are the column names in our datsets


# In[5]:


df["Frailty"].value_counts()
#How many data points for Y and N 


# In[9]:


df.plot(kind='scatter',x='Height',y='Weight')
plt.show()
#Scatter plot for Height vs Weight


# In[7]:


sns.set_style("whitegrid");
sns.FacetGrid(df, hue="Frailty", height=4)     .map(plt.scatter, "Height", "Weight")      .add_legend();
plt.show();
# 2d scatter plot with legend as Frailty
# Observation : People whose weight is below 125 doesnt have frailty


# In[10]:


plt.close();
sns.set_style("whitegrid");
sns.pairplot(df, hue="Frailty", height = 3);
plt.show()
#Pairwise Scatter plot:Pair plot
#Observation:Here if we observe weight vs grip strength person with weight more than 135 and grip strength less than 30 are having Frailty Y


# In[12]:


sns.FacetGrid(df, hue="Frailty", height =5) .map(sns.histplot,"Height") .add_legend();
plt.show();

# Classification of Frailty based on Height


# In[13]:


sns.FacetGrid(df, hue="Frailty", height =5) .map(sns.histplot,"Weight") .add_legend();
plt.show();
# Classification of Frailty based on Weight


# In[14]:



sns.FacetGrid(df, hue="Frailty", height =5) .map(sns.histplot,"Age") .add_legend();
plt.show();
# Classification of Frailty based on Age


# In[15]:


sns.FacetGrid(df, hue="Frailty", height =5) .map(sns.histplot,"Grip strength") .add_legend();
plt.show();

# Classification of Frailty based on Grip Strength


# In[16]:


#For univariate analysis classification based on Gripstrength should be taken into consideration


# In[ ]:




