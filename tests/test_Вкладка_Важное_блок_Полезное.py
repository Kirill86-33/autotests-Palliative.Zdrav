class TestTabImportant:
    
    def test_tab_important(self, button_tab_important):  # Фикстура автоматически передаст login_page
        button_tab_important.open()
        button_tab_important.click_tab_important()