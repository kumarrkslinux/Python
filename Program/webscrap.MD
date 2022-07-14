```python
import requests as re
from bs4 import BeautifulSoup as bs

URL = "https://economictimes.indiatimes.com/"
r = re.get(URL)
soup = bs(r.content, 'html.parser')
M = 1
for link in soup.find_all('a'):
     if(str(type(link.string)) == "<class 'bs4.element.NavigableString'>"
       and len(link.string) > 35):
          print(str(M)+".", link.string)
          M += 1
