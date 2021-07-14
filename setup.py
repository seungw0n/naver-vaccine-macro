import sys
import subprocess
import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import pyautogui


def install_packages():
    # https://www.activestate.com/resources/quick-reads/how-to-install-python-packages-using-a-script/
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'selenium', 'chromedriver_autoinstaller', 'pyperclip', 'pyautogui'])

    # process output with an API in the subprocess module:
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

    print(installed_packages)

def setup_chrome():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()

    return driver


#클립보드에 input을 복사한 뒤
#해당 내용을 actionChain을 이용해 로그인 폼에 붙여넣기
def type_input(xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    # pyautogui.typewrite(input, interval=0.5)
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

    time.sleep(2)

def login(driver):
    driver.implicitly_wait(3)

    url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"

    driver.get(url)

    type_input('//*[@id="id"]', "stevenswjoeng")
    time.sleep(2)
    type_input('//*[@id="pw"]', "1997zxc959703")
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

    return driver





def chrome_version():
    print(chromedriver_autoinstaller.install())

    driver = webdriver.Chrome()
    driver.get("https://flexshop1.com/shop/search.php?qsort=&qorder=&qcaid=1020&q=%EC%8A%A4%ED%86%A4&qname=1&qexplan=1&qbasic=1&qid=1&qfrom=&qto=")
    # driver.get("https://m.place.naver.com/rest/vaccine?vaccineFilter=used")

"""
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
"""
# def open_page():
#     subprocess.Popen(r'/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/Users/stevenjoeng/chrometemp')
#     option = Options()
#     option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")



# chrome_version()
driver = setup_chrome()
driver = login(driver)
time.sleep(5)
driver.quit()