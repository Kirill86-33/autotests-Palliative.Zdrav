from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class TabImportant(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/library'

    TAB_IMPORTANT = ("xpath", "//div//button[text()='Важное']")

    def click_button_search(self):
        button_leave = self.wait.until(EC.element_to_be_clickable(self.TAB_IMPORTANT))
        self.driver.execute_script("arguments[0].click();", button_leave)

    def click_tab_important(self):
        self.click_button_search()