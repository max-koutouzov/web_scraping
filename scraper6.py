

from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import re


random.seed()

def getLinks(articleUrl):
    html = urlopen(f'https://en.wikipedia.org{articleUrl}')
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id': 'bodyContent'}).find_all('a',
                                                          href=re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks('/wiki/Kevin_Bacon')

while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
