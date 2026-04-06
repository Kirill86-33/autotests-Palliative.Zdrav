from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class SearchField(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'

    BUTTON_SEARCH = ("xpath", "//div[@class='MuiBox-root css-ue9arn']")
    INPUT_SEARCH = ("xpath", "//input[@placeholder='Поиск...']")

    def click_button_search(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.BUTTON_SEARCH))
        btn.click()
        self.wait.until(EC.visibility_of_element_located(self.INPUT_SEARCH))



    def enter_input_search(self, text):
        input_field = self.wait.until(EC.element_to_be_clickable(self.INPUT_SEARCH))
        input_field.clear()
        input_field.send_keys(text)
        input_field.send_keys(Keys.ENTER)