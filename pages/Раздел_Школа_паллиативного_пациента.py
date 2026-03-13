from pages.base_page import BasePage

class CardPatientSchool(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'


    CARD_PATIENT_SCHOOL = ("xpath","//div//h4[text()='Школа паллиативного пациента']") 
    CARD_NUTRITION_RULES = ("xpath", "//div//h4[text()='Основные правила питания']")


    def click_cart_patient_school(self):  
        cart_patient= self.driver.find_element(*self.CARD_PATIENT_SCHOOL) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_patient)


    def click_cart_nutrition_rules(self):  
        cart_nutrition= self.driver.find_element(*self.CARD_NUTRITION_RULES) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_nutrition)