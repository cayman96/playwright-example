# biblioteka do regexów
import pytest
# import Page i expect'a z playwrighta
from playwright.sync_api import Page, expect
from models.main_page import MainPage

# deklaracja funkcji z testu, jako że używamy pytesta to musi się zaczynać od test, tak samo plik się musi tak zaczynać
# a tu oznaczyłem, którego fixture'a ma użyć
@pytest.mark.usefixtures("mainpage")
def test_goto_blog(page: Page):
    main = MainPage(page)
    main.go_to_blogs()

@pytest.mark.usefixtures("mainpage")
def test_goto_offers(page: Page):
    main = MainPage(page)
    main.go_to_offers()

@pytest.mark.usefixtures("mainpage")
def test_pick_currency(page: Page):
    currencies = ("GBP", "USD")
    main = MainPage(page)
    for i in currencies:
        main.show_currency_list()
        main.pick_currency(i)

@pytest.mark.usefixtures("mainpage")
def test_search_hotel_or_city(page: Page):
    main = MainPage(page)
    main.get_search_text()
    main.type_in_city("Dubai")
    main.type_in_check_in("01/01/2023")
    main.type_in_check_out("30/06/2023")
    main.search()
