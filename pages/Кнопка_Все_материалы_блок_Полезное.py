from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time

class ButtonMaterials(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'


    BUTTON_ALL_MATERIALS = ("xpath", "//a[contains(text(), 'Все материалы')]")

    def click_button_materials(self):
        button = self.wait.until(EC.presence_of_element_located(self.BUTTON_ALL_MATERIALS))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", button)

