import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

for i in range(1, 6):
    
    # print("페이지 ", i)
    # print("*" * 10)

    url = f"https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={i}&rocketAll=false&searchIndexingToken=1=8"
    
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    # print(res.status_code)
    
    soup = BeautifulSoup(res.text, "lxml")

    items =  soup.find_all("li", attrs={"class": re.compile("^search-product")})

    for item in items:
        
        # 광고 상품은 제외
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            continue
        
        name = item.find("div", attrs={"class": "name"}).get_text() # 제품명
        # 애플 제품 제외
        if "Apple" in name:
            continue
        
        price = item.find("strong", attrs={"class": "price-value"}).get_text() # 가격
        
        rate = item.find("em", attrs={"class": "rating"}) # 평점
        # 평점 없는 제품 제외
        if rate:
            rate = rate.get_text() # 평점
        else:
            continue
        
        rate_count = item.find("span", attrs={"class": "rating-total-count"}) # 평점수
        # 평점 수 없는 제품 제외
        if rate_count:
            rate_count = rate_count.get_text()[1:-1] # 평점 괄호 제외
        else:
            continue
        
        link = item.find("a", attrs={"class": "search-product-link"})["href"]
        
        # 리뷰 100개 이상, 평점 4.5이상 되는 상품만 출력
        if float(rate) >= 4.5 and int(rate_count) >= 100:
            print(f"제품명 : {name.strip()}")
            print(f"가격 : {price.strip()}")
            print(f"평점 : {rate.strip()}점 ({rate_count.strip()}개)")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-" * 100)