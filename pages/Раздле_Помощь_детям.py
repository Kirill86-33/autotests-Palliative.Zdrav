from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC



class CardHelpChildren(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'


    CARD_HELP_CHILDREN = ("xpath","//div//h4[text()='Помощь детям']") 
    CARD_HELP_PALLIATIVE = ("xpath", "//div//h4[text()='Где и как получить паллиативную помощь']")

    def wait_for_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.CARD_HELP_CHILDREN))



    def click_cart_help (self):
        self.wait_for_page_load()
        element = self.wait.until(EC.element_to_be_clickable(self.CARD_HELP_CHILDREN))
        self.driver.execute_script("arguments[0].click();", element)




    def click_cart_help_palliative(self):
        element = self.wait.until(EC.element_to_be_clickable(self.CARD_HELP_PALLIATIVE))
        self.driver.execute_script("arguments[0].click();", element)