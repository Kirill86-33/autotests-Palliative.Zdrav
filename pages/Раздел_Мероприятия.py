from pages.base_page import BasePage

class CardEvents(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'


    CARD_EVENTS = ("xpath","//div//h4[text()='Мероприятия']") 
   



    def click_events (self):  
        cart_events= self.driver.find_element(*self.CARD_EVENTS) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_events)


