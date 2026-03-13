
class TestBidHospitalization:
    def test_bid_hospitalization(self, bid_hospitalization):
        bid_hospitalization.open()
        bid_hospitalization.enter_name ("ТЕСТ ТЕСТ")
        bid_hospitalization.enter_phone ("+73333333333")
        bid_hospitalization.click_send_button()