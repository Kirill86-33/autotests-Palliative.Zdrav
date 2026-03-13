from pages.base_page import BasePage

class SearchNewsPage(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/news'


    SEARCH_FIELD = ("xpath","//div//input[@placeholder='Поиск']") 
    CARD_NEW = ("xpath","(//div//a[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 css-1k57qih'])[1]") 



    def enter_search_field(self, text):  
        input_search = self.driver.find_element(*self. SEARCH_FIELD)
        input_search.send_keys(text)



    def click_card_new(self):  
        cart_new = self.driver.find_element(*self.CARD_NEW) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", cart_new)