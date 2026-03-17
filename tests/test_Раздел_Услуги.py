from testit_python_commons.decorators import externalId, displayName
class TestInpatientCare:
    @externalId("test_cart_inpatient_care")
    @displayName("Карточка стационарной помощи")
    def test_cart_inpatient_care(self, card_service):  
        card_service.open()
        card_service.click_cart_service ()
        card_service.click_cart_inpatient_care()