from selene import browser, by, be, have


class HomePage:

    def open(self, url="https://finuslugi.ru/"):
        browser.open(url)

    def open_all_products(self):
        browser.element(by.text('Все продукты')).click()

    def open_products_by_name(self, name):
        browser.all('.HomeProductsModal_chipText__S8P0F').element_by(have.text(name)).should(be.clickable).click()

