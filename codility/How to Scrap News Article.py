#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#install Newspaper Module 
pip install newspaper3k


# In[ ]:


import nltk
from newspaper import Article


# In[ ]:


url = 'https://www.cnbc.com/2020/12/27/wonder-woman-1984-opening-weekend-leads-to-fast-tracked-third-film.html'
article = Article(url)
article.download()
article.parse()
nltk.download('punkt')
article.nlp()


# In[ ]:


article.publish_date


# In[ ]:


article.top_image


# In[ ]:


# get article text
print(article.text)


# In[ ]:


# load article keywords
article.keywords


# In[ ]:


# summarize news article 
print(article.summary)


# In[ ]:


# who is the author of the article?
article.authors


# In[ ]:


# This Newspapaer library works in 30 + languages!

import newspaper
newspaper.languages()


# In[ ]:




