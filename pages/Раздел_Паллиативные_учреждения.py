from pages.base_page import BasePage

class CardPalliativInstitutions(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'


    CARD_PALLIATIVE = ("xpath","//div//h4[text()='Паллиативные учреждения']") 
    LPU_CARD = ("xpath", "//div//h4[text()='Координационный центр паллиативной медицинской помощи Московской области']")



    def click_cart_institutions (self):  
        cart_palliative = self.driver.find_element(*self.CARD_PALLIATIVE) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_palliative)



    def click_lpu_card(self):  
        lpu_card= self.driver.find_element(*self.LPU_CARD) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", lpu_card)