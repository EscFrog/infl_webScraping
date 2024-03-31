import re
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de) : 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se$) : 문자열의 끝 > case, base (O) | face (X)


p = re.compile("ca.e")

def print_match(m):
  if m:
    print(f"m.group() : {m.group()}") # 일치하는 문자열 반환
    print(f"m.string : {m.string}") # 입력받은 문자열을 그대로 출력
    print(f"m.start() : {m.start()}") # 일치하는 문자열의 시작 index
    print(f"m.end() : {m.end()}") # 일치하는 문자열의 끝 index
    print(f"m.span() : {m.span()}") # 일치하는 문자열의 시작 / 끝 index
  else:
    print("매칭되지 않음")
  print("")

checklist = ["case", "caseless", "caffe", "small cafe"]


m_list = [p.match(m) for m in checklist] # match : 주어진 문자열의 처음부터 일치하는지 확인

for m in m_list:
  print_match(m)


m2_list = [p.search(m) for m in checklist] # search : 주어진 문자열중에 일치하는게 있는지 확인

for m in m2_list:
  print_match(m)


find_result = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
print(find_result)