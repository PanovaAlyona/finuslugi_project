from selene import browser, by, have, be

from pages.home_page import HomePage


class FondPage:

    def check_fond_company(self, company):
        browser.element(
            '//*[contains(@class, "finkit-select__placeholder") and text()="Управляющая Компания"]/..').click()

        browser.element(
            f'//li[contains(., "{company}")]//span[contains(@class, "finkit-common-marker--checkbox")]'
        ).click()

    def check_fond_risk(self, risk):
        browser.element(
            '//*[contains(@class, "finkit-select__placeholder") and text()="Риск"]/..').click()

        browser.element(
            f'//li[contains(., "{risk}")]//span[contains(@class, "finkit-common-marker--checkbox")]'
        ).click()

    def show_fond_offers(self):
        browser.element(by.text('Показать')).click()

    def show_fond_one_offer(self):
        browser.all(by.text('Подробнее'))[0].click()

    def check_company_in_fond(self, company):
        browser.element(f"//div[contains(text(), '{company}')]").should(be.existing)

    def check_risk_in_fond(self, risk):
        browser.element(f"//div[contains(text(), '{risk}')]").should(be.existing)

    def check_fond_calculator(self, filters):
        homepage = HomePage()
        homepage.open_all_products()
        homepage.open_products_by_name('Паевые инвестиционные фонды')

        self.check_fond_company(filters['company'])
        self.check_fond_risk(filters['risk'])
        self.show_fond_offers()
        self.show_fond_one_offer()
        self.check_company_in_fond(filters['company'])
        self.check_risk_in_fond(filters['risk'])





