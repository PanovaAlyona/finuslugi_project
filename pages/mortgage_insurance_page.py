from datetime import datetime

from dateutil.relativedelta import relativedelta
from selene import browser, be, have, by

from pages.home_page import HomePage


class MortgagePage:
    def filter_mortgage_offer(self, filters):
        fields = [
            {"name": "propertyType"},
            {"name": "bankCode"},
            {"name": "creditSum"},
            {"name": "birthDate"},
            {"name": "sex"},
        ]
        for field in fields:
            browser.element(f'[name="{field["name"]}"]').should(be.visible).should(
                be.clickable
            )

        browser.element('[name="propertyType"]').should(be.clickable).click()
        browser.element('//div[contains(@class, "Dropdown__opened")]').should(
            be.visible
        )
        obj = filters["object"]
        browser.element(f'//*[text()="{obj}"]').should(be.visible).click()
        browser.element('//input[@name="propertyType"]').should(
            have.value(filters["object"])
        )

        browser.element('//div[@title="Вид страхования"]').should(be.visible).should(
            be.clickable
        ).click()
        type_insurance = filters["type_insurance"]
        browser.element(f'//*[text()="{type_insurance}"]').should(be.visible).click()

        browser.element('[name="creditSum"]').should(be.visible).clear().type(
            filters["credit"]
        )

        browser.element('[name="bankCode"]').should(be.clickable)
        browser.element('//div[@title="В каком банке кредит"]').should(
            be.visible
        ).click()
        bank = filters["bank"]
        browser.element(f'//*[text()="{bank}"]').should(be.visible).click()

        browser.element('[name="birthDate"]').should(be.visible).clear().type(
            filters["birthDate"]
        )

        browser.element('[name="sex"]').should(be.visible).should(be.clickable).click()
        sex = filters["sex"]
        browser.element(f'//*[text()="{sex}"]').should(be.visible).click()

        browser.element(by.text("Рассчитать")).should(be.visible).should(
            be.clickable
        ).click()

    def check_filters_in_search(self, filters):
        browser.element('//h3[text()="Параметры"]').should(be.visible)
        browser.element(
            '//div[text()="Тип недвижимости:"]/following-sibling::div'
        ).should(have.text(filters["object"]))
        browser.element('//div[text()="Банк:"]/following-sibling::div').should(
            have.text(filters["bank"])
        )
        browser.element('//div[text()="Остаток долга:"]/following-sibling::div').should(
            have.text(filters["credit"] + " ₽")
        )

        birth_date_str = filters["birthDate"]
        birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y").date()
        today = datetime.now().date()
        age = relativedelta(today, birth_date).years

        sex_text = filters["sex"]
        browser.element('//div[text()="Пол и возраст:"]/following-sibling::div').should(
            have.text(f"{sex_text}, {age} лет")
        )
        type_insurance = filters["type_insurance"]
        browser.element(f'//button[.//span[text()="{type_insurance}"]]').should(
            have.css_class("Chip__selected__94c0a")
        )

    def check_mortgage_calculator(self, filters):
        homepage = HomePage()
        homepage.open_all_products()
        homepage.open_products_by_name("Калькулятор страхования ипотеки")

        self.filter_mortgage_offer(filters)
        self.check_filters_in_search(filters)
