from testit_python_commons.decorators import externalId, displayName


class TestSearchPage:
    @externalId("test_search")
    @displayName("Поиск на главной странице")
    def test_search(self, search_page):
        search_page.open()
        search_page.click_button_search()   # теперь внутри есть ожидание поля
        search_page.enter_input_search("Услуга")