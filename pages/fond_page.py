from selene import browser, by, have, be

from pages.home_page import HomePage


class FondPage:
    def check_fond_company(self, company):
        xpath_company = (
            '//*[contains(@class, "finkit-select__placeholder") '
            'and text()="Управляющая Компания"]/..'
        )
        browser.element(xpath_company).should(be.visible).should(be.clickable).click()

        xpath_checkbox = (
            f'//li[contains(., "{company}")]//span[contains(@class, '
            '"finkit-common-marker--checkbox")]'
        )
        browser.element(xpath_checkbox).should(be.visible).should(be.clickable).click()

    def check_fond_risk(self, risk):
        xpath_risk = (
            '//*[contains(@class, "finkit-select__placeholder") '
            'and text()="Риск"]/..'
        )
        browser.element(xpath_risk).should(be.visible).should(be.clickable).click()

        xpath_checkbox = (
            f'//li[contains(., "{risk}")]//span[contains(@class, '
            '"finkit-common-marker--checkbox")]'
        )
        browser.element(xpath_checkbox).should(be.visible).should(be.clickable).click()

    def show_fond_offers(self):
        browser.element(by.text("Показать")).should(be.visible).should(
            be.clickable
        ).click()

    def show_fond_one_offer(self):
        browser.all(by.text("Подробнее")).should(have.size_greater_than_or_equal(1))
        browser.all(by.text("Подробнее"))[0].should(be.visible).should(
            be.clickable
        ).click()

    def check_company_in_fond(self, company):
        browser.element(f"//div[contains(text(), '{company}')]").should(be.visible)

    def check_risk_in_fond(self, risk):
        browser.element(f"//div[contains(text(), '{risk}')]").should(be.visible)

    def check_fond_calculator(self, filters):
        homepage = HomePage()
        homepage.open_all_products()
        homepage.open_products_by_name("Паевые инвестиционные фонды")

        self.check_fond_company(filters["company"])
        self.check_fond_risk(filters["risk"])
        self.show_fond_offers()
        self.show_fond_one_offer()
        self.check_company_in_fond(filters["company"])
        self.check_risk_in_fond(filters["risk"])
