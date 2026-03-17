from testit_python_commons.decorators import externalId, displayName
class TestSideButton:
    @externalId("test_side_button")
    @displayName("Боковая кнопка для карточек")
    def test_side_button(self, side_button):  # Фикстура автоматически передаст login_page
        side_button.open()
        side_button.click_button_search()
        side_button.click_button_search()
        side_button.click_button_search()