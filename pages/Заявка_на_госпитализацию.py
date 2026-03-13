from pages.base_page import BasePage



class BidHospitalization(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/gospitalizatsiya/zayavka_na_gospitalizatsiy'
    

    INPUT_NAME = ("xpath", "//input[@id='title']")  
    INPUT_PHONE = ("xpath", "//div//input[@id='phone']")
    BUTTON_SEND = ("xpath", "//button[text()='Отправить']")

    
    
    
   
    def enter_name (self, name):  
        input_name = self.driver.find_element(*self. INPUT_NAME)
        input_name.send_keys(name)


    def enter_phone (self, phone):  
        input_phone = self.driver.find_element(*self. INPUT_PHONE)
        input_phone.send_keys(phone)

    
    def click_send_button(self):
        button = self.driver.find_element(*self.BUTTON_SEND)
        self.driver.execute_script("arguments[0].click();", button)