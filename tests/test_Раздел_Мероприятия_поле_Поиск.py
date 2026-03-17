from testit_python_commons.decorators import externalId, displayName
class TestCartEventsSearch:
    @externalId("test_cart_events_search_card")
    @displayName("Поиск мероприятий по названию")
    def test_cart_events_search(self, card_events_search):  
        card_events_search.open()
        card_events_search.enter_search_field("Школа")
        card_events_search.click_card_events()