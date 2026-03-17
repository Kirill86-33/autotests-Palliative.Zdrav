from testit_python_commons.decorators import externalId, displayName
class TestSearchPage:
    @externalId("test_search")
    @displayName("Поиск на главной странице")
    def test_search(self, search_page):  # Фикстура автоматически передаст login_page
        search_page.open()
        search_page.click_button_search()
        search_page.enter_input_search("Услуга")