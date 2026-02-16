import allure

from pages.deposit_page import DepositPage
from pages.fond_page import FondPage
from pages.home_page import HomePage
from pages.kasko_page import KaskoPage


@allure.epic("Finuslugi")
@allure.feature("Вклады")
@allure.title("Проверить соответствие предложения по вкладам для выбранных фильтров")
def test_deposit_calculator(setup_browser):
    homepage = HomePage()
    homepage.open()
    deposit = DepositPage()
    deposit.check_deposit_calculator()

@allure.epic("Finuslugi")
@allure.feature("Фонды")
@allure.title("Проверить соответствие предложения по фондам для выбранных фильтров")
def test_fond_calculator(setup_browser):
    homepage = HomePage()
    homepage.open()
    fond = FondPage()
    fond.check_fond_calculator()
#
# @allure.epic("Finuslugi")
# @allure.feature("Долгосрочные сбережения")
# @allure.title("Проверить соответствие предложения по долгосрочным сбережениям для выбранных фильтров")
# def test_pds_calculator(setup_browser):
#     homepage = HomePage()
#     homepage.open()
#
@allure.epic("Finuslugi")
@allure.feature("Каско")
@allure.title("Проверить подгрузку данных о машине по номеру в калькуляторе Каско")
def test_kasko_calculator(setup_browser):
    homepage = HomePage()
    homepage.open()
    kasko = KaskoPage()
    kasko.check_kasko_calculator()
#
# @allure.epic("Finuslugi")
# @allure.feature("ОСАГО")
# @allure.title("Проверить подгрузку данных о машине по номеру в калькуляторе ОСАГО")
# def test_osago_calculator(setup_browser):
#     homepage = HomePage()
#     homepage.open()
#
# @allure.epic("Finuslugi")
# @allure.feature("Ипотечное страхование")
# @allure.title("Проверить установленные фильтры в списке предложений для страхования ипотеки")
# def test_mortgage_calculator(setup_browser):
#     homepage = HomePage()
#     homepage.open()
#
# @allure.epic("Finuslugi")
# @allure.feature("Страхование имущества физических лиц")
# @allure.title("Проверить установленные фильтры в списке предложений для страхования имущества физических лиц")
# def test_property_calculator(setup_browser):
#     homepage = HomePage()
#     homepage.open()