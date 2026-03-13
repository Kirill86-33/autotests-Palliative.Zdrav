from pages.base_page import BasePage

class SearchField(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'

    BUTTON_SEARCH = ("xpath", "(//div)[17]")
    INPUT_SEARCH = ("xpath", "//div//input[@placeholder='Поиск...']")
 
  

    def click_button_search (self):  
       button_search = self.driver.find_element(*self.BUTTON_SEARCH) # Добавляем явное ожидание
       self.driver.execute_script("arguments[0].click();", button_search)



    def enter_input_search (self, text):  
        input_search = self.driver.find_element(*self.INPUT_SEARCH) # Добавляем явное ожидание
        input_search.send_keys(text)