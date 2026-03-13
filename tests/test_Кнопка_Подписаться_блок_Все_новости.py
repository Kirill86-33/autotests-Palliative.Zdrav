class TestInputEmail:
    
    def test_input_email(self, button_subscribe  ):  # Фикстура автоматически передаст login_page
        button_subscribe .open()
        button_subscribe .click_button_subscribe_1()
        button_subscribe .enter_email("test@yandex.ru")
        button_subscribe .click_button_subscribe_2()