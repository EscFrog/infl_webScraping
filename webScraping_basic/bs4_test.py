import requests
from bs4 import BeautifulSoup

url = "https://www.printables.com/model"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title.get_text()) # 처음 발견되는 title 엘리먼트의 텍스트를 출력한다
# print(soup.a)
# print(soup.a.attrs)
# print(soup.a["href"])

print(soup.find("h3", attrs={"class" : "name"}))