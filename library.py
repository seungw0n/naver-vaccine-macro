"""
    File name: main.py
    Author: Seung Won Joeng
    Date created: 7/14/2021
    Date last modified: 7/22/2021
    Python Version: 3.7
"""


import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller

# Need to be updated
CLASS_REFRESH = '_1MCHh'
CLASS_LIST = '_31ySW'
XPATH_RESERVATION = "//*[@id='_list_scroll_container']/div/div/div[3]/ul/li/div[2]/div/a"
XPATH_CONFIRMATION = "//*[@id='reservation_confirm']"
VACCINE_URL = "https://m.place.naver.com/rest/vaccine?vaccineFilter=used"


def wait(aTime, msg=""):
    for i in range(aTime):
        time.sleep(1)
        if msg != "":
            print("[", msg, "]", "Remaining Time : ", str((aTime-i)))
        else:
            print("Remaining Time : ", str((aTime - i)))


def move_page(driver, url):
    driver.get(url)


def open_list(driver):
    print("Function: open_list")
    element = driver.find_element_by_class_name(CLASS_LIST)
    element.click()
    time.sleep(1)


def refresh(driver):
    try:
        print("Function: refresh")
        element = driver.find_element_by_class_name(CLASS_REFRESH)
        element.click()
        time.sleep(1)
        return True
    except NoSuchElementException:
        print("Function: refresh\n\tPassed to reservation page")
        time.sleep(0.5)
        return False

def click_reservation(driver):
    try:
        print("Function: click_reservation")
        print('\007')  # sound
        element = driver.find_element_by_xpath(XPATH_RESERVATION)
        element.click()
        time.sleep(0.5)
        return True
    except NoSuchElementException:
        print("Function: click_reservation\n\tNot found")
        time.sleep(0.5)
        return False

def click_confirm(driver):
    try:
        print("Function: click_confirm")
        element = driver.find_element_by_xpath(XPATH_CONFIRMATION)
        return True
    except NoSuchElementException:
        print("Function: click_confirm\n\tNot found")
        time.sleep(0.5)
        return True



#
# def clickOne(driver):
#     print("Function: clickOne")
#     try:
#         element = driver.find_element_by_xpath(XPATH_RESERVATION)
#         element.click()
#         time.sleep(1)
#         return clickTwo(driver=driver)
#
#     except NoSuchElementException:
#         print("\tNo Such element\n\t\t", XPATH_RESERVATION)
#         return False
#
#
# def clickTwo(driver):
#     print("Function: clickTwo")
#     try:
#         print('\007')
#         element = driver.find_element_by_xpath(XPATH_CONFIRMATION)
#         element.click()
#         return True
#     except NoSuchElementException:
#         print("\tNo Such element\n\t\t", XPATH_CONFIRMATION)
#         return False


# def check_avail_vaccines(driver):
#     print("Function: check_avail_vaccines")
#     try:
#         driver.find_element_by_class_name(CLASS_DEACTIVATED_RESERVED)
#
#     except NoSuchElementException:
#         try:
#             driver.find_element_by_class_name("_3zkaH")
#         except NoSuchElementException:
#             print("[ERROR] Function: check_avail_vaccines")
#             print("\tCannot find class _3zkaH")
#             return False
#
#         time.sleep(1)
#
#         try:
#             element = driver.find_element_by_class_name(CLASS_ACTIVATED_RESERVED)
#             element.click()
#
#         except NoSuchElementException:
#             print("[ERROR] Function: check_avail_vaccines") # Maybe network issue
#             print("\tCannot find class CLASS_ACTIVATED_RESERVED")
#
#     time.sleep(1)
#     if driver.current_url != VACCINE_URL:
#         return True
#     else:
#         return False

"""

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

"""
