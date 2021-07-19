"""
    File name: main.py
    Author: Seung Won Joeng
    Date created: 7/14/2021
    Date last modified: 7/16/2021
    Python Version: 3.7
"""


from bot import Bot
from selenium import webdriver


if __name__ == '__main__':
    """
    setup.install_chrome()  # Just in case
    setup.install_packages()  # Just in case
    """

    bot = Bot()
    bot.run()
    bot.close()


#
# driver = webdriver.Chrome('/Users/beomi/Downloads/chromedriver')
# driver.implicitly_wait(3)
# # url에 접근한다.
# driver.get('https://nid.naver.com/nidlogin.login')
