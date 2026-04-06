from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CardPalliativHelp(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'

    # Более гибкие локаторы
    CARD_PALLIATIVE_HELP = ("xpath", "//h4[contains(text(), 'О паллиативной помощи')]")
    CARD_FOR_WHAT_HELP_PALLIATIVE = ("xpath", "//h4[contains(text(), 'Для чего нужна паллиативная помощь')]")

    def wait_for_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.CARD_PALLIATIVE_HELP))

    def click_cart_palliative_help(self):
        self.wait_for_page_load()
        element = self.wait.until(EC.element_to_be_clickable(self.CARD_PALLIATIVE_HELP))
        self.driver.execute_script("arguments[0].click();", element)

    def click_cart_for_what_help_palliative(self):
        element = self.wait.until(EC.element_to_be_clickable(self.CARD_FOR_WHAT_HELP_PALLIATIVE))
        self.driver.execute_script("arguments[0].click();", element)