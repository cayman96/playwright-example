import re

from playwright.sync_api import expect


class MainPage:
    def __init__(self, page):
        self.page = page
        self.blog_btn = self.page.get_by_role("link", name=re.compile("^Blog$"))
        self.offer_btn = self.page.get_by_role("link", name=re.compile("^Offers$"))
        self.currency_btn = self.page.locator("xpath=//html/body/nav/div/div[2]/ul[2]/ul/li[2]/a/strong")
        self.currency_list = self.page.locator("xpath=//html/body/nav/div/div[2]/ul[2]/ul/li[2]/ul")

    def navigate(self):
        self.page.goto("http://www.kurs-selenium.pl/demo/")
        expect(self.page).to_have_title(re.compile("PHPTRAVELS"))

    def go_to_blogs(self):
        expect(self.blog_btn).to_be_visible()
        expect(self.blog_btn).to_have_attribute("href", re.compile(".*demo/blog"))
        self.blog_btn.click()
        expect(self.page).to_have_url(re.compile(".*/demo/blog"))
        expect(self.page).to_have_title(re.compile("Blog"))

    def go_to_offers(self):
        expect(self.offer_btn).to_be_visible()
        expect(self.offer_btn).to_have_attribute("href", re.compile(".*/demo/offers"))
        self.offer_btn.click()
        expect(self.page).to_have_url(re.compile(".*/demo/offers"))
        expect(self.page).to_have_title(re.compile("Special Offers"))

    def show_currency_list(self):
        expect(self.currency_btn).to_be_visible()
        self.currency_btn.hover()

    def pick_currency(self, curr: str):
        expect(self.currency_list).to_be_visible()
        target = self.page.get_by_text(f" {curr} ").last
        expect(target).to_be_visible()
        target.click()
        expect(self.currency_btn).to_contain_text(f" {curr} ")


if __name__ == '__main__':
    print("You're not supposed to run me!")
