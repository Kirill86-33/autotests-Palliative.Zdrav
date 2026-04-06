from testit_python_commons.decorators import externalId, displayName
class TestButtonSorting:
    @externalId("test_button_sorting")
    @displayName("Сортировка в блоке Полезное")
    def test_button_sorting(self, button_sorting):
        button_sorting.open()
        # небольшая задержка для загрузки (можно убрать, если ожидания внутри)
        import time
        time.sleep(2)
        button_sorting.click_button_sorting()
        button_sorting.click_button_by_name()
