

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img',
                     {'src': re.compile('..\/img\/gifts/img.*.jpg')})

for image in images:
    print(image['src'])

print(bs.find_all(lambda tag: len(tag.attrs) == 2))
print('\n\n')
print(bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?'))
