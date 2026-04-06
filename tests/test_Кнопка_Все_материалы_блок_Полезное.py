from testit_python_commons.decorators import externalId, displayName
class TestMaterials:
    @externalId("test_materials")
    @displayName("Кнопка 'Все материалы' в блоке Полезное")
    def test_materials(self, button_all_materials):  # Фикстура автоматически передаст login_page
        button_all_materials .open()
        import time
        time.sleep(2)  # дать странице время на первичную загрузку
        print("URL:", button_all_materials.driver.current_url)
        print("Title:", button_all_materials.driver.title)
        button_all_materials .click_button_materials()
       