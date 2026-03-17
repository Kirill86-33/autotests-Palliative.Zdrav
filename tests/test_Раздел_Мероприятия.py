from testit_python_commons.decorators import externalId, displayName
class TestCartEvents:
    @externalId("test_cart_events")
    @displayName("Карточка мероприятий")
    def test_cart_events(self, card_events):  
        card_events.open()
        card_events.click_events()
