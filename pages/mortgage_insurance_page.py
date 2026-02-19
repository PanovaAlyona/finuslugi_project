from datetime import datetime

from dateutil.relativedelta import relativedelta
from selene import browser, be, have, by

from pages.home_page import HomePage


class MortgagePage:

    def filter_mortgage_offer(self, filters):
        fields = [
            {'name': 'propertyType'},
            {'name': 'bankCode'},
            {'name': 'creditSum'},
            {'name': 'birthDate'},
            {'name': 'sex'}
        ]
        for field in fields:
            browser.element(f'[name="{field["name"]}"]').should(be.visible).should(be.clickable)


        browser.element('[name="propertyType"]').click()
        browser.element('//div[contains(@class, "Dropdown__opened")]').should(be.visible)
        browser.element(f'//*[text()="{filters['object']}"]').click()
        browser.element('//input[@name="propertyType"]').should(have.value(filters['object']))

        browser.element('//div[@title="Вид страхования"]').click()
        browser.element(f'//*[text()="{filters['type_insurance']}"]').click()

        browser.element('[name="creditSum"]').clear().type(filters['credit'])

        browser.element('[name="bankCode"]').should(be.clickable)
        browser.element('//div[@title="В каком банке кредит"]').click()
        browser.element(f'//*[text()="{filters['bank']}"]').click()

        browser.element('[name="birthDate"]').clear().type(filters['birthDate'])

        browser.element('[name="sex"]').click()
        browser.element(f'//*[text()="{filters['sex']}"]').click()

        browser.element(by.text('Рассчитать')).click()

    def check_filters_in_search(self, filters):

        browser.element('//h3[text()="Параметры"]').should(be.visible)
        browser.element('//div[text()="Тип недвижимости:"]/following-sibling::div').should(have.text(filters['object']))
        browser.element('//div[text()="Банк:"]/following-sibling::div').should(have.text(filters['bank']))
        browser.element(
            '//div[text()="Остаток долга:"]/following-sibling::div'
            ).should(have.text(filters['credit']+' ₽'))

        birth_date_str = filters['birthDate']
        birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y").date()
        today = datetime.now().date()
        age = relativedelta(today, birth_date).years

        browser.element('//div[text()="Пол и возраст:"]/following-sibling::div').should(
            have.text(f'{filters['sex']}, {age} лет'))
        browser.element(f'//button[.//span[text()="{filters['type_insurance']}"]]') \
            .should(have.css_class('Chip__selected__94c0a'))


    def check_mortgage_calculator(self, filters):
        homepage = HomePage()
        homepage.open_all_products()
        homepage.open_products_by_name('Калькулятор страхования ипотеки')

        self.filter_mortgage_offer(filters)
        self.check_filters_in_search(filters)

