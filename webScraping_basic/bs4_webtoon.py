import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
books = soup.find_all("article", attrs={"class":"product_pod"})
for book in books:
    title = book.find("h3").get_text()
    print(title)