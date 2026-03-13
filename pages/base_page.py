from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver



class BasePage:
    LOGO = ("xpath", "//div[@class='MuiBox-root css-matur3']") 

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 10)


    def open(self): # Открытие страницы, если задан URL    
        if hasattr(self, 'PAGE_URL'):
            self.driver.get(self.PAGE_URL)