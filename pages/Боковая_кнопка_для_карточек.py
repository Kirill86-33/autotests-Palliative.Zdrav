from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time





class SideButton(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'



    BUTTON_SIDE = ("xpath", "//*[@id='__next']/main/div/div[2]/div[1]/div[2]/div/div/div[3]/div")
    BUTTON_CARD = ("xpath", "(//div//h4[text()='Обезболивание'])[1]")
   
 
  
    def click_button_search(self):
        button_leave = self.wait.until(EC.element_to_be_clickable(self.BUTTON_SIDE))
        self.driver.execute_script("arguments[0].click();", button_leave)


    
    def click_card (self):  
        button_card = self.driver.find_element(*self.BUTTON_CARD) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_card)