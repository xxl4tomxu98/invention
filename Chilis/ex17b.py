import requests
from bs4 import BeautifulSoup

url = 'https://www.aiche.org/community/sites/divisions-forums/sustainable-engineering-forum-sef/membership'

sef_r = requests.get(url)
print(sef_r.status_code)
sef_soup = BeautifulSoup(sef_r.text, 'html.parser')
#print(sef_soup.text)

# for link in sef_soup.findAll('a', attrs={'id':'lvMembers-ctr10_Name'}):
#      print(link)

