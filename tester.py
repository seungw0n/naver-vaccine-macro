from selenium import webdriver

class WebDriverChrome(object):

    def __init__(self):
        self.driver = self.StartWebdriver()

    def StartWebdriver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        driver = webdriver.Chrome(options=options)
        return driver

    def RunStart(self):
        self.driver.get('https://bot.sannysoft.com')
        # time.sleep(10)
        # self.driver.quit()

if __name__ == '__main__':
    Crawl = WebDriverChrome()
    Crawl.RunStart()