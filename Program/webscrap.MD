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
          
```python
import requests
from bs4 import BeautifulSoup as bs

username = input("enter the git username: ")
repo = input("user's repo name on git: ")

URL = f'https://github.com/{username}/{repo}'
r = requests.get(URL)
soup = bs(r.content, 'html.parser')
Image = soup.find('img',{"alt":"ScreenShot"})['src']
print(Image)
