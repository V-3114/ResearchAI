from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait

class DriverManager:

    def __init__(self, headless=False, uc=True, incognito=True):

        self.driver = Driver(uc=uc, headless=headless, incognito=incognito)
        self.driver.uc_gui_click_captcha()
        self.wait = WebDriverWait(self.driver, 60)


    def get_driver(self):

        return self.driver, self.wait


    def quit_driver(self):

        if self.driver:
            self.driver.quit()
            print("✅ Browser closed successfully.")
        else:
            print("⚠️ No driver to quit.")