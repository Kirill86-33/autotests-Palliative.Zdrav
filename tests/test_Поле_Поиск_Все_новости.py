from testit_python_commons.decorators import externalId, displayName
class TestCardNewsPage:
    @externalId("test_card_news")
    @displayName("Поиск новости по слову 'Дети'")
    def test_card_news(self, search_news_page):  # Фикстура автоматически передаст login_page
        search_news_page.open()
        search_news_page.enter_search_field ("Дети")
        search_news_page.click_card_new()