from selene import browser, by, have, be

from pages.home_page import HomePage


class PropertyPage:


    def verify_fire_chip_in_all_offers(self, filter):

        offers = browser.all('[data-testid="offer-item"]')
        offers_count = len(offers)
        success_count = 0

        for i, offer in enumerate(offers):

            fire_chips = offer.all('.OfferItem_item__chips__chip__hYGhf').element_by(have.exact_text(filter))

            if fire_chips.matching(be.present):
                success_count += 1

        assert success_count == offers_count

    def filter_offers(self, filter):
        browser.element('.Select__input__c4c9b').with_(timeout=10).should(be.present)
        browser.element('.Insurance_container__filter__4U5lz .Select__input__c4c9b').click()

        fire_option = browser.element(f'//*[contains(text(), "{filter}")]/ancestor::div[contains(@class, "option")]')
        fire_option.should(be.visible).click()

        browser.element(by.xpath("//span[starts-with(text(), 'Показать')]")).click()

    def check_property_calculator(self, filter):
        homepage = HomePage()
        homepage.open_all_products()
        homepage.open_products_by_name('Калькулятор страхования дома')

        self.filter_offers(filter)
        self.verify_fire_chip_in_all_offers(filter)

