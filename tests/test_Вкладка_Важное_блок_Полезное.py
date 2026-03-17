from testit_python_commons.decorators import externalId, displayName
class TestTabImportant:
    @externalId("test_tab_important")
    @displayName("Вкладка 'Важное' в блоке Полезное")
    def test_tab_important(self, button_tab_important):  # Фикстура автоматически передаст login_page
        button_tab_important.open()
        button_tab_important.click_tab_important()