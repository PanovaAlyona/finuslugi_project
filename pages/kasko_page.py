from pages.home_page import HomePage


class KaskoPage:

    def check_kasko_calculator(self):
        homepage = HomePage()
        homepage.open()
        homepage.open_all_products()
        homepage.open_products_by_name('Калькулятор Каско')