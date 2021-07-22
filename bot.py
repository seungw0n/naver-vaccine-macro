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

    def process(self):
        result_refresh = refresh(driver=self.driver)  # Find and click refresh button
        result_reservation = click_reservation(driver=self.driver)
        result_confirm = click_confirm(driver=self.driver)
        return result_refresh, result_reservation, result_confirm

    def run(self):
        wait(aTime=20)  # You can change time
        # You must be finish login action in aTime seconds.

        move_page(driver=self.driver, url=VACCINE_URL)  # Move to vaccine reservation page
        wait(aTime=20)  # Wait 15 secs for network bandwidth

        open_list(driver=self.driver)  # To see hospital list

        # cnt = 0
        while True:
            res_ref, res_res, res_con = self.process()

            """ Need to implement logic that handles the 인증서 here """

            if res_con:
                print("Complete")

    def close(self):
        print("Quit driver")
        self.driver.quit()

