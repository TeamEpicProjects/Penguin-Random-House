#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
import numpy as np
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
import seaborn as sns


# In[25]:


Goodreads = pd.read_csv('goodreads.tsv' , sep='\t') 
Goodreads.head()


# In[26]:


df = Goodreads
df


# In[27]:


df1 = df[(df.rating==1) | (df.rating==6)]
df1.info()
df1.describe()
f=df1.isnull()
f.sum()


# In[32]:


df1.groupby('title')['rating'].count()


# In[33]:


df1.groupby('title')['rating'].mean()


# In[40]:


#Title
plt.hist(df1['title'])
plt.xticks(rotation = 80)
plt.show()
# Rating
plt.hist(df1['rating'])
plt.xticks(rotation = 80)
plt.show()


# In[43]:


plt.figure(figsize=(12,6))
sns.countplot(x ='title',hue='rating' ,data = df1)
plt.xticks(rotation = 90)
plt.show()

