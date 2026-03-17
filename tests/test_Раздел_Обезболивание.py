from testit_python_commons.decorators import externalId, displayName
class TestCartPainRelief:
    @externalId("test_cart_pain_relief")
    @displayName("Карточка обезболивания")
    def test_cart_pain_relief(self, card_relief_pain):  
        card_relief_pain.open()
        card_relief_pain.click_cart_pain_relief()
        card_relief_pain.click_button_tab()