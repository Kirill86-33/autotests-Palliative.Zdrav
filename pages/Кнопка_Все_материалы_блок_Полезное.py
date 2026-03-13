from pages.base_page import BasePage

class ButtonMaterials(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/'

    BUTTON_ALL_MATERIALS = ("xpath", "(//div//a[@class='MuiTypography-root MuiTypography-body1 css-1ezscke'])[1]")
    
 

    def click_button_materials (self):  
       button_materials = self.driver.find_element(*self.BUTTON_ALL_MATERIALS) # Добавляем явное ожидание
       self.driver.execute_script("arguments[0].click();", button_materials)

