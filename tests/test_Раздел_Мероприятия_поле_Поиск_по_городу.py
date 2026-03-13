class TestCartEventsSearch:
    
    def test_cart_events_search(self, search_city):  
        search_city.open()
        search_city.enter_city("Балашиха")
        search_city.click_button_city()