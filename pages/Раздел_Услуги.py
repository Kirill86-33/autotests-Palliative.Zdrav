from pages.base_page import BasePage

class CardService(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'


    CARD_SERVICE = ("xpath","//div//h4[text()='Услуги']") 
    CARD_INPATIENT_CARE = ("xpath", "//div//h4[text()='Стационарная помощь']")


    def click_cart_service (self):  
        cart_service= self.driver.find_element(*self.CARD_SERVICE) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_service)


    def click_cart_inpatient_care(self):  
        cart_inpatient_care= self.driver.find_element(*self.CARD_INPATIENT_CARE) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_inpatient_care)