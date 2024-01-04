from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

namelist = bs.find_all('span', {'class': 'green'})
all_tags = bs.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
find_the_prince = bs.find_all(text='the prince')
title = bs.find(id='green')
for name in namelist:
    print(name.get_text())

print(all_tags)
print(f"Numer of times 'the prince' was found; {len(find_the_prince)}")
print(title)
