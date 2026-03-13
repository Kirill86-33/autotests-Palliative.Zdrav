from pages.base_page import BasePage

class ButtonSubscribe(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/news'

    BUTTON_SUBSCRIBE_1 = ("xpath", "(//div//button[text()='Подписаться'])[1]") 
    INPUT_EMAIL = ("xpath", "//div//input[@id='email']")
    BUTTON_SUBSCRIBE_2 = ("xpath", " (//div//button[text()='Подписаться'])[2]")  





    def click_button_subscribe_1 (self):  
       button_subscribe_1 = self.driver.find_element(*self.BUTTON_SUBSCRIBE_1) # Добавляем явное ожидание
       self.driver.execute_script("arguments[0].click();", button_subscribe_1)


    def enter_email (self, email):  
        input_email = self.driver.find_element(*self. INPUT_EMAIL)
        input_email.send_keys(email)


    def click_button_subscribe_2 (self):  
       button_subscribe_2 = self.driver.find_element(*self.BUTTON_SUBSCRIBE_2) # Добавляем явное ожидание
       self.driver.execute_script("arguments[0].click();", button_subscribe_2)

