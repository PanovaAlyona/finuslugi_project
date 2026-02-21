from selene import browser, by, be, have


class HomePage:
    def open(self, url="https://finuslugi.ru/"):
        browser.open(url)
        browser.element(by.text("Все продукты")).should(be.visible)

    def open_all_products(self):
        browser.element(by.text("Все продукты")).should(be.visible).should(
            be.clickable
        ).click()
        browser.all(".HomeProductsModal_chipText__S8P0F").should(
            have.size_greater_than_or_equal(1)
        )

    def open_products_by_name(self, name):
        browser.all(".HomeProductsModal_chipText__S8P0F").element_by(
            have.text(name)
        ).should(be.visible).should(be.clickable).click()
