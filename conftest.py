import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.Тег_блок_Все_новости import TagNews




@pytest.fixture
def driver():
    # Автоматически скачивает подходящий ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()



@pytest.fixture
def search_page(driver):
    from pages.Поле_Поиск_Главная_страница import SearchField
    return SearchField (driver)



@pytest.fixture
def cart_hospitalization(driver):
    from pages.Просмотр_карточки import CartHospitalization
    return CartHospitalization (driver)




@pytest.fixture
def bid_hospitalization(driver):
    from pages.Заявка_на_госпитализацию import BidHospitalization
    return BidHospitalization (driver)



@pytest.fixture
def side_button(driver):
    from pages.Боковая_кнопка_для_карточек import SideButton
    return SideButton(driver)



@pytest.fixture
def card_help_children(driver):
    from pages.Раздле_Помощь_детям import CardHelpChildren
    return CardHelpChildren (driver)





@pytest.fixture
def card_palliative_help(driver):
    from pages.Раздел_О_паллиативной_помощи import CardPalliativHelp
    return CardPalliativHelp (driver)




@pytest.fixture
def card_palliative_institutions(driver):
    from pages.Раздел_Паллиативные_учреждения import CardPalliativInstitutions
    return CardPalliativInstitutions (driver)



@pytest.fixture
def card_service (driver):
    from pages.Раздел_Услуги import CardService
    return CardService (driver)




@pytest.fixture
def card_patient_school (driver):
    from pages.Раздел_Школа_паллиативного_пациента import CardPatientSchool
    return CardPatientSchool (driver)



@pytest.fixture
def card_events(driver):
    from pages.Раздел_Мероприятия import CardEvents
    return CardEvents(driver)




@pytest.fixture
def card_events_search (driver):
    from pages.Раздел_Мероприятия_поле_Поиск import CardEventsSearch
    return CardEventsSearch (driver)




@pytest.fixture
def search_city (driver):
    from pages.Раздел_Мероприятия_поле_Поиск_по_городу import EventsSearchCity
    return EventsSearchCity (driver)





@pytest.fixture
def button_all_materials (driver):
    from pages.Кнопка_Все_материалы_блок_Полезное import ButtonMaterials
    return ButtonMaterials(driver)




@pytest.fixture
def search_useful (driver):
    from pages.Поле_Поиск_блок_Полезное import SearchUsefulPage
    return SearchUsefulPage(driver)





@pytest.fixture
def button_tab_important (driver):
    from pages.Вкладка_Важное_блок_Полезное import TabImportant
    return TabImportant (driver)



@pytest.fixture
def button_sorting (driver):
    from pages.Поле_Сортировка_блок_Полезное import SortingPage
    return SortingPage (driver)





@pytest.fixture
def button_watch_all  (driver):
    from pages.Кнопка_Смотреть_все_блок_Все_новости import ButtonWatchAll
    return ButtonWatchAll (driver)



@pytest.fixture
def search_news_page  (driver):
    from pages.Поле_Поиск_Все_новости import SearchNewsPage
    return SearchNewsPage (driver)



@pytest.fixture
def tag_news (driver):
    from pages.Тег_блок_Все_новости import TagNews
    return TagNews (driver)




@pytest.fixture
def button_subscribe (driver):
    from pages.Кнопка_Подписаться_блок_Все_новости import ButtonSubscribe
    return ButtonSubscribe (driver)



