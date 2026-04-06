from testit_python_commons.decorators import externalId, displayName
class TestCartEventsSearch:
    @externalId("test_cart_events_search_city")
    @displayName("Поиск мероприятий по городу")
    def test_cart_events_search(self, search_city):
        search_city.open()
        import time
        time.sleep(3)
        print(search_city.driver.page_source[:3000])
        search_city.enter_city("Балашиха")
        search_city.click_button_city()