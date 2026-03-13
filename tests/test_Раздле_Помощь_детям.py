class TestCartHelpChildren:
    
    def test_cart_help_children(self, card_help_children):  
        card_help_children.open()
        card_help_children.click_cart_help()
        card_help_children.click_cart_help_palliative()
        