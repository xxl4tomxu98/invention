import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

for title in soup.findAll('h2'):

    print(title.text.replace("\n", " ").strip())
