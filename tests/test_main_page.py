# well, podstawa - pytest. Tutaj służy do "wstrzykania" naszych fixture'ów deklarowanych w conftest.
import pytest
# import Page i expect'a z playwrighta
from playwright.sync_api import Page
# importujemy nasz page object model
from models.main_page import MainPage

"""
standardowo - każdy test musi zaczynać się na 'test_' lib kończyć na '_test' (no, chyba że to z końcówką aplikuje się
tylko do nazw plików. Regardless, test w nazwie musi być
"""
@pytest.mark.usefixtures("main_page")  # użycie fixture'a
def test_goto_blog(page: Page):
    # prosty test - przejście do strony "blogs", metoda wywoływana z obiektu typu "MainPage"
    main = MainPage(page)
    main.go_to_blogs()

@pytest.mark.usefixtures("main_page")
def test_goto_offers(page: Page):
    # tak, do każdego testu deklarujemy nowy Page Object Model. i ten test też jest prosty, przejście do "Offers"
    main = MainPage(page)
    main.go_to_offers()

@pytest.mark.usefixtures("main_page")
def test_pick_currency(page: Page):
    # prosta krotka, sprawdzamy przełączanie walut i tutaj potrzebujemy min. dwóch walut
    currencies = ("GBP", "USD")
    main = MainPage(page)
    # tyle, ile jest rzeczy w ktorce, tyle razy się muszą się wykonać poniższe metody
    for i in currencies:
        main.show_currency_list()
        main.pick_currency(i)

# ten test - oczekujemy, że przejdzie, na podstawie np. nie wiem, wiemy że coś jest w bazie i jest git
@pytest.mark.usefixtures("main_page")
def test_search_hotel_or_city_pass(page: Page):
    main = MainPage(page)
    main.get_search_text()
    main.type_in_city("Dubai")
    main.type_in_check_in("01/01/2023")
    main.type_in_check_out("30/06/2023")
    main.search()

# ten sam test, co wyżej, jednak tu spodziewamy się, że zawali, stąd xfail
@pytest.mark.usefixtures("main_page")
@pytest.mark.xfail
def test_search_hotel_or_city_fail(page: Page):
    main = MainPage(page)
    main.get_search_text()
    main.type_in_city("Zadupie")
    main.type_in_check_in("01/01/2023")
    main.type_in_check_out("30/06/2023")
    main.search()
