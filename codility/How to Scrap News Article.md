```python
#install Newspaper Module 
pip install newspaper3k
```


```python
import nltk
from newspaper import Article
```


```python
url = 'https://www.cnbc.com/2020/12/27/wonder-woman-1984-opening-weekend-leads-to-fast-tracked-third-film.html'
article = Article(url)
article.download()
article.parse()
nltk.download('punkt')
article.nlp()
```


```python
article.publish_date
```


```python
article.top_image
```


```python
# get article text
print(article.text)
```


```python
# load article keywords
article.keywords
```


```python
# summarize news article 
print(article.summary)
```


```python
# who is the author of the article?
article.authors
```


```python
# This Newspapaer library works in 30 + languages!

import newspaper
newspaper.languages()
```


```python

```
