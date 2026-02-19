from poetry.console.commands import self
from selene import browser, by, be, have, query
from pages.home_page import HomePage


class DepositPage:

    def input_deposit_amount(self, amount):
        amount_input = browser.element(by.xpath("//label[span[text()='Сумма']]/input"))
        amount_input.should(be.visible).click()
        amount_input.type(amount)

    def check_deposit_period(self, period):
        browser.element(".finkit-select__icon .private-icon").should(be.visible).click()
        option = browser.element(
            by.xpath(f"//span[@class='finkit-dropdown-option__label' and text()='{period}']"))
        option.should(be.visible).click()

    def show_deposit_offers(self):
        browser.element(by.xpath("//span[starts-with(text(), 'Показать')]")).click()

    def open_deposit_offer(self):
        offers = browser.all("[data-testid='deposits-item']")

        # Пропускаем первое рекламное предложение, если предложений больше одного
        if len(offers) >= 2:
            button = offers[1].element(by.xpath(".//span[text()='Подробнее']"))
            button.click()
        else:
            button = offers[0].element(by.xpath(".//span[text()='Подробнее']"))
            button.click()

    def check_offer_contains_filter(self, amount, period):
        browser.element(by.xpath("//button[normalize-space()='Настройки вклада']")).should(be.visible)
        element = browser.element("input[placeholder='Сумма']")
        actual_value = element.get(query.value).replace("\xa0", " ")
        assert actual_value == amount
        browser.element("span._label_2qe4q_137").should(have.text(period))

    def check_deposit_calculator(self, filters: dict):
        homepage = HomePage()
        homepage.open_all_products()
        homepage.open_products_by_name('Все вклады')

        self.input_deposit_amount(filters['amount'])
        self.check_deposit_period(filters['period'])
        self.show_deposit_offers()
        self.open_deposit_offer()
        self.check_offer_contains_filter(filters['amount_check'], filters['period_check'])



