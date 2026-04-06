from testit_python_commons.decorators import externalId, displayName
import time  # добавьте импорт в начало файла, если его нет

class TestCartEvents:
    @externalId("test_cart_events")
    @displayName("Карточка мероприятий")
    def test_cart_events(self, card_events):
        card_events.open()
        time.sleep(5)  # пауза для загрузки
        print("\n--- PAGE SOURCE (первые 3000 символов) ---")
        print(card_events.driver.page_source[:3000])
        card_events.click_events()
