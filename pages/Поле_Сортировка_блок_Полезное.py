from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class SortingPage(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/library'
    
    BUTTON_SORTING = ("xpath", "//div[text()='Сортировка:']")  
    BUTTON_BY_NAME = ("xpath", "//div[text()='По названию']")

    
    
    
    def wait_for_page_load(self):
        # Ждём, пока элемент сортировки станет видимым
        self.wait.until(EC.visibility_of_element_located(self.BUTTON_SORTING))


    def click_button_sorting(self):
        self.wait_for_page_load()
        btn = self.wait.until(EC.element_to_be_clickable(self.BUTTON_SORTING))
        self.driver.execute_script("arguments[0].click();", btn)


    def click_button_by_name(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.BUTTON_BY_NAME))
        self.driver.execute_script("arguments[0].click();", btn)