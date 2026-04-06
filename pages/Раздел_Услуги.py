from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CardService(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'


    CARD_SERVICE = ("xpath","//div//h4[text()='Услуги']") 
    CARD_INPATIENT_CARE = ("xpath", "//div//h4[text()='Стационарная помощь']")


    def wait_for_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.CARD_SERVICE))
    
    

    def click_cart_service (self):
        self.wait_for_page_load()
        element = self.wait.until(EC.element_to_be_clickable(self.CARD_SERVICE))
        self.driver.execute_script("arguments[0].click();", element)



    def click_cart_inpatient_care(self):
        element = self.wait.until(EC.element_to_be_clickable(self.CARD_INPATIENT_CARE))
        self.driver.execute_script("arguments[0].click();", element)