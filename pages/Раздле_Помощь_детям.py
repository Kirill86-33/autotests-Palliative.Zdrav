from pages.base_page import BasePage

class CardHelpChildren(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'


    CARD_HELP_CHILDREN = ("xpath","//div//h4[text()='Помощь детям']") 
    CARD_HELP_PALLIATIVE = ("xpath", "//div//h4[text()='Где и как получить паллиативную помощь']")


    def click_cart_help (self):  
        cart_children= self.driver.find_element(*self.CARD_HELP_CHILDREN) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_children)


    def click_cart_help_palliative (self):  
        cart_palliative= self.driver.find_element(*self.CARD_HELP_PALLIATIVE) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_palliative)