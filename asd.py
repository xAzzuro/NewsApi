import requests
import urllib
from bs4 import BeautifulSoup

url = "http://aajtak.intoday.in/"
page = requests.get(url)
data = urllib.request.urlopen(url)

soup = BeautifulSoup(data,"html.parser")
for a in soup:
    seen = set(data)
        for li in soup.select('ul li.href'):
            if li in seen:
                li.extract()  # remove tag if seen
            else:
                seen.add(li)