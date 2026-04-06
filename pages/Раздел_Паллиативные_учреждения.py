from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CardPalliativInstitutions(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'


    CARD_PALLIATIVE = ("xpath","//div//h4[text()='Паллиативные учреждения']") 
    LPU_CARD = ("xpath", "//div//h4[text()='Координационный центр паллиативной медицинской помощи Московской области']")


    def wait_for_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.CARD_PALLIATIVE))



    def click_cart_institutions (self):
        self.wait_for_page_load()
        element = self.wait.until(EC.element_to_be_clickable(self.CARD_PALLIATIVE))
        self.driver.execute_script("arguments[0].click();", element)



    def click_lpu_card(self):
        element = self.wait.until(EC.element_to_be_clickable(self.LPU_CARD))
        self.driver.execute_script("arguments[0].click();", element)