#!/usr/bin/env python
# coding: utf-8

# # GOOD READ REVIEWS

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


# In[26]:


HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
URL ="https://www.goodreads.com/book/show/25527772-python-data-science-essentials---learn-the-fundamentals-of-data-science"
webpage = requests.get(URL, headers=HEADERS)
content1 = webpage.content
    


# In[29]:


soup = BeautifulSoup(content1, "lxml")
review_gooodread=[]


# In[33]:


titles = soup.find("h1", id='bookTitle').text.strip()
authors = soup.find('span', itemprop='name').string
reviews=soup.find_all('span',style="display:none")


# In[36]:


for x in range(1,len(reviews)):
      review_gooodread.append(reviews[x].text)

review_gooodread
        


# In[38]:


reviews_df=pd.DataFrame(review_gooodread).T
reviews_df


# In[39]:


reviews_df.to_csv('goodreadreview.csv',index=False,encoding='utf-8')


# In[40]:


df = pd.read_csv("goodreadreview.csv")


# In[41]:


df.shape

