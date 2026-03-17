from testit_python_commons.decorators import externalId, displayName
class TestSearchUsefulPage:
    @externalId("test_search_useful")
    @displayName("Поиск в блоке Полезное")
    def test_search_useful(self, search_useful):  # Фикстура автоматически передаст login_page
        search_useful.open()
        search_useful.enter_search_field ("Уход")
        search_useful.click_card_useful ()