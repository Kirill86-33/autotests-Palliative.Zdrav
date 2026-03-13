import pytest
from selenium import webdriver
from pages.Поле_Поиск_Главная_страница import SearchField
from pages.Просмотр_карточки import CartHospitalization
from pages.Заявка_на_госпитализацию import BidHospitalization
from pages.Боковая_кнопка_для_карточек import SideButton
from pages.Раздле_Помощь_детям import CardHelpChildren
from pages.Раздел_О_паллиативной_помощи import CardPalliativHelp
from pages.Раздел_Паллиативные_учреждения import CardPalliativInstitutions
from pages.Раздел_Услуги import CardService
from pages.Раздел_Обезболивание import CardPainRelief
from pages.Раздел_Школа_паллиативного_пациента import CardPatientSchool
from pages.Раздел_Мероприятия import CardEvents
from pages.Раздел_Мероприятия_поле_Поиск import CardEventsSearch
from pages.Раздел_Мероприятия_поле_Поиск_по_городу import EventsSearchCity
from pages.Кнопка_Все_материалы_блок_Полезное import ButtonMaterials
from pages.Поле_Поиск_блок_Полезное import SearchUsefulPage
from pages.Вкладка_Важное_блок_Полезное import TabImportant
from pages.Поле_Сортировка_блок_Полезное import SortingPage
from pages.Кнопка_Смотреть_все_блок_Все_новости import ButtonWatchAll
from pages.Поле_Поиск_Все_новости import SearchNewsPage
from pages.Тег_блок_Все_новости import TagNews
from pages.Кнопка_Подписаться_блок_Все_новости import ButtonSubscribe



@pytest.fixture # Общие настройки экрана для всех фикстур
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def search_page(driver):
    return SearchField (driver)


@pytest.fixture
def cart_hospitalization (driver):
    return CartHospitalization (driver)


@pytest.fixture
def bid_hospitalization (driver):
    return BidHospitalization (driver)


@pytest.fixture
def side_button(driver):
    return SideButton(driver)


@pytest.fixture
def card_help_children(driver):
    return CardHelpChildren(driver)


@pytest.fixture
def card_palliative_help(driver):
    return CardPalliativHelp(driver)


@pytest.fixture
def card_palliative_institutions(driver):
    return CardPalliativInstitutions(driver)

@pytest.fixture
def card_service(driver):
    return CardService(driver)


@pytest.fixture
def card_relief_pain(driver):
    return CardPainRelief(driver)


@pytest.fixture
def card_patient_school (driver):
    return CardPatientSchool(driver)

@pytest.fixture
def card_events (driver):
    return CardEvents (driver)


@pytest.fixture
def card_events_search (driver):
    return CardEventsSearch (driver)


@pytest.fixture
def search_city (driver):
    return EventsSearchCity (driver)


@pytest.fixture
def button_all_materials (driver):
    return ButtonMaterials (driver)


@pytest.fixture
def search_useful (driver):
    return SearchUsefulPage (driver)


@pytest.fixture
def button_tab_important (driver):
    return TabImportant (driver)


@pytest.fixture
def button_sorting (driver):
    return SortingPage (driver)


@pytest.fixture
def button_watch_all (driver):
    return ButtonWatchAll (driver)


@pytest.fixture
def search_news_page (driver):
    return SearchNewsPage (driver)


@pytest.fixture
def tag_news (driver):
    return TagNews (driver)


@pytest.fixture
def button_subscribe (driver):
    return ButtonSubscribe (driver)