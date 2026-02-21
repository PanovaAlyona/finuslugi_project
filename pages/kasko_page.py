from selene import browser, have, be

from pages.home_page import HomePage


class KaskoPage:
    def input_number_auto(self, number):
        browser.element("#licensePlate").should(be.visible).type(number)

    def calculate(self):
        button = browser.element("#startFlowButton")
        button.should(be.visible).should(have.text("Рассчитать")).click()

    def check_data_auto_by_number(self, auto):
        browser.element("#licensePlate").should(be.visible).should(
            have.value(auto["number"])
        )
        browser.element("#brand").should(be.visible).should(have.value(auto["brand"]))
        browser.element("#model").should(be.visible).should(have.value(auto["model"]))
        browser.element("#vehicle\\.year").should(be.visible).should(
            have.value(auto["vehicle_year"])
        )
        browser.element("#vehicle\\.power").should(be.visible).should(
            have.value(auto["vehicle_power"])
        )

    def check_kasko_calculator(self, auto):
        homepage = HomePage()
        homepage.open_all_products()
        homepage.open_products_by_name("Калькулятор Каско")

        self.input_number_auto(auto["number"])
        self.calculate()
        self.check_data_auto_by_number(auto)
