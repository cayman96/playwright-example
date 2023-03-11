import re

from playwright.sync_api import expect

# ah, nasz niesławny page object model - klasa MainPage.
class MainPage:
    # standard, __init__, żeby sobie do obiektu przypisać lokatory, page jako argument, a potem z niego lokatory
    def __init__(self, page):
        self.page = page
        self.blog_btn = self.page.get_by_role("link", name=re.compile("^Blog$"))
        self.offer_btn = self.page.get_by_role("link", name=re.compile("^Offers$"))
        """
        ajjj, xpathy... na razie ich nie chcę zmieniać, bo kod z nimi działa, zresztą nawet w dokumentacji
        Playwrighta się to odradza robić, jednak na razie dzięki nim mój kod działą.
        Zdecydowanie trzeba tu wrócić i dokonać refaktoryzacji.
        """
        self.currency_btn = self.page.locator("xpath=//html/body/nav/div/div[2]/ul[2]/ul/li[2]/a/strong")
        self.currency_list = self.page.locator("xpath=//html/body/nav/div/div[2]/ul[2]/ul/li[2]/ul")
        self.search_field = self.page.get_by_text(re.compile("Search by Hotel or City Name"))
        self.search_btn = self.page.get_by_role("button", name=re.compile("Search"))
        # j.w. generalnie, staraj używać się get_by_role lub get_by_text
        self.check_in = self.page.locator("xpath=//*[@id='dpd1']/div/input")
        self.check_out = self.page.locator("xpath=//*[@id='dpd2']/div/input")
        self.adults_child = self.page.get_by_text("2 Adult 0 Child")

    """
    simple test - sprawdza, czy przycisk jest dostępny i zawiera w linku demo/blog
    potem klika, sprawdza url'a czy jest to co wyżej i czy w tytule jest Blog.
    """
    def go_to_blogs(self):
        expect(self.blog_btn).to_be_visible()
        expect(self.blog_btn).to_have_attribute("href", re.compile(".*demo/blog"))
        self.blog_btn.click()
        expect(self.page).to_have_url(re.compile(".*/demo/blog"))
        expect(self.page).to_have_title(re.compile("Blog"))

    """
    analogicznie do poprzedniej metody, tylko offers
    """
    def go_to_offers(self):
        expect(self.offer_btn).to_be_visible()
        expect(self.offer_btn).to_have_attribute("href", re.compile(".*/demo/offers"))
        self.offer_btn.click()
        expect(self.page).to_have_url(re.compile(".*/demo/offers"))
        expect(self.page).to_have_title(re.compile("Special Offers"))

    """
    szuka i oczekuje, aż przycisk od waluty jest widoczny
    potem hover, by wyświetlić listę walut
    """
    def show_currency_list(self):
        expect(self.currency_btn).to_be_visible()
        self.currency_btn.hover()

    """
    pobiera z argumentu nazwę waluty, potem szuka jej na liście i klika, a następnie sprawdza,
    czy waluta się zmieniłą poprzez porównanie curra z tekstem w buttonie od walut
    """
    def pick_currency(self, curr: str):
        expect(self.currency_list).to_be_visible()
        target = self.page.get_by_role("link", name=curr, exact=True)
        expect(target).to_be_visible()
        target.click()
        expect(self.currency_btn).to_contain_text(f"{curr}")

    """
    tutaj tylko sprawdza, czy pole od szukania jest widoczne
    nie wiem, czy tej metody się nie pozbyć i nie podciągnąć jej pod metodę type_in_city.
    zastanowię się podczas refaktoryzacji kodu.
    """
    def get_search_text(self):
        expect(self.search_field).to_be_visible()

    # pobiera se city z argumentu, wpisuje do pola szukajki i szuka na liście tej lokalizacji
    def type_in_city(self, city: str):
        self.search_field.click()
        self.search_field.type(city)
        expect(self.page.get_by_text("Locations")).to_be_visible()
        # korzystanie z last też nie jest do końca rekomendowane.
        location = self.page.get_by_text(city).last
        expect(location).to_be_visible()
        location.click()

    # wprowadza datę check_in w odpowiednim formacie
    def type_in_check_in(self, date: str):
        expect(self.check_in).to_be_visible()
        self.check_in.type(date)

    # wprowadza datę check_out w odpowiednim formacie
    def type_in_check_out(self, date: str):
        expect(self.check_out).to_be_visible()
        self.check_out.type(date)
    """
    jedna uwaga do powyższych dwóch metod: one wpisują bezpośrednio daty, nie wybierają jej z datepickera.
    dla pełnego pokrycia powinno się zaimplementować i to, co mamy wyżej, i obsługę datepickera.
    ----------------------
    Żeby już nie robić kolejnego komentarza, metoda search sporawdza, czy przycisk jest widoczny i włączony,
    a następnie klika, żeby wyszukać wyniki na podstawie ww. metod
    """
    def search(self):
        expect(self.search_btn).to_be_visible()
        expect(self.search_btn).to_be_enabled()
        self.search_btn.click()
        # funkcja niedokończona, dopisać sprawdzenie, czy jesteśmy na stronie z resultami i wyniki


# tu tak na wszelki wypadek, jakby nam się zachciało sprawdzić klasę na osobno wywoływanych metodach.
if __name__ == '__main__':
    print("You're not supposed to run me!")
