from pages.home_page import HomePage


class FondPage:

    def check_fond_calculator(self):
        homepage = HomePage()
        homepage.open()
        homepage.open_all_products()
        homepage.open_products_by_name('Паевые инвестиционные фонды')