import requests
from bs4 import BeautifulSoup

res = requests.get("https://search.daum.net/search?w=tot&q=2021%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR")
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

thumbs = soup.find_all("a", attrs={"class":"thumb_bf"})

if len(thumbs) >= 0:
    print("can't find image")

for thumb in thumbs:
    image = thumb.find("img")
    print("go")
    print(image["src"])