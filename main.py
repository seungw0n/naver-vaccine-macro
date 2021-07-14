from selenium import webdriver

driver = webdriver.Chrome('/Users/beomi/Downloads/chromedriver')
driver.implicitly_wait(3)
# url에 접근한다.
driver.get('https://nid.naver.com/nidlogin.login')