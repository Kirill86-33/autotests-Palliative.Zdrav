from testit_python_commons.decorators import externalId, displayName
class TestInputEmail:
    @externalId("test_input_email")
    @displayName("Подписка по email в блоке Все новости")
    def test_input_email(self, button_subscribe  ):  # Фикстура автоматически передаст login_page
        button_subscribe .open()
        button_subscribe .click_button_subscribe_1()
        button_subscribe .enter_email("test@yandex.ru")
        button_subscribe .click_button_subscribe_2()