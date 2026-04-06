from testit_python_commons.decorators import externalId, displayName
class TestCartPalliativeInstitutions:
    @externalId("test_cart_palliative_institutions")
    @displayName("Карточка паллиативных учреждений")
    def test_cart_palliative_institutions(self, card_palliative_institutions):  
        card_palliative_institutions.open()
        card_palliative_institutions.click_cart_institutions()
        card_palliative_institutions.click_lpu_card()



