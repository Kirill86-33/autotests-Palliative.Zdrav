from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC



class CardPatientSchool(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'


    CARD_PATIENT_SCHOOL = ("xpath","//div//h4[text()='Школа паллиативного пациента']") 
    CARD_NUTRITION_RULES = ("xpath", "//div//h4[text()='Основные правила питания']")


    def wait_for_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.CARD_PATIENT_SCHOOL))



    def click_cart_patient_school (self):
        self.wait_for_page_load()
        element = self.wait.until(EC.element_to_be_clickable(self.CARD_PATIENT_SCHOOL))
        self.driver.execute_script("arguments[0].click();", element)




    def click_cart_nutrition_rules(self):
        element = self.wait.until(EC.element_to_be_clickable(self.CARD_NUTRITION_RULES))
        self.driver.execute_script("arguments[0].click();", element)