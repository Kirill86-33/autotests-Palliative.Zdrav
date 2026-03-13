from pages.base_page import BasePage

class CardPainRelief(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'


    CARD_PAIN_RELIEF = ("xpath","//div//h4[text()='Обезболивание']") 
    BUTTON_TAB = ("xpath", "(//div//input[@type='checkbox'])[1]")


    def click_cart_pain_relief (self):  
        cart_relief= self.driver.find_element(*self.CARD_PAIN_RELIEF) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_relief)


    def click_button_tab(self):  
        button_tab= self.driver.find_element(*self.BUTTON_TAB) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_tab)