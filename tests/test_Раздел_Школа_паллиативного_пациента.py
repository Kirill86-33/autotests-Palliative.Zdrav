class TestPatientSchool:
    
    def test_cart_patient_school(self, card_patient_school):  
        card_patient_school.open()
        card_patient_school.click_cart_patient_school()
        card_patient_school.click_cart_nutrition_rules()