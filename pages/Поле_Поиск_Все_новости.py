from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class SearchNewsPage(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/news'

    SEARCH_FIELD = ("xpath", "//div//input[@placeholder='Поиск']")
    # Более гибкий локатор: ищем h4, содержащий часть текста
    CARD_NEW = ("xpath", "//h4[contains(text(), 'Новое пособие')]")

    def enter_search_field(self, text):
        field = self.wait.until(EC.visibility_of_element_located(self.SEARCH_FIELD))
        field.clear()
        field.send_keys(text)
        field.send_keys(Keys.ENTER)   # запускаем поиск
        time.sleep(1)  # небольшая пауза для загрузки результатов

    def click_card_new(self):
        card = self.wait.until(EC.element_to_be_clickable(self.CARD_NEW))
        self.driver.execute_script("arguments[0].click();", card)