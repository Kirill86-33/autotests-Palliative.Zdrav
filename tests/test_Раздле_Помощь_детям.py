from testit_python_commons.decorators import externalId, displayName
class TestCartHelpChildren:
    @externalId("test_cart_help_children")
    @displayName("Карточка помощи детям")
    def test_cart_help_children(self, card_help_children):  
        card_help_children.open()
        card_help_children.click_cart_help()
        card_help_children.click_cart_help_palliative()
        