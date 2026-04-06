from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC





class SearchUsefulPage(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/library'


    SEARCH_FIELD = ("xpath","//div//input[@placeholder='Поиск']") 
    CARD_USEFUL = ("xpath","(//div//a)[12]") 




    def enter_search_field(self, text):
        field = self.wait.until(EC.visibility_of_element_located(self.SEARCH_FIELD))
        field.clear()
        field.send_keys(text)




    def click_card_useful(self):
        card = self.wait.until(EC.element_to_be_clickable(self.CARD_USEFUL))
        self.driver.execute_script("arguments[0].click();", card)