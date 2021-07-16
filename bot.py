"""
    File name: main.py
    Author: Seung Won Joeng
    Date created: 7/14/2021
    Date last modified: 7/16/2021
    Python Version: 3.7
"""


from library import *
from setup import setup_driver
import pyautogui


class Bot:
    def __init__(self):
        self.driver = setup_driver()

    def run(self):
        wait(aTime=20)  # You can change time
        # You must be finish login action in aTime seconds.

        move_page(driver=self.driver, url=VACCINE_URL)  # Move to vaccine reservation page
        wait(aTime=15)  # Wait 15 secs for network bandwidth

        open_list(driver=self.driver)  # To see hospital list

        while True:
            refresh(driver=self.driver)  # Find and click refresh button
            res = check_avail_vaccines(driver=self.driver)
            print(res)
            if res:
                break

        wait(100)

    def close(self):
        print("Quit driver")
        self.driver.quit()

