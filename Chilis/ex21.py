import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

with open('ex21.txt', 'w') as open_file:
    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a:
            open_file.write(story_heading.a.text.replace('\n', ' ').strip())
        else:
            open_file.write(story_heading.contents[0].strip())
    print()