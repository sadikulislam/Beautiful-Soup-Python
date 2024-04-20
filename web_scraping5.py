# Web Scraping with BeautifulSoup, Request, selenium
import re
import requests
from bs4 import BeautifulSoup

url = 'https://oxylabs.io/blog'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# blog_titles = soup.find_all('a', class_='e1dscegp1')
# dynamic rendering

# blog_titles = soup.find_all('a', class_=re.compile('oxy-rmqaiq'))
# Using regex

# blog_titles = soup.select('a.e1dscegp1')
# using CSS selectors

