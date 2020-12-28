# How to Scrape News Articles Using Python
Newspaper is a Python module used for extracting and parsing news articles. To extract information from the websites of newspapers and magazines we are going to use Newspaper library.
Using Newspaper library, not only extracting and curating articles, but you can also extract text, summary text, get text keyword.

## Getting Started:
1. Download [Anaconda](https://docs.anaconda.com/anaconda/user-guide/tasks/install-packages/). 
* I downloaded Individual Edition. Anaconda is the world's most popular Python distribution platform which contains Python packages including Jupyter Notebook, Scipy, Numpy, Panda, Matplotlib, TensorFlow, etc. 

2. Launch Jupyter Notebooks to write and iterate your Python code. See [Instruction](https://www.codecademy.com/articles/how-to-use-jupyter-notebooks/).

3. Installation Newspaper Module + Ready to Scrape News Articles
```
pip install newspaper3k
```

## Ready to Scrape News Articles

* Import nltk - nltk is an open source Python package
```py
import nltk
from newspaper import Article
```
```
* download news article
```py
url = 'https://www.cnbc.com/2020/12/27/wonder-woman-1984-opening-weekend-leads-to-fast-tracked-third-film.html'
article = Article(url)
article.download()
article.parse()
nltk.download('punkt')
article.nlp()
```

* get pulication date of the news article
```py
article.publish_date
```

* get article text
```py
print(article.text)
```

* load article keywords
```py
article.keywords
```

* summarize news article 
```py
print(article.summary)
```

* who is the author of the article?
```py
article.authors
```

**This Newspapaer library works in 30 + languages!**
```py
import newspaper
newspaper.languages()
```


[See my module](https://github.com/Conniekoh/Web-Scrapping/blob/master/codility/How%20to%20Scrap%20News%20Article.ipynb)


