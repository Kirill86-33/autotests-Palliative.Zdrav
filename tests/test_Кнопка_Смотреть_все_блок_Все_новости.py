from testit_python_commons.decorators import externalId, displayName
class TestWatchAll:
    @externalId("test_watch_all")
    @displayName("Кнопка 'Смотреть все' в блоке Все новости")
    def test_watch_all(self, button_watch_all):  # Фикстура автоматически передаст login_page
        button_watch_all .open()
        button_watch_all .click_button_watch ()
        