from pages.base_page import BasePage

class CardPalliativHelp(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'


    CARD_PALLIATIVE_HELP = ("xpath","//div//h4[text()='О паллиативной помощи']") 
    CARD_FOR_WHAT_HELP_PALLIATIVE = ("xpath", "//div//h4[text()='Для чего нужна паллиативная помощь']")



    def click_cart_palliative_help (self):  
        cart_palliative_help= self.driver.find_element(*self.CARD_PALLIATIVE_HELP) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_palliative_help)



    def click_cart_for_what_help_palliative (self):  
        cart_palliative= self.driver.find_element(*self.CARD_FOR_WHAT_HELP_PALLIATIVE) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_palliative)