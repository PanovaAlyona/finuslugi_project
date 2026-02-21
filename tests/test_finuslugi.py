import allure
import pytest

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
@allure.story("Калькулятор вкладов")
@allure.title("Проверить соответствие предложения по вкладам для выбранных фильтров")
@allure.description("""
Тест проверяет корректность работы калькулятора вкладов:
- Установка суммы вклада (100 000 ₽)
- Выбор периода вклада (3 месяца)
- Проверка отображения выбранных параметров в результатах
""")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("calculator", "deposit", "filters")
@pytest.mark.xfail(reason="Не всегда подгружаются компоненты", strict=False)
def test_deposit_calculator(setup_browser):
    filters = {
        "amount": "100000",
        "period": "3 месяца",
        "amount_check": "100 000 ₽",
        "period_check": "3 мес",
    }
    homepage = HomePage()
    homepage.open()
    deposit = DepositPage()
    deposit.check_deposit_calculator(filters)


@allure.epic("Finuslugi")
@allure.feature("Фонды")
@allure.story("Калькулятор фондов")
@allure.title("Проверить соответствие предложения по фондам для выбранных фильтров")
@allure.description("""
Тест проверяет корректность работы калькулятора фондов:
- Выбор управляющей компании (СОЛИД Менеджмент)
- Установка уровня риска (Низкий)
- Проверка соответствия результатов выбранным фильтрам
""")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("calculator", "fond", "filters")
def test_fond_calculator(setup_browser):
    filters = {"company": "СОЛИД Менеджмент", "risk": "Низкий"}
    homepage = HomePage()
    homepage.open()
    fond = FondPage()
    fond.check_fond_calculator(filters)


@allure.epic("Finuslugi")
@allure.feature("Накопительный счет")
@allure.story("Калькулятор накопительных счетов")
@allure.title(
    "Проверить соответствие предложения по накопительным счетам для выбранных фильтров"
)
@allure.description("""
Тест проверяет корректность работы калькулятора накопительных счетов:
- Установка суммы накопления (500 000 ₽)
- Выбор периода накопления (6 месяцев)
- Проверка отображения выбранных параметров в результатах
""")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("calculator", "accumulation", "filters")
@pytest.mark.xfail(reason="Не всегда подгружаются компоненты", strict=False)
def test_accumulation_account_calculator(setup_browser):
    filters = {"amount": "500 000", "period": "6 месяцев", "period_short": "6 мес"}
    homepage = HomePage()
    homepage.open()
    accumulation = AccumulationPage()
    accumulation.check_accumulation_account_calculator(filters)


@allure.epic("Finuslugi")
@allure.feature("Каско")
@allure.story("Калькулятор страхования Каско")
@allure.title("Проверить подгрузку данных о машине по номеру в калькуляторе Каско")
@allure.description("""
Тест проверяет автоматическую подгрузку данных автомобиля по госномеру:
- Ввод госномера (У 675 РХ 38)
- Проверка автозаполнения марки (Toyota)
- Проверка автозаполнения модели (Corolla)
- Проверка года выпуска (2002)
- Проверка мощности двигателя (109 л.с.)
""")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("calculator", "kasko", "auto-fill", "vehicle-data")
def test_kasko_calculator(setup_browser):
    auto = {
        "number": "У 675 РХ 38",
        "brand": "Toyota",
        "model": "Corolla",
        "vehicle_year": "2002",
        "vehicle_power": "109",
    }
    homepage = HomePage()
    homepage.open()
    kasko = KaskoPage()
    kasko.check_kasko_calculator(auto)


@allure.epic("Finuslugi")
@allure.feature("ОСАГО")
@allure.story("Калькулятор страхования ОСАГО")
@allure.title("Проверить подгрузку данных о машине по номеру в калькуляторе ОСАГО")
@allure.description("""
Тест проверяет автоматическую подгрузку данных автомобиля по госномеру:
- Ввод госномера (У 675 РХ 38)
- Проверка автозаполнения марки (Toyota)
- Проверка автозаполнения модели (Corolla)
- Проверка года выпуска (2002)
- Проверка мощности двигателя (109 л.с.)
""")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("calculator", "osago", "auto-fill", "vehicle-data")
def test_osago_calculator(setup_browser):
    auto = {
        "number": "У 675 РХ 38",
        "brand": "Toyota",
        "model": "Corolla",
        "vehicle_year": "2002",
        "vehicle_power": "109",
    }
    homepage = HomePage()
    homepage.open()
    osago = OsagoPage()
    osago.check_osago_calculator(auto)


@allure.epic("Finuslugi")
@allure.feature("Ипотечное страхование")
@allure.story("Калькулятор ипотечного страхования")
@allure.title(
    "Проверить установленные фильтры в списке предложений для страхования ипотеки"
)
@allure.description("""
Тест проверяет корректность работы калькулятора ипотечного страхования:
- Выбор объекта страхования (Дом)
- Выбор типа страхования (Все сразу)
- Установка суммы кредита (500 000 ₽)
- Выбор банка (Сбербанк)
- Ввод даты рождения (13.12.1980)
- Выбор пола (Женский)
- Проверка соответствия результатов выбранным фильтрам
""")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("calculator", "mortgage", "filters", "insurance")
def test_mortgage_calculator(setup_browser):
    filters = {
        "object": "Дом",
        "type_insurance": "Все сразу",
        "credit": "500 000",
        "bank": "Сбербанк",
        "birthDate": "13.12.1980",
        "sex": "Женский",
    }
    homepage = HomePage()
    homepage.open()
    mortgage = MortgagePage()
    mortgage.check_mortgage_calculator(filters)


@allure.epic("Finuslugi")
@allure.feature("Страхование имущества физических лиц")
@allure.story("Калькулятор страхования имущества")
@allure.title(
    "Проверить установленные фильтры в списке предложений "
    "для страхования имущества физических лиц"
)
@allure.description("""
Тест проверяет корректность работы калькулятора страхования имущества:
- Выбор типа страхового случая (Пожар)
- Проверка соответствия результатов выбранному фильтру
""")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("calculator", "property", "filters", "insurance")
def test_property_calculator(setup_browser):
    filter = "Пожар"
    homepage = HomePage()
    homepage.open()
    property = PropertyPage()
    property.check_property_calculator(filter)
