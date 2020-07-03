import requests
from bs4 import BeautifulSoup

url = 'https://www.yelp.com/search?find_desc=Restaurants%20-%20Open%20Now&find_loc=near%20irvine%2C%20CA'

yelp_r = requests.get(url)
print(yelp_r.status_code)
yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
print(yelp_soup.prettify())
print(yelp_soup.findAll('a'))

for link in yelp_soup.findAll('a'):
    print(link.text)