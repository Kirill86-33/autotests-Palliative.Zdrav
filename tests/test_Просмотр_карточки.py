from testit_python_commons.decorators import externalId, displayName

class TestCartHospitalization:
    @externalId("test_cart_hospitalization")
    @displayName("Карточка госпитализации")
    def test_cart_hospitalization(self, cart_hospitalization):
        cart_hospitalization.open()
        # Небольшая пауза для загрузки (можно убрать, если ожидания внутри)
        import time
        time.sleep(2)
        cart_hospitalization.click_cart_hospitalization()
    