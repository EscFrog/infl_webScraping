import requests
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
url = "http://nadocoding.tistory.com"

res = requests.get(url, headers=headers)
res.raise_for_status() # 응답에 문제가 생겼을 경우 바로 에러를 내고 프로그램을 종료한다.

with open("mygoogle.html", "w", encoding="utf-8") as f:
  f.write(res.text)