from pages.base_page import BasePage

class CardEventsSearch(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/events'


    SEARCH_FIELD = ("xpath","//div//input[@placeholder='Поиск']") 
    CARD_EVENTS = ("xpath","(//div//a)[12]") 



    def enter_search_field (self, text):  
        input_search = self.driver.find_element(*self. SEARCH_FIELD)
        input_search.send_keys(text)



    def click_card_events (self):  
        cart_events= self.driver.find_element(*self.CARD_EVENTS) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_events)