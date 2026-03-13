from pages.base_page import BasePage

class EventsSearchCity(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/events'


    SEARCH_FIELD = ("xpath","//div//input[@placeholder='Поиск по городу']") 
    BUTTON_CITY = ("xpath","//div//span[text()='Балашиха']") 



    def enter_city (self, city):  
        input_city = self.driver.find_element(*self. SEARCH_FIELD)
        input_city.send_keys(city)



    def click_button_city (self):  
        button_city = self.driver.find_element(*self.BUTTON_CITY) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_city)