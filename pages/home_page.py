from selene import browser


class HomePage:

    def open(self, url="https://finuslugi.ru/"):
        browser.open(url)