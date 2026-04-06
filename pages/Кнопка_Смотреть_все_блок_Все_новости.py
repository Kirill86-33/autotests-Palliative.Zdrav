from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time



class ButtonWatchAll(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'

    BUTTON_WATCH_ALL = ("xpath", "(//div//a[@class='MuiTypography-root MuiTypography-body1 css-1ezscke'])[2]")
    
 

    def click_button_watch(self):
        button = self.wait.until(EC.presence_of_element_located(self.BUTTON_WATCH_ALL))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", button)