
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class ryan:

    def set_up(self):
        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.ryanair.com/ie/en/")
        self.driver.maximize_window()
