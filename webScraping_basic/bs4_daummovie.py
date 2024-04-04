import requests
from bs4 import BeautifulSoup

res = requests.get("https://search.daum.net/search?w=tot&q=2023%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR")
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

with open("bs_res", "w") as f:
    f.write(soup.text)

# frame = soup.find("div", attrs={"class":"pdt2"})
# if frame:
#     thumbs = frame.find_all("a", attrs={"class":"thumb_bf"})
# else:
#     print("can't find frame")

# for thumb in thumbs:
#     print(thumbs)
#     # image = thumb.find("img")
#     # print(image["src"])