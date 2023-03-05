import re
class MainPage:
    def __init__(self, page):
        self.page = page
        self.blog_btn = self.page.get_by_role("link", name=re.compile("^Blog$"))
        self.offer_btn = self.page.get_by_role("link", name=re.compile("^Offers$"))

    def navigate(self):
        self.page.goto("http://www.kurs-selenium.pl/demo/")

    def go_to_blogs(self):
        self.blog_btn.click()

    def go_to_offers(self):
        self.offer_btn.click()


if __name__ == '__main__':
    print("You're not supposed to run me!")
