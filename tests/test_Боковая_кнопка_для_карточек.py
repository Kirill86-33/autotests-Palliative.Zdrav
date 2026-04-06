from testit_python_commons.decorators import externalId, displayName
import time
from selenium.webdriver.common.by import By

class TestSideButton:
    @externalId("test_side_button")
    @displayName("Боковая кнопка для карточек")
    def test_side_button(self, side_button):
        side_button.open()
        time.sleep(3)  # дать странице загрузиться
        print("\nURL:", side_button.driver.current_url)
        # Проверка элемента
        elements = side_button.driver.find_elements(By.XPATH, "//*[@id='__next']/main/div/div[2]/div[1]/div[2]/div/div/div[3]/div")
        print(f"Найдено элементов: {len(elements)}")
        if elements:
            print("Тег:", elements[0].tag_name)
            print("Класс:", elements[0].get_attribute("class"))
        side_button.click_button_search()
        side_button.click_card()
        
        