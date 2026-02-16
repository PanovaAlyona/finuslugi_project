from pages.home_page import HomePage


class DepositPage:

    def check_deposit_calculator(self):
        homepage = HomePage()
        homepage.open()
        homepage.open_all_products()
        homepage.open_products_by_name('Все вклады')
