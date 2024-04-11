from selenium import webdriver

browser = webdriver.Chrome()

# 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element(y.CLASS, "link_login")
elem.click()

# 3. id, pw 입력
browser.find_element(by.ID, "id").send_keys("naver_id")
browser.find_element(by.ID, "pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element(by.ID, "log.login").click()
browser.find
