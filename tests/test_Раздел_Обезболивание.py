class TestCartPainRelief:
    
    def test_cart_pain_relief(self, card_relief_pain):  
        card_relief_pain.open()
        card_relief_pain.click_cart_pain_relief()
        card_relief_pain.click_button_tab()