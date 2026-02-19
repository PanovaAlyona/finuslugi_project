from selene import browser, be, have, by
from selenium.webdriver.common.by import By

from pages.home_page import HomePage


class AccumulationPage:

    def filter_accumulation_account(self, filters):
        amount_input = browser.element('[data-qa="filter-amount-input"] input')
        amount_input.should(be.visible).clear().type(filters['amount'])

        term_selector = browser.element('.finkit-select__activator')
        term_selector.should(be.visible).click()

        browser.all('.finkit-dropdown-option__label').element_by(have.text(filters['period'])).click()

        browser.element(by.xpath("//span[starts-with(text(), 'Показать')]")).click()

    def open_offer(self):
        browser.all(by.text('Подробнее'))[1].click()

    def check_filters_in_offer(self, filters):
        browser.element('input[placeholder="Сумма"]').with_(timeout=10).should(be.visible)

        check_amount = filters['amount'].replace(' ', ' ') + ' ₽'
        browser.element('input[placeholder="Сумма"]').should(have.attribute('value').value_containing(check_amount))

        browser.element('[aria-checked="true"]').should(have.text(filters['period_short']))

    def check_accumulation_account_calculator(self, filters):

        homepage = HomePage()
        homepage.open_all_products()
        homepage.open_products_by_name('Накопительные счета')

        self.filter_accumulation_account(filters)
        self.open_offer()
        self.check_filters_in_offer(filters)




