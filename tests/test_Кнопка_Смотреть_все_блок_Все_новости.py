class TestWatchAll:
    
    def test_watch_all(self, button_watch_all):  # Фикстура автоматически передаст login_page
        button_watch_all .open()
        button_watch_all .click_button_watch ()
        