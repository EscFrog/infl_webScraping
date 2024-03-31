import requests

res = requests.get("http://google.com")
res.raise_for_status() # 응답에 문제가 생겼을 경우 바로 에러를 내고 프로그램을 종료한다.
# print("응답코드 :", res.status_code) # 200이면 정상

# if res.status_code == requests.codes.ok: # status_code가 200이라는 것과 같은 얘기
#   print('정상입니다.')
# else:
#   print(f"문제가 생겼습니다. [에러코드 {res.status_code}]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf-8") as f:
  f.write(res.text)