import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
res = requests.get(url, headers=headers)
res.raise_for_status()
print(res.status_code)
soup = BeautifulSoup(res.text, "lxml")

items =  soup.find_all("li", attrs={"class": re.compile("^search-product")})

for idx, item in enumerate(items):
    name = item.find("div", attrs={"class": "name"}).get_text() # 제품명
    price = item.find("strong", attrs={"class": "price-value"}).get_text() # 가격
    
    rate = item.find("em", attrs={"class": "rating"})
    if rate:
        rate = rate.get_text() # 평점
    else:
        rate = "평점 없음"
    
    rate_count = item.find("span", attrs={"class": "rating-total-count"}) # 평점수
    if rate_count:
        rate_count = rate_count.get_text() # 평점
    else:
        rate_count = "평점 없음"
    
    print(idx, "----> ", name.strip(), price.strip(), rate.strip(), rate_count.strip())