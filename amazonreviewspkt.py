#!/usr/bin/env python
# coding: utf-8

# # Amazon Reviews

# In[21]:


get_ipython().system('pip install BeautifulSoup4')


# In[27]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


# In[72]:


def get_data(pageNo):  
    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
    URL = "https://www.amazon.com/Python-Data-Science-Essentials-practitioners-ebook/product-reviews/B07H5KBDVL/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
    webpage = requests.get(URL, headers=HEADERS)
    content= webpage.content
    soup = BeautifulSoup(content , "lxml")
    review_amazon=[]


# In[127]:


for d in soup.findAll('div', attrs={'class':'a-section a-spacing-none aok-relative'}):
        
        title = soup.find( attrs={"id":'productTitle'})
        #review_amazon.append(title)
        review_date = soup.find( attrs={'data-hook':'review-date'})
        review_amazon.append(review_date)
        customer_name = soup.find( attrs={'class':'a-profile-name'})
        review_amazon.append(customer_name)
        review_title = soup.find(attrs={'data-hook':'review-title'})
        review_title = review_title.text.strip('\n')
        review_amazon.append(review_title)
        review = soup.find(attrs={'data-hook':'review-body'})
        review = review.text.strip().replace('\n', '')
        review_amazon.append(review)
        rating = soup.find(attrs={'class':'a-icon-alt'})
        review_amazon.append(rating)
        review_count = soup.find(attrs={'id':'acrCustomerReviewText'})
        review_amazon.append(review_count)
        


# In[128]:


review_amazon
reviews_df=pd.DataFrame(reviews).T


# In[129]:


reviews_df


# In[130]:


reviews_df.to_csv('amazonreview.csv',index=False,encoding='utf-8')


# In[131]:


df = pd.read_csv("amazonreview.csv")


# In[132]:


df.shape


# In[133]:


df.head(23)


# In[ ]:




