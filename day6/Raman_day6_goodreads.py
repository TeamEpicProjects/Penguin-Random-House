#!/usr/bin/env python
# coding: utf-8

# In[49]:


# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import string
import nltk
import warnings 
get_ipython().run_line_magic('matplotlib', 'inline')
warnings.filterwarnings("ignore", category=DeprecationWarning)
from nltk.corpus import stopwords
stop = stopwords.words('english')


# In[50]:


dat = pd.read_csv('goodreads.tsv' , sep='\t') 
print(dat.shape)
dat.head(5)


# In[52]:


# Get the number of dates / entries in each month
dat.groupby('title')['rating'].count()
dat.rating.value_counts()


# In[70]:


dat.groupby('body')['rating'].mean()
f=dat.isnull()
f
#Dropping Null Values
df=dat.dropna()
df
#Changing review data of every row into string type
for i in range(0,len(dat)-1):
    if type(dat.iloc[i]['body']) != str:
        dat.iloc[i]['body'] = str(dat.iloc[i]['body'])
type(dat.body)


# In[141]:


#function to represent sentiment -1(negetive);0(neutral);1(positive)
def sentiment(n):
    return 1 if n>=4 else (-1 if n<=2 else 0)
#Applying Sentiment Function 
dat['sent'] = dat['rating'].apply(sentiment)
dat.head()


# In[142]:


dat.sentiment.value_counts()


# In[143]:


Sentiment_count=dat.groupby('sent').count()
Sentiment_count


# In[144]:


from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer


# In[145]:


#tokenizer to remove unwanted elements from out data like symbols and numbers
token = RegexpTokenizer(r'[a-zA-Z0-9]+')
cv = CountVectorizer(lowercase=True,stop_words='english',ngram_range = (1,1),tokenizer = token.tokenize)
text_counts= cv.fit_transform(dat['title'])


# In[146]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    text_counts, dat['sentiment'], test_size=0.3, random_state=1)


# In[147]:


from sklearn.naive_bayes import MultinomialNB
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Generation Using Multinomial Naive Bayes
clf = MultinomialNB().fit(X_train, y_train)
predicted= clf.predict(X_test)
print("MultinomialNB Accuracy:",metrics.accuracy_score(y_test, predicted))


# In[148]:


from sklearn.feature_extraction.text import TfidfVectorizer
tf=TfidfVectorizer()
text_tf= tf.fit_transform(dat['title'])
text_tf


# In[149]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    text_tf, dat['sentiment'], test_size=0.3, random_state=123)


# In[150]:


from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
# Model Generation Using Multinomial Naive Bayes
clf = MultinomialNB().fit(X_train, y_train)
predicted= clf.predict(X_test)
print("MultinomialNB Accuracy:",metrics.accuracy_score(y_test, predicted))


# In[151]:


model = MultinomialNB()
model.fit(X_train, y_train)
#Predicting on X_test
y_pred  =  model.predict(X_test)
y_pred


# In[152]:


from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
cr = classification_report(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
ac = accuracy_score(y_test,y_pred)
ac


# In[153]:


#Classification Report
print('Classification Report :\n')
print(cr)


# In[154]:


import seaborn as sn
import matplotlib.pyplot as plt


# In[155]:


categories = [-1,0,1]
sn.set(font_scale=1.4) # for label size
sn.heatmap(cm, annot=True) # font size

plt.show()


# In[156]:


print('Accuracy of our Model is : ',ac*100)

