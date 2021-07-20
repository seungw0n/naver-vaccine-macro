"""
    File name: main.py
    Author: Seung Won Joeng
    Date created: 7/14/2021
    Date last modified: 7/16/2021
    Python Version: 3.7
"""


import sys
import subprocess
from selenium import webdriver
import chromedriver_autoinstaller

LOGIN_URL = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"


def install_chrome():
    try:
        print("Function: install_chrome")
        chromedriver_autoinstaller.install()
        return True
    except Exception:
        print("Unknown Error")
        return False


def install_packages():
    print("Function: install_packages")
    # https://www.activestate.com/resources/quick-reads/how-to-install-python-packages-using-a-script/
    # implement pip as a subprocess:
    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', 'selenium', 'chromedriver_autoinstaller', 'pyautogui'])

    # process output with an API in the subprocess module:
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

    print(installed_packages)


def setup_driver():
    print("Function: setup_driver")
    try:
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)
        return driver
    except:
        print("[ERROR] Function: setup_driver")


"""
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
"""
# def open_page(): subprocess.Popen(r'/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome
# --remote-debugging-port=9222 --user-data-dir="/Users/stevenjoeng/chrometemp') option = Options()
# option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

