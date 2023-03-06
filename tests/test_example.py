# biblioteka do regexów
import re
import pytest
# import Page i expect'a z playwrighta
from playwright.sync_api import Page, expect
from models.main_page import MainPage


# deklaracja funkcji z testu, jako że używamy pytesta to musi się zaczynać od test, tak samo plik się musi tak zaczynać
# a tu oznaczyłem, którego fixture'a ma użyć
# @pytest.mark.usefixtures("mainpage")
def test_goto_blog(page: Page):
    main = MainPage(page)
    main.navigate()
    main.go_to_blogs()
# @pytest.mark.usefixtures("mainpage")
def test_goto_offers(page: Page):
    main = MainPage(page)
    main.navigate()
    main.go_to_offers()

def test_pick_currency(page: Page):
    currencies = ("GBP", "USD")
    main = MainPage(page)
    main.navigate()
    for i in currencies:
        main.show_currency_list()
        main.pick_currency(i)


