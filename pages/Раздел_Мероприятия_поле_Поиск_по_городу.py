from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class EventsSearchCity(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/events'

    SEARCH_FIELD = ("xpath", "//input[@placeholder='Поиск по городу']")  # уточните, если нужно
    BUTTON_CITY = ("xpath", "//span[text()='Балашиха']")  # уточните локатор кнопки

    def wait_for_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_FIELD))

    def enter_city(self, city):
        self.wait_for_page_load()
        input_city = self.wait.until(EC.element_to_be_clickable(self.SEARCH_FIELD))
        input_city.clear()
        input_city.send_keys(city)

    def click_button_city(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.BUTTON_CITY))
        self.driver.execute_script("arguments[0].click();", btn)