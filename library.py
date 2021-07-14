import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller

# Need to be updated
CLASS_REFRESH = '_1MCHh'
CLASS_LIST = '_31ySW'
CLASS_RESERVED = 'lwEWu._1dEyY'
VACCINE_URL = "https://m.place.naver.com/rest/vaccine?vaccineFilter=used"

def wait(rTime):
    for i in range(rTime):
        time.sleep(1)
        print("Remain Time: ", str((rTime-i)))

def open_list(driver):
    print("Function: open_list")
    element = driver.find_element_by_class_name(CLASS_LIST)
    element.click()
    time.sleep(1)

def refresh(driver):
    print("Function: refresh")
    element = driver.find_element_by_class_name(CLASS_REFRESH)
    element.click()
    time.sleep(1.5)

def check_avail_vaccines(driver):
    print("Function: check Vaccines")
    try:
        driver.find_element_by_class_name(CLASS_RESERVED).click()
    except NoSuchElementException:
        time.sleep(1)
        try:
            driver.find_element_by_class_name('lwEwu').click()
        except NoSuchElementException:
            print("UNKNOWN ERROR")

    time.sleep(1)
    if driver.current_url != VACCINE_URL:
        return True
    else:
        return False



chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
wait(10)

# move to vaccine site
driver.get("https://m.place.naver.com/rest/vaccine?vaccineFilter=used")
wait(15)

open_list(driver)

try:
    while True:
        refresh(driver=driver)
        res = check_avail_vaccines(driver=driver)
        if res:
            break
except KeyboardInterrupt:
    pass

wait(30)


driver.get("https://m.place.naver.com/rest/vaccine?vaccineFilter=used")
wait(10)
open_list(driver)
try:
    while True:
        refresh(driver=driver)
        res = check_avail_vaccines(driver=driver)
        if res:
            break
except KeyboardInterrupt:
    pass

driver.quit()

# element = driver.find_element_by_class_name("_1MCHh")
# element.click()
# wait(10)
# driver.quit()