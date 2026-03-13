class TestMaterials:
    
    def test_materials(self, button_all_materials):  # Фикстура автоматически передаст login_page
        button_all_materials .open()
        button_all_materials .click_button_materials()
       