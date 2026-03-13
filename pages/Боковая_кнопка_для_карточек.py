from pages.base_page import BasePage

class SideButton(BasePage):
    PAGE_URL = 'https://onco.zdrav.mosreg.ru/'

    BUTTON_SIDE = ("xpath", "(//div)[147]")
   
 
  
    def click_button_search (self):  
        button_search = self.driver.find_element(*self.BUTTON_SIDE) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_search)