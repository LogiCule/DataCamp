#Importing flat files from the web: your turn!

from urllib.request import urlretrieve 
import pandas as pd
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
urlretrieve(url,'winequality-red.csv')
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())

#Opening and reading flat files from the web

import matplotlib.pyplot as plt
import pandas as pd
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
df = pd.read_csv(url,sep=";")
print(df.head())
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()

#Importing non-flat files from the web

import pandas as pd
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'
xls = pd.read_excel(url,sheet_name=None)
print(xls.keys())
print(xls['1700'].head())

#Performing HTTP requests in Python using urllib

from urllib.request import urlopen,Request
url = "http://www.datacamp.com/teach/documentation"
request = Request(url)
response = urlopen(request)
print(type(response))
response.close()

#Printing HTTP request results in Python using urllib

from urllib.request import urlopen, Request
url = "http://www.datacamp.com/teach/documentation"
request = Request(url)
response = urlopen(request)
html = response.read()
print(html)
response.close()

#Performing HTTP requests in Python using requests

import requests
url = "http://www.datacamp.com/teach/documentation"
r = requests.get(url)
text = r.text

#Parsing HTML with BeautifulSoup

import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/~guido/'
r= requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)
pretty_soup = soup.prettify()
print(pretty_soup)

#Turning a webpage into data using BeautifulSoup: getting the text

url = 'https://www.python.org/~guido/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)
guido_title = soup.title
print(guido_title)
guido_text = soup.get_text()
print(guido_text)

#Turning a webpage into data using BeautifulSoup: getting the hyperlinks

url = 'https://www.python.org/~guido/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)
print(soup.title)
a_tags = soup.find_all('a')
for link in a_tags:
    print(link.get('href'))
