import allure

from pages.accumulation_account_page import AccumulationPage
from pages.deposit_page import DepositPage
from pages.fond_page import FondPage
from pages.home_page import HomePage
from pages.kasko_page import KaskoPage
from pages.mortgage_insurance_page import MortgagePage
from pages.osago_page import OsagoPage
from pages.property_insurance_page import PropertyPage


@allure.epic("Finuslugi")
@allure.feature("Вклады")
@allure.title("Проверить соответствие предложения по вкладам для выбранных фильтров")
def test_deposit_calculator(setup_browser):
    filters = {
        "amount":"100000",
        "period":"3 месяца",
        "amount_check": "100 000 ₽",
        "period_check": "3 мес"
    }
    homepage = HomePage()
    homepage.open()
    deposit = DepositPage()
    deposit.check_deposit_calculator(filters)

@allure.epic("Finuslugi")
@allure.feature("Фонды")
@allure.title("Проверить соответствие предложения по фондам для выбранных фильтров")
def test_fond_calculator(setup_browser):
    filters = {
        "company": 'СОЛИД Менеджмент',
        "risk": "Низкий"
    }
    homepage = HomePage()
    homepage.open()
    fond = FondPage()
    fond.check_fond_calculator(filters)

@allure.epic("Finuslugi")
@allure.feature("Накопительный счет")
@allure.title("Проверить соответствие предложения по накопительным счетам для выбранных фильтров")
def test_accumulation_account_calculator(setup_browser):
    filters = {
        "amount":"500 000",
        "period": "6 месяцев",
        "period_short": "6 мес"
    }
    homepage = HomePage()
    homepage.open()
    accumulation = AccumulationPage()
    accumulation.check_accumulation_account_calculator(filters)

@allure.epic("Finuslugi")
@allure.feature("Каско")
@allure.title("Проверить подгрузку данных о машине по номеру в калькуляторе Каско")
def test_kasko_calculator(setup_browser):
    auto = {
        "number": 'У 675 РХ 38',
        "brand": "Toyota",
        "model": 'Corolla',
        "vehicle_year": '2002',
        "vehicle_power": '109'
    }
    homepage = HomePage()
    homepage.open()
    kasko = KaskoPage()
    kasko.check_kasko_calculator(auto)

@allure.epic("Finuslugi")
@allure.feature("ОСАГО")
@allure.title("Проверить подгрузку данных о машине по номеру в калькуляторе ОСАГО")
def test_osago_calculator(setup_browser):
    auto = {
        "number": 'У 675 РХ 38',
        "brand": "Toyota",
        "model": 'Corolla',
        "vehicle_year": '2002',
        "vehicle_power": '109'
    }
    homepage = HomePage()
    homepage.open()
    osago = OsagoPage()
    osago.check_osago_calculator(auto)

@allure.epic("Finuslugi")
@allure.feature("Ипотечное страхование")
@allure.title("Проверить установленные фильтры в списке предложений для страхования ипотеки")
def test_mortgage_calculator(setup_browser):
    filters = {
        "object": "Дом",
        "type_insurance": "Все сразу",
        "credit": "500 000",
        "bank": "Сбербанк",
        "birthDate": "13.12.1980",
        "sex": "Женский"
    }
    homepage = HomePage()
    homepage.open()
    mortgage = MortgagePage()
    mortgage.check_mortgage_calculator(filters)

@allure.epic("Finuslugi")
@allure.feature("Страхование имущества физических лиц")
@allure.title("Проверить установленные фильтры в списке предложений для страхования имущества физических лиц")
def test_property_calculator(setup_browser):
    filter = 'Пожар'
    homepage = HomePage()
    homepage.open()
    property = PropertyPage()
    property.check_property_calculator(filter)