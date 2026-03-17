from testit_python_commons.decorators import externalId, displayName
class TestCartHelpChildren:
    @externalId("test_cart_help_children_palliative")
    @displayName("Паллиативная помощь детям")
    def test_cart_help_children(self, card_palliative_help):  
        card_palliative_help.open()
        card_palliative_help.click_cart_palliative_help()
        card_palliative_help.click_cart_for_what_help_palliative ()