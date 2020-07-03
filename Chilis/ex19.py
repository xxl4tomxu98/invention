import requests
from bs4 import BeautifulSoup

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

all_p_cn_text_body = soup.select("div.parbase.cn_text > div.body > p")

for elem in all_p_cn_text_body[7:]:
  print(elem.text)