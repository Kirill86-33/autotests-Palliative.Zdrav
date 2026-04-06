from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CardEventsSearch(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/events'


    SEARCH_FIELD = ("xpath","//div//input[@placeholder='Поиск']") 
    CARD_EVENTS = ("xpath","(//div//a)[12]") 



    def wait_for_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_FIELD))


    def enter_search_field (self, text):
        self.wait_for_page_load()
        input_city = self.wait.until(EC.element_to_be_clickable(self.SEARCH_FIELD))
        input_city.clear()
        input_city.send_keys(text)


    def click_card_events (self):
        btn = self.wait.until(EC.element_to_be_clickable(self.CARD_EVENTS))
        self.driver.execute_script("arguments[0].click();", btn)