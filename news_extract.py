import requests
import urllib
from bs4 import BeautifulSoup

url = "http://aajtak.intoday.in/"
page = requests.get(url)
data = urllib.request.urlopen(url)

soup = BeautifulSoup(data,"html.parser")
add = soup.find_all('a')
print(add)

#news= soup.find_all('div',attrs={"class" : "play_more"})
#print(news.text)
for a in soup.find_all('a', href=True):
   print ("Found the URL:", a['href'])
