class TestCartPalliativeInstitutions:
    
    def test_cart_palliative_institutions(self, card_palliative_institutions):  
        card_palliative_institutions.open()
        card_palliative_institutions.click_cart_institutions()
        card_palliative_institutions.click_lpu_card()