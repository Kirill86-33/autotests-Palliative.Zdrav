from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CardEvents(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'

    CARD_EVENTS = ("xpath", "//h4[contains(text(),'Мероприятия')]")  # гибкий локатор

    def wait_for_page_load(self):
        # Ждём, пока лоадер исчезнет
        self.wait.until(EC.invisibility_of_element_located(("xpath", "//div[contains(@class, 'css-h2cf2p')]")))

    def click_events(self):
        self.wait_for_page_load()
        element = self.wait.until(EC.element_to_be_clickable(self.CARD_EVENTS))
        self.driver.execute_script("arguments[0].click();", element)


