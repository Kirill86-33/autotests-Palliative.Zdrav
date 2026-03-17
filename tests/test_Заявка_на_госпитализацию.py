from testit_python_commons.decorators import externalId, displayName
class TestBidHospitalization:
    @externalId("test_bid_hospitalization")
    @displayName("Заявка на госпитализацию")
    def test_bid_hospitalization(self, bid_hospitalization):
        bid_hospitalization.open()
        bid_hospitalization.enter_name ("ТЕСТ ТЕСТ")
        bid_hospitalization.enter_phone ("+73333333333")
        bid_hospitalization.click_send_button()