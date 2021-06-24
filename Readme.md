## 🐧 Penguin Random House - Sentiment Analysis
## ⌛ Summary : TL;DR;

Developed web crawlers, featurized the text and trained the ML algorithm to classify reviews and build a dashboard.  


## 🏠 Problem statement :
Penguin Random House is a global trade publisher known for publishing in diverse languages publishing e-books and audio books across genres like fiction, non-fiction, thrillers, memoirs, health and so on. Since Penguin Random House products are distributed over various channels, they want to understand how it is received by the customers. They want to build a review collecting system to understand the customers better. The system should help to collect reviews from sources like Amazon, Goodreads.

## 🚩 Purpose :
Now , more than ever , it's key for companies to play close attention to the **voice of customer** (VOC) to improve their products.

That's where sentiment analysis helps to understand the customer like and dislike about product

**Sentiment Analysis** is the automated process of understanding the sentiment or opinion of a given text . We can use it to automatically analyze product reviews and sort them by Positive , Neutral , Negative


## 🎯 Goals :

- As a data engineer, to download reviews from a book page on Amazon and GoodRead
- As a data scientist, to classify a review, written in English. Output should be Positive, Negative or Neutral (polarity) 
- To visualize the number of reviews of products across all channels for each week, month, and year, broken down per polarity


  ![picture](https://drive.google.com/uc?export=view&id=1LZVJRw-SSMe2CKzdYxHeqedT-VWa79pZ)


## Milestones, code and tech 

### 💻 Technology Stack

<img src='https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white'>

<img src='https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white'>

<img src='https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white'>

<img src='https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white'>


<img src='https://img.shields.io/badge/BeautiulSoup-FF6384?style=for-the-badge&logo=chart-dot-js&logoColor=white'>

<img src='https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white'>

<img src='https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white'>

<img src='https://img.shields.io/badge/Seaborn-239120?style=for-the-badge&logo=plotly&logoColor=white'>


#### The project was composed by 4 milestones

## 🥇Crawling Amazon and Goodreads :

- Created a [`Amazon`](https://github.com/TeamEpicProjects/Penguin-Random-House/blob/Day3/Nitheesh_Day3.ipynb) and [`Goodreads crawler`](https://github.com/TeamEpicProjects/Penguin-Random-House/blob/Day4/Nitheesh_Day4.ipynb) based on beautiful Soup (bs4)
- Downloaded all the reviews that spans over multiple pages in each page, altogether with the ratings (1-5 stars) and the dates
- Downloaded the dataset.csv file

The final outcome looks like a table below :

|   Source   |   Book Title  |       Review     | Stars  |    Date |
----------|---------------|------------------|--------|---------|
|Goodreads | Peace and War | I love this book |   5    | 2021-06-01
|Goodreads | Peace and War | I hate it        |   1    | 2021-06-02
|Goodreads | Peace and War | Quite indifferent|   3    | 2021-05-20



## 🥈Extract the sentiment from each review via NLP
- Cleaned the reviews using **Regular Expressions**
- Extracted features from text using **Count Vectorizer**
- Created a multinominal **text classifier** using [**`Multinominal Naive Bayes Classifier`**](https://github.com/TeamEpicProjects/Penguin-Random-House/blob/Day6/Nitheesh_Day%206.ipynb)
- Output is Polarity -  Positive(1), Negative(-1) or Neutral(0)
- Got an accuracy of 73.4

  ![picture](https://drive.google.com/uc?export=view&id=1xaoXK3QbEHzuPulmvFN64FSm1ijnPFU3)

## 🥉Improvising The results
- Cleaned the reviews using **Regular Expressions**
- Extracted features from text using **TF-IDF**
- Created a Binary text classifier using [**`SGD Classifier`**](https://github.com/TeamEpicProjects/Penguin-Random-House/blob/Day7/Nitheesh_Day%207.ipynb) 
- Output is  Polarity - Positive(1) or Negative(0) 
- Used **GridSearchCV** for Cross Validation 
- Improvised the results by implementing [**`Deep Learning Techniques : ANN , RNN[LSTM]`**](https://github.com/TeamEpicProjects/Penguin-Random-House/blob/Day8/Nitheesh_Day%208.ipynb)
    - Activation Function - Sigmoid ; Optimizer - Adam ; Loss Function - Binary_Crossentropy

## 📊 Visualisation of the results, for product managers and exec management
- Created a [`Visualisations`](https://github.com/TeamEpicProjects/Penguin-Random-House/blob/Day10/Nitheesh_Day%209%2610.ipynb) using Matplotlib and Seaborn for the following:
    - Distribution of Ratings
    - Distribution of Sentiment
    - Sentiment Polarity Distribution
    - Review Text Length Distribution
    - Mean and Median Polarity Of Reviews Per Month
    - Top 10 Most Reviewed Books
    - Year and Month Wise Review Count
    - Word Cloud of words impacting the review
    
## ✏ Contribute : 
Contributions are always welcome !

### &copy;_Nitheesh Reddy_

## 📱 Contact Me :

<a href='nitheesh.1305@gmail.com'>
<img src='https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white'>
</a>

<a href='www.linkedin.com/in/sai-nitheesh-kumar-reddy-53b792114'>
 <img src='https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white'></a>
 
 

