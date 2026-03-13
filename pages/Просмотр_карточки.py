from pages.base_page import BasePage



class CartHospitalization(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'
    
    CART_HOSPITALIZATION = ("xpath", "(//div//h4[text()='Госпитализация'])[1]")  
    

    
    
    def click_cart_hospitalization(self):
       cart_hospitalization = self.driver.find_element(*self.CART_HOSPITALIZATION)
       self.driver.execute_script("arguments[0].click();", cart_hospitalization)

