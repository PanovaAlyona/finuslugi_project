from selene import browser, have, be, by

from pages.home_page import HomePage


class OsagoPage:
    def input_number_auto(self, number):
        browser.element('[name="licensePlate"]').should(be.visible).type(number)

    def calculate(self):
        button = browser.element(by.text("Рассчитать"))
        button.should(be.visible).should(be.clickable).click()

    def check_data_auto_by_number(self, auto):
        browser.element("[name='licensePlate']").should(be.visible).should(
            have.value(auto["number"])
        )
        browser.element("[name='vehicle.brand']").should(be.visible).should(
            have.value(auto["brand"])
        )
        browser.element("[name='vehicle.model']").should(be.visible).should(
            have.value(auto["model"])
        )
        browser.element("[name='vehicle.year']").should(be.visible).should(
            have.value(auto["vehicle_year"])
        )
        browser.element("[name='vehicle.modification']").should(be.visible).should(
            have.value(auto["vehicle_power"])
        )

    def check_osago_calculator(self, auto):
        homepage = HomePage()
        homepage.open_all_products()
        homepage.open_products_by_name("Калькулятор ОСАГО")
        self.input_number_auto(auto["number"])
        self.calculate()
        self.check_data_auto_by_number(auto)
