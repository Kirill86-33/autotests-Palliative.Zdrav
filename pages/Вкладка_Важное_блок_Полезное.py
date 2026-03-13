from pages.base_page import BasePage



class TabImportant(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/library'
    

    TAB_IMPORTANT = ("xpath", "//div//button[text()='Важное']")  
    

    
    def click_tab_important(self):
        button_tab = self.driver.find_element(*self.TAB_IMPORTANT)
        self.driver.execute_script("arguments[0].click();", button_tab)