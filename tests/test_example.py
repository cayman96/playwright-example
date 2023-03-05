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
    expect(main.page).to_have_title(re.compile("PHPTRAVELS"))
    expect(main.blog_btn).to_have_attribute("href", re.compile(".*demo/blog"))
    main.go_to_blogs()
    expect(main.page).to_have_url(re.compile(".*/demo/blog"))
    expect(main.page).to_have_title(re.compile("Blog"))

# @pytest.mark.usefixtures("mainpage")
def test_goto_offers(page: Page):
    main = MainPage(page)
    main.navigate()
    expect(main.page).to_have_title(re.compile("PHPTRAVELS"))
    expect(main.offer_btn).to_have_attribute("href", re.compile(".*/demo/offers"))
    main.go_to_offers()
    expect(page).to_have_url(re.compile(".*/demo/offers"))
    expect(page).to_have_title(re.compile("Special Offers"))

