from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CartHospitalization(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'

    # Локатор с использованием normalize-space() для игнорирования пробелов
    CART_HOSPITALIZATION = ("xpath", "//h4[normalize-space()='Госпитализация']")

    def click_cart_hospitalization(self):
        element = self.wait.until(EC.element_to_be_clickable(self.CART_HOSPITALIZATION))
        self.driver.execute_script("arguments[0].click();", element)

