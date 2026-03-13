from pages.base_page import BasePage

class ButtonWatchAll(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'

    BUTTON_WATCH_ALL = ("xpath", "(//div//a[@class='MuiTypography-root MuiTypography-body1 css-1ezscke'])[2]")
    
 

    def click_button_watch (self):  
       button_watch_all = self.driver.find_element(*self.BUTTON_WATCH_ALL) # Добавляем явное ожидание
       self.driver.execute_script("arguments[0].click();", button_watch_all)