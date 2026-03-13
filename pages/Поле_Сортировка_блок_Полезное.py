from pages.base_page import BasePage



class SortingPage(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/library'
    
    BUTTON_SORTING = ("xpath", "//div[text()='Сортировка:']")  
    BUTTON_BY_NAME = ("xpath", "//div[text()='По названию']")

    
    
    def click_button_sorting(self):
       button_sorting = self.driver.find_element(*self.BUTTON_SORTING)
       self.driver.execute_script("arguments[0].click();", button_sorting)


    def click_button_by_name(self):
       button_name = self.driver.find_element(*self.BUTTON_BY_NAME)
       self.driver.execute_script("arguments[0].click();", button_name)