class TestCardNewsPage:
    
    def test_card_news(self, search_news_page):  # Фикстура автоматически передаст login_page
        search_news_page.open()
        search_news_page.enter_search_field ("Дети")
        search_news_page.click_card_new()