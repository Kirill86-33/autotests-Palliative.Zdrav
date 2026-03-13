from pages.base_page import BasePage



class TagNews(BasePage):
    PAGE_URL = 'https://palliative.zdrav.mosreg.ru/news'
    
    TAG_NEWS = ("xpath", "//div//span[text()='#инновации_развития']")  
    

    
    
    def click_tag_news(self):
       tag_news = self.driver.find_element(*self.TAG_NEWS)
       self.driver.execute_script("arguments[0].click();", tag_news)
