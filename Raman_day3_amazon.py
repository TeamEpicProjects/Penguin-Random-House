#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests   # Importing requests to extract content from a url
from bs4 import BeautifulSoup  # Beautifulsoup is for web scrapping...used to scrap specific content 
import re 
import os
import pandas as pd
import ssl
from datetime import datetime


# In[8]:


# For ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# In[9]:


links = pd.read_excel('dataset.xlsx')
links.head(5)
amazon_links = links['Amazon link']
data_asin=[]
titles=[]
base_urls=[]
ip=[]
length = len(amazon_links)
for i in range (len(amazon_links)):
    url=amazon_links[i]
    asin=url.split("/dp/")[1]
    title=url.split("/dp/")[0].split('.com/')[1]
    titles.append(title)
    data_asin.append(asin)
for i in range (length):
    base_url='https://www.amazon.com/'+titles[i]+'/product-reviews/'+data_asin[i]+'ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber='
    base_urls.append(base_url)
def reviews(base_url):
    reviews=[]
    ratings=[]
    review_dates=[]
    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
    for i in range (1,11):
        URL = base_url+str(i)
        webpage = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, "lxml")
        review = soup.find_all("span", attrs={'data-hook':'review-title'})
        review_date = soup.find_all("span", attrs={'data-hook':'review-date'})
        rating = soup.find_all("span", attrs={'class':'a-icon-alt'})
        for j in range(len(review)):
                reviews.append(review[j].text)
        for j in range(len(review_date)):
            review_dates.append(review_date[j].string.strip())
        for j in range(len(rating)):
            ratings.append(rating[j].string.strip())
        
    for j in range(len(reviews)):
        reviews[j]=reviews[j].strip('\n')
    
    for j in range(len(ratings)):
        ratings[j]=ratings[j].split()[0]
    
    for j in range(len(review_dates)):
            review_dates[j]=review_dates[j].split('on')[1].strip()
            review_dates[j]=datetime.strptime(review_dates[j],'%B %d, %Y').strftime('%Y-%m-%d')
        
    df=pd.DataFrame(list(zip(review_dates,ratings,reviews)),columns =['Date','Rating','Review'])
    print(df)    


# In[ ]:


AmazonReviews={}
for i in range (1,1000):
    df=reviews(base_urls[i])
    d={titles[i]:df}
    AmazonReviews.update(d)
    AmazonReviews 
reviews=pd.concat(AmazonReviews) 
reviews['source']='Amazon'
reviews.head()


# In[ ]:


reviews.to_csv('amazon_review.csv',index=False)

